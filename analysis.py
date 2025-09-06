"""
AI Energy Analysis: From Watts to World Impact
===============================================

This script performs comprehensive analysis of AI energy scenarios,
exploring the implications of different power levels, years, and energy mixes.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from energy_model import (
    run_scenario, watts_to_h100e, calculate_capex,
    moores_law, power_efficiency, cost_efficiency,
    WORLD_ELECTRICITY_2024, WORLD_GDP_2024
)


def create_scenario_matrix():
    """Create a matrix of scenarios for analysis."""
    
    # Power levels: from 10 GW to 2 TW
    power_levels_gw = [10, 30, 100, 300, 1000, 2000]
    
    # Years to analyze
    years = [2025, 2030, 2035, 2040]
    
    # Energy mixes
    energy_mixes = {
        'Pure Solar': {'solar': 1.0, 'gas': 0.0},
        'Pure Gas': {'solar': 0.0, 'gas': 1.0},
        'Balanced': {'solar': 0.5, 'gas': 0.5},
        'Solar Heavy': {'solar': 0.7, 'gas': 0.3},
    }
    
    results = []
    
    for power_gw in power_levels_gw:
        for year in years:
            for mix_name, energy_mix in energy_mixes.items():
                scenario = run_scenario(
                    watts=power_gw * 1e9,
                    year=year,
                    energy_mix=energy_mix
                )
                
                results.append({
                    'Power_GW': power_gw,
                    'Year': year,
                    'Energy_Mix': mix_name,
                    'H100e_Count': scenario.compute['h100e_count'],
                    'Total_FLOPS': scenario.compute['total_flops'],
                    'CapEx_USD': scenario.capex['total_capex'],
                    'CapEx_per_Watt': scenario.capex['capex_per_watt'],
                    'Pct_World_Electricity': scenario.global_fractions['electricity_fraction'] * 100,
                    'Pct_World_GDP': scenario.global_fractions['gdp_fraction'] * 100,
                    'Transformers_Needed': scenario.infrastructure['transformers'],
                    'PV_Modules_Needed': scenario.infrastructure['pv_modules'],
                    'Turbines_Needed': scenario.infrastructure['turbines'],
                    'Annual_Tokens': scenario.tokens['annual_tokens'],
                })
    
    return pd.DataFrame(results)


def analyze_bottlenecks(df):
    """Identify and analyze bottlenecks across scenarios."""
    
    print("\n" + "="*80)
    print("BOTTLENECK ANALYSIS")
    print("="*80)
    
    # Find scenarios that exceed world electricity
    electricity_bottleneck = df[df['Pct_World_Electricity'] > 100]
    if not electricity_bottleneck.empty:
        print("\n⚠️  Scenarios exceeding current world electricity production:")
        for _, row in electricity_bottleneck.iterrows():
            print(f"  - {row['Power_GW']:.0f} GW in {row['Year']}: "
                  f"{row['Pct_World_Electricity']:.1f}% of world electricity")
    
    # Find the threshold where we hit 100% of world electricity
    for year in [2025, 2030, 2035, 2040]:
        year_data = df[(df['Year'] == year) & (df['Energy_Mix'] == 'Balanced')]
        year_data = year_data.sort_values('Power_GW')
        
        # Find the power level where we cross 100%
        for i in range(len(year_data) - 1):
            if year_data.iloc[i]['Pct_World_Electricity'] < 100 and \
               year_data.iloc[i+1]['Pct_World_Electricity'] > 100:
                # Interpolate
                p1, e1 = year_data.iloc[i]['Power_GW'], year_data.iloc[i]['Pct_World_Electricity']
                p2, e2 = year_data.iloc[i+1]['Power_GW'], year_data.iloc[i+1]['Pct_World_Electricity']
                threshold_power = p1 + (100 - e1) * (p2 - p1) / (e2 - e1)
                print(f"\n  Year {year}: ~{threshold_power:.0f} GW uses 100% of current world electricity")
                break


def plot_feasibility_landscape():
    """Create a heatmap showing feasibility across power levels and years."""
    
    # Create scenario data
    power_levels_gw = np.logspace(1, 3.3, 30)  # 10 GW to 2 TW
    years = np.arange(2025, 2041)
    
    feasibility_matrix = np.zeros((len(years), len(power_levels_gw)))
    
    for i, year in enumerate(years):
        for j, power_gw in enumerate(power_levels_gw):
            scenario = run_scenario(
                watts=power_gw * 1e9,
                year=year,
                energy_mix={'solar': 0.5, 'gas': 0.5}
            )
            
            # Feasibility score (0-100)
            # Based on fraction of world electricity
            electricity_frac = scenario.global_fractions['electricity_fraction']
            
            if electricity_frac < 0.1:  # < 10% of world electricity
                score = 100  # Highly feasible
            elif electricity_frac < 0.5:  # 10-50%
                score = 80 - 40 * (electricity_frac - 0.1) / 0.4
            elif electricity_frac < 1.0:  # 50-100%
                score = 40 - 30 * (electricity_frac - 0.5) / 0.5
            elif electricity_frac < 2.0:  # 100-200%
                score = 10 - 9 * (electricity_frac - 1.0)
            else:
                score = 1  # Essentially impossible
            
            feasibility_matrix[i, j] = score
    
    # Create the plot
    fig, ax = plt.subplots(figsize=(12, 8))
    
    im = ax.imshow(feasibility_matrix, aspect='auto', cmap='RdYlGn', 
                   vmin=0, vmax=100, origin='lower')
    
    # Set ticks
    ax.set_xticks(np.arange(0, len(power_levels_gw), 5))
    ax.set_xticklabels([f'{int(p)}' for p in power_levels_gw[::5]])
    ax.set_yticks(np.arange(len(years)))
    ax.set_yticklabels(years)
    
    # Labels
    ax.set_xlabel('Power (GW)', fontsize=12)
    ax.set_ylabel('Year', fontsize=12)
    ax.set_title('AI Energy Feasibility Landscape\n(Green = Feasible, Red = Infeasible)', 
                 fontsize=14, fontweight='bold')
    
    # Add colorbar
    cbar = plt.colorbar(im, ax=ax)
    cbar.set_label('Feasibility Score (0-100)', rotation=270, labelpad=20)
    
    # Add contour lines for key thresholds
    contour_levels = [10, 50, 100]  # % of world electricity
    for level in contour_levels:
        # Calculate the contour
        contour_line = []
        for i, year in enumerate(years):
            for j, power_gw in enumerate(power_levels_gw):
                scenario = run_scenario(
                    watts=power_gw * 1e9,
                    year=year,
                    energy_mix={'solar': 0.5, 'gas': 0.5}
                )
                if abs(scenario.global_fractions['electricity_fraction'] * 100 - level) < 5:
                    contour_line.append((j, i))
        
        if contour_line:
            x_coords, y_coords = zip(*contour_line)
            ax.plot(x_coords, y_coords, 'k--', alpha=0.5, linewidth=1)
            ax.text(x_coords[-1], y_coords[-1], f'{level}%', fontsize=9)
    
    plt.tight_layout()
    return fig


def plot_cost_curves():
    """Plot how costs evolve over time for different power levels."""
    
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    power_levels_gw = [30, 100, 300, 1000]
    years = np.arange(2025, 2041)
    
    for power_gw in power_levels_gw:
        capex_values = []
        capex_per_watt = []
        h100e_counts = []
        cost_per_h100e = []
        
        for year in years:
            scenario = run_scenario(
                watts=power_gw * 1e9,
                year=year,
                energy_mix={'solar': 0.5, 'gas': 0.5}
            )
            
            capex_values.append(scenario.capex['total_capex'] / 1e12)  # Trillions
            capex_per_watt.append(scenario.capex['capex_per_watt'])
            h100e_counts.append(scenario.compute['h100e_count'] / 1e9)  # Billions
            cost_per_h100e.append(scenario.capex['cost_per_h100e'])
        
        # Total CapEx
        axes[0, 0].plot(years, capex_values, label=f'{power_gw} GW', linewidth=2)
        axes[0, 0].set_xlabel('Year')
        axes[0, 0].set_ylabel('Total CapEx (Trillion USD)')
        axes[0, 0].set_title('Total Capital Expenditure Over Time')
        axes[0, 0].legend()
        axes[0, 0].grid(True, alpha=0.3)
        
        # CapEx per Watt
        axes[0, 1].plot(years, capex_per_watt, label=f'{power_gw} GW', linewidth=2)
        axes[0, 1].set_xlabel('Year')
        axes[0, 1].set_ylabel('CapEx per Watt (USD/W)')
        axes[0, 1].set_title('Capital Efficiency Over Time')
        axes[0, 1].legend()
        axes[0, 1].grid(True, alpha=0.3)
        
        # H100e Count
        axes[1, 0].plot(years, h100e_counts, label=f'{power_gw} GW', linewidth=2)
        axes[1, 0].set_xlabel('Year')
        axes[1, 0].set_ylabel('H100 Equivalents (Billions)')
        axes[1, 0].set_title('Compute Capacity Over Time')
        axes[1, 0].legend()
        axes[1, 0].grid(True, alpha=0.3)
        
        # Cost per H100e
        axes[1, 1].plot(years, cost_per_h100e, label=f'{power_gw} GW', linewidth=2)
        axes[1, 1].set_xlabel('Year')
        axes[1, 1].set_ylabel('Cost per H100e (USD)')
        axes[1, 1].set_title('Chip Cost Efficiency Over Time')
        axes[1, 1].legend()
        axes[1, 1].grid(True, alpha=0.3)
    
    plt.suptitle('Economic Trends in AI Infrastructure', fontsize=14, fontweight='bold')
    plt.tight_layout()
    return fig


def compare_to_csv_projections():
    """Compare our model to the original CSV projections."""
    
    print("\n" + "="*80)
    print("COMPARISON WITH ORIGINAL CSV PROJECTIONS")
    print("="*80)
    
    # Key data points from CSV
    csv_data = {
        2030: {'power_gw': 270.47, 'h100e': 628e6, 'capex': 2.002e12},
        2035: {'power_gw': 895.10, 'h100e': 5.37e9, 'capex': 4.941e12},
        2040: {'power_gw': 1990, 'h100e': 29.5e9, 'capex': 8.875e12},
    }
    
    print("\nYear | CSV Power | Model H100e | CSV H100e | Model CapEx | CSV CapEx")
    print("-" * 70)
    
    for year, csv_values in csv_data.items():
        # Run our model with CSV power levels
        scenario = run_scenario(
            watts=csv_values['power_gw'] * 1e9,
            year=year,
            energy_mix={'solar': 0.3, 'gas': 0.7}
        )
        
        print(f"{year} | {csv_values['power_gw']:.1f} GW | "
              f"{scenario.compute['h100e_count']:.2e} | {csv_values['h100e']:.2e} | "
              f"${scenario.capex['total_capex']:.2e} | ${csv_values['capex']:.2e}")
        
        # Calculate differences
        h100e_diff = (scenario.compute['h100e_count'] - csv_values['h100e']) / csv_values['h100e'] * 100
        capex_diff = (scenario.capex['total_capex'] - csv_values['capex']) / csv_values['capex'] * 100
        
        print(f"     | Difference: H100e {h100e_diff:+.1f}%, CapEx {capex_diff:+.1f}%")


def generate_key_insights():
    """Generate key insights from the analysis."""
    
    print("\n" + "="*80)
    print("KEY INSIGHTS")
    print("="*80)
    
    # 1. When do we hit world electricity limits?
    print("\n1. ELECTRICITY CONSTRAINTS:")
    for year in [2025, 2030, 2035, 2040]:
        for power_gw in [10, 30, 100, 300, 1000]:
            scenario = run_scenario(
                watts=power_gw * 1e9,
                year=year,
                energy_mix={'solar': 0.5, 'gas': 0.5}
            )
            if scenario.global_fractions['electricity_fraction'] > 0.95 and \
               scenario.global_fractions['electricity_fraction'] < 1.05:
                print(f"   {year}: ~{power_gw} GW ≈ 100% of current world electricity")
                break
    
    # 2. Moore's Law vs Power Efficiency
    print("\n2. EFFICIENCY IMPROVEMENTS (2025 → 2040):")
    print(f"   Moore's Law: {moores_law(2040):.1f}x improvement")
    print(f"   Power Efficiency: {1000/power_efficiency(2040):.1f}x improvement")
    print(f"   Cost Efficiency: {24000/cost_efficiency(2040):.1f}x improvement")
    
    # 3. CapEx as fraction of GDP
    print("\n3. ECONOMIC SCALE:")
    for power_gw in [100, 500, 1000, 2000]:
        scenario_2030 = run_scenario(
            watts=power_gw * 1e9,
            year=2030,
            energy_mix={'solar': 0.5, 'gas': 0.5}
        )
        print(f"   {power_gw} GW in 2030: ${scenario_2030.capex['total_capex']/1e12:.1f}T "
              f"({scenario_2030.global_fractions['gdp_fraction']*100:.1f}% of world GDP)")
    
    # 4. Token generation capacity
    print("\n4. TOKEN GENERATION CAPACITY:")
    scenario_100gw_2030 = run_scenario(
        watts=100e9,
        year=2030,
        energy_mix={'solar': 0.5, 'gas': 0.5}
    )
    print(f"   100 GW in 2030: {scenario_100gw_2030.tokens['annual_tokens']:.2e} tokens/year")
    print(f"   That's {scenario_100gw_2030.tokens['tokens_per_second']:.2e} tokens/second")
    
    # 5. Energy mix implications
    print("\n5. ENERGY MIX IMPLICATIONS (1000 GW in 2035):")
    for mix_name, energy_mix in [
        ('Pure Solar', {'solar': 1.0, 'gas': 0.0}),
        ('Pure Gas', {'solar': 0.0, 'gas': 1.0}),
        ('50/50 Mix', {'solar': 0.5, 'gas': 0.5}),
    ]:
        scenario = run_scenario(
            watts=1000e9,
            year=2035,
            energy_mix=energy_mix
        )
        print(f"   {mix_name}: {scenario.infrastructure['pv_modules']:.2e} PV modules, "
              f"{scenario.infrastructure['turbines']:.0f} turbines")


def main():
    """Run the complete analysis."""
    
    print("="*80)
    print("AI ENERGY FORECAST ANALYSIS")
    print("From Watts to World Impact")
    print("="*80)
    
    # Generate scenario matrix
    print("\nGenerating scenario matrix...")
    df = create_scenario_matrix()
    
    # Save to CSV for further analysis
    df.to_csv('scenario_analysis.csv', index=False)
    print(f"Saved {len(df)} scenarios to scenario_analysis.csv")
    
    # Analyze bottlenecks
    analyze_bottlenecks(df)
    
    # Compare to original CSV
    compare_to_csv_projections()
    
    # Generate key insights
    generate_key_insights()
    
    # Create visualizations
    print("\n" + "="*80)
    print("GENERATING VISUALIZATIONS")
    print("="*80)
    
    print("\nCreating feasibility landscape...")
    fig1 = plot_feasibility_landscape()
    fig1.savefig('feasibility_landscape.png', dpi=150, bbox_inches='tight')
    print("Saved: feasibility_landscape.png")
    
    print("\nCreating cost curves...")
    fig2 = plot_cost_curves()
    fig2.savefig('cost_curves.png', dpi=150, bbox_inches='tight')
    print("Saved: cost_curves.png")
    
    # Summary statistics
    print("\n" + "="*80)
    print("SUMMARY STATISTICS")
    print("="*80)
    
    print(f"\nScenarios analyzed: {len(df)}")
    print(f"Power range: {df['Power_GW'].min():.0f} - {df['Power_GW'].max():.0f} GW")
    print(f"CapEx range: ${df['CapEx_USD'].min()/1e9:.1f}B - ${df['CapEx_USD'].max()/1e12:.1f}T")
    print(f"H100e range: {df['H100e_Count'].min():.2e} - {df['H100e_Count'].max():.2e}")
    
    # Identify most extreme scenarios
    print("\n📊 EXTREME SCENARIOS:")
    max_electricity = df.loc[df['Pct_World_Electricity'].idxmax()]
    print(f"Highest electricity use: {max_electricity['Power_GW']:.0f} GW in "
          f"{max_electricity['Year']:.0f} = {max_electricity['Pct_World_Electricity']:.0f}% of world")
    
    max_capex = df.loc[df['CapEx_USD'].idxmax()]
    print(f"Highest CapEx: ${max_capex['CapEx_USD']/1e12:.1f}T for "
          f"{max_capex['Power_GW']:.0f} GW in {max_capex['Year']:.0f}")
    
    print("\n✅ Analysis complete!")


if __name__ == "__main__":
    main()
