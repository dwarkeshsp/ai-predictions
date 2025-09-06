"""
AI Energy and Compute Forecast Model
=====================================

This model projects AI compute and infrastructure requirements based on power consumption.
Unlike traditional forecasts that start with compute growth, this model uses power (watts)
as the independent variable and calculates resulting compute, CapEx, and infrastructure needs.

Key Features:
- Year-dependent efficiency curves (Moore's Law, power efficiency, cost efficiency)
- Infrastructure requirements (transformers, switchgear, PV modules, turbines)
- Global resource comparisons (electricity, GDP, production capacity)
- Token output estimation
- Flexible energy mix scenarios

Author: Dwarkesh Patel & Romeo Dean
Date: December 2024
"""

import numpy as np
import pandas as pd
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d


# =============================================================================
# BASE CONSTANTS
# =============================================================================

# Starting values (2024/2025 baseline)
BASE_YEAR = 2024
H100_POWER = 700  # Watts per H100
H100_COST = 24000  # USD per H100 equivalent in 2025
H100_FLOPS = 2e15  # FP8 FLOPS for H100

# Global reference values (2024)
WORLD_ELECTRICITY_2024 = 35.2e12  # Wh/year (35.2 PWh)
WORLD_GDP_2024 = 111e12  # USD (111 trillion)
WORLD_FINAL_ENERGY_2024 = 180e12  # Wh/year (180 PWh)

# Infrastructure constants (per MW of datacenter capacity)
# These are placeholder values - should be replaced with real data
TRANSFORMERS_PER_MW = 0.5  # Number of HV transformers per MW
SWITCHGEAR_PER_MW = 2.0  # Switchgear units per MW
PV_MODULES_PER_MW_SOLAR = 4000  # PV modules per MW of solar capacity
BATTERIES_MWH_PER_MW_SOLAR = 4  # MWh of batteries per MW of solar
TURBINES_PER_MW_GAS = 1.0  # Gas turbines per MW of gas capacity

# Global production capacities (annual)
GLOBAL_TRANSFORMER_PRODUCTION = 10000  # Units per year
GLOBAL_SWITCHGEAR_PRODUCTION = 50000  # Units per year
GLOBAL_PV_MODULE_PRODUCTION = 1e9  # Modules per year (1 TW equivalent)
GLOBAL_BATTERY_PRODUCTION = 500  # GWh per year
GLOBAL_TURBINE_PRODUCTION = 5000  # Units per year


# =============================================================================
# EFFICIENCY CURVES
# =============================================================================

def moores_law(year: int) -> float:
    """
    Moore's Law: Improvement in compute performance per chip (H100e/H100-sized-die).
    Interpolates decay from 1.35x to 1.25x growth rate from 2025 to 2040.
    
    Args:
        year: The year for which to calculate the improvement
        
    Returns:
        Cumulative improvement factor relative to 2024 baseline (1.0)
    """
    if year <= BASE_YEAR:
        return 1.0
    
    # Growth rates: 1.35 in 2025, decaying to 1.25 by 2040
    years = np.array([2025, 2040])
    growth_rates = np.array([1.35, 1.25])
    
    # Create interpolation function
    interp_func = interp1d(years, growth_rates, kind='linear', fill_value='extrapolate')
    
    # Calculate cumulative improvement
    cumulative = 1.0
    for y in range(BASE_YEAR + 1, year + 1):
        if y >= 2040:
            yr_growth = 1.25
        else:
            yr_growth = float(interp_func(min(y, 2040)))
        cumulative *= yr_growth
    
    return cumulative


def power_efficiency(year: int) -> float:
    """
    Power efficiency: Watts per H100 equivalent.
    Starting at 1000W in 2025, improving 1.3x/year initially, decaying to 1.2x/year by 2040.
    
    Args:
        year: The year for which to calculate power consumption
        
    Returns:
        Watts per H100 equivalent
    """
    if year <= 2024:
        return 1000.0
    
    # Growth rates (improvement means lower W/H100e, so we use 1/growth)
    years = np.array([2025, 2040])
    improvement_rates = np.array([1.3, 1.2])  # Improvement factors
    
    # Calculate watts per H100e
    base_watts = 1000.0  # Starting point in 2025
    
    if year == 2025:
        return base_watts
    
    # Create interpolation function
    interp_func = interp1d(years, improvement_rates, kind='linear', fill_value='extrapolate')
    
    # Calculate cumulative improvement (lower watts = better)
    watts = base_watts
    for y in range(2026, year + 1):
        if y >= 2040:
            yr_improvement = 1.2
        else:
            yr_improvement = float(interp_func(min(y, 2040)))
        watts = watts / yr_improvement
    
    return watts


def cost_efficiency(year: int) -> float:
    """
    Cost efficiency: USD per H100 equivalent.
    Starting at $24K in 2025, improving 1.3x/year initially, decaying to 1.2x/year by 2040.
    
    Args:
        year: The year for which to calculate cost
        
    Returns:
        USD per H100 equivalent
    """
    if year <= 2024:
        return 24000.0
    
    # Growth rates (improvement means lower $/H100e, so we use 1/growth)
    years = np.array([2025, 2040])
    improvement_rates = np.array([1.3, 1.2])  # Improvement factors
    
    # Calculate cost per H100e
    base_cost = 24000.0  # Starting point in 2025
    
    if year == 2025:
        return base_cost
    
    # Create interpolation function
    interp_func = interp1d(years, improvement_rates, kind='linear', fill_value='extrapolate')
    
    # Calculate cumulative improvement (lower cost = better)
    cost = base_cost
    for y in range(2026, year + 1):
        if y >= 2040:
            yr_improvement = 1.2
        else:
            yr_improvement = float(interp_func(min(y, 2040)))
        cost = cost / yr_improvement
    
    return cost


# =============================================================================
# CORE CALCULATION FUNCTIONS
# =============================================================================

def watts_to_h100e(watts: float, year: int) -> Dict[str, float]:
    """
    Convert power consumption to H100 equivalents.
    
    Args:
        watts: Power consumption in watts
        year: Year for efficiency calculations
        
    Returns:
        Dictionary with H100e count and related metrics
    """
    watts_per_h100e = power_efficiency(year)
    h100e_count = watts / watts_per_h100e
    
    # Calculate theoretical FLOPS
    moores_factor = moores_law(year)
    flops_per_h100e = H100_FLOPS * moores_factor
    total_flops = h100e_count * flops_per_h100e
    
    return {
        'h100e_count': h100e_count,
        'watts_per_h100e': watts_per_h100e,
        'total_flops': total_flops,
        'flops_per_h100e': flops_per_h100e
    }


def calculate_capex(watts: float, year: int) -> Dict[str, float]:
    """
    Calculate CapEx requirements for given power and year.
    
    Args:
        watts: Power consumption in watts
        year: Year for cost calculations
        
    Returns:
        Dictionary with CapEx breakdown
    """
    compute_info = watts_to_h100e(watts, year)
    cost_per_h100e = cost_efficiency(year)
    
    # Compute CapEx (just the chips)
    compute_capex = compute_info['h100e_count'] * cost_per_h100e
    
    # Non-compute CapEx (cooling, power, networking, etc.)
    # Assumption: Non-compute is 50% of compute cost initially, improving over time
    non_compute_ratio = 0.5 * (1.1 ** (year - 2025))  # Slightly increasing ratio
    non_compute_capex = compute_capex * non_compute_ratio
    
    total_capex = compute_capex + non_compute_capex
    
    return {
        'total_capex': total_capex,
        'compute_capex': compute_capex,
        'non_compute_capex': non_compute_capex,
        'cost_per_h100e': cost_per_h100e,
        'capex_per_watt': total_capex / watts
    }


def calculate_infrastructure(watts: float, energy_mix: Dict[str, float]) -> Dict[str, float]:
    """
    Calculate infrastructure requirements for given power and energy mix.
    
    Args:
        watts: Power consumption in watts
        energy_mix: Dictionary with 'solar' and 'gas' percentages (should sum to 1.0)
        
    Returns:
        Dictionary with infrastructure requirements
    """
    mw = watts / 1e6  # Convert to megawatts
    
    # Grid infrastructure (needed regardless of source)
    transformers = mw * TRANSFORMERS_PER_MW
    switchgear = mw * SWITCHGEAR_PER_MW
    
    # Solar infrastructure
    solar_fraction = energy_mix.get('solar', 0.0)
    solar_mw = mw * solar_fraction
    # Account for capacity factor (~25% for solar)
    solar_capacity_needed = solar_mw * 4  # Need 4x capacity due to capacity factor
    pv_modules = solar_capacity_needed * PV_MODULES_PER_MW_SOLAR
    batteries_mwh = solar_capacity_needed * BATTERIES_MWH_PER_MW_SOLAR
    
    # Gas infrastructure
    gas_fraction = energy_mix.get('gas', 0.0)
    gas_mw = mw * gas_fraction
    turbines = gas_mw * TURBINES_PER_MW_GAS
    
    return {
        'transformers': transformers,
        'switchgear': switchgear,
        'pv_modules': pv_modules,
        'batteries_mwh': batteries_mwh,
        'turbines': turbines,
        'total_mw': mw,
        'solar_mw_capacity': solar_capacity_needed,
        'gas_mw': gas_mw
    }


def estimate_token_output(h100e_count: float, utilization: float = 0.5) -> Dict[str, float]:
    """
    Estimate token generation capacity.
    
    Args:
        h100e_count: Number of H100 equivalents
        utilization: Average utilization rate (0-1)
        
    Returns:
        Dictionary with token output estimates
    """
    # Rough estimates based on current models
    # H100 can generate ~10K tokens/second for inference on large models
    tokens_per_second_per_h100e = 10000
    
    # Account for utilization
    effective_h100e = h100e_count * utilization
    
    # Tokens per second
    tokens_per_second = effective_h100e * tokens_per_second_per_h100e
    
    # Annual tokens (seconds in a year = 365.25 * 24 * 3600)
    seconds_per_year = 365.25 * 24 * 3600
    annual_tokens = tokens_per_second * seconds_per_year
    
    return {
        'tokens_per_second': tokens_per_second,
        'annual_tokens': annual_tokens,
        'effective_h100e': effective_h100e
    }


def calculate_global_fractions(watts: float, capex: float, infrastructure: Dict) -> Dict[str, float]:
    """
    Calculate what fraction of global resources this represents.
    
    Args:
        watts: Power consumption in watts
        capex: Total CapEx in USD
        infrastructure: Infrastructure requirements dictionary
        
    Returns:
        Dictionary with global resource fractions
    """
    # Power fractions
    annual_energy = watts * 365.25 * 24  # Watt-hours per year
    electricity_fraction = annual_energy / WORLD_ELECTRICITY_2024
    final_energy_fraction = annual_energy / WORLD_FINAL_ENERGY_2024
    
    # Economic fractions
    gdp_fraction = capex / WORLD_GDP_2024
    
    # Infrastructure fractions
    transformer_fraction = infrastructure['transformers'] / GLOBAL_TRANSFORMER_PRODUCTION
    switchgear_fraction = infrastructure['switchgear'] / GLOBAL_SWITCHGEAR_PRODUCTION
    pv_fraction = infrastructure['pv_modules'] / GLOBAL_PV_MODULE_PRODUCTION
    battery_fraction = infrastructure['batteries_mwh'] / (GLOBAL_BATTERY_PRODUCTION * 1000)  # Convert GWh to MWh
    turbine_fraction = infrastructure['turbines'] / GLOBAL_TURBINE_PRODUCTION
    
    return {
        'electricity_fraction': electricity_fraction,
        'final_energy_fraction': final_energy_fraction,
        'gdp_fraction': gdp_fraction,
        'transformer_fraction': transformer_fraction,
        'switchgear_fraction': switchgear_fraction,
        'pv_fraction': pv_fraction,
        'battery_fraction': battery_fraction,
        'turbine_fraction': turbine_fraction
    }


# =============================================================================
# SCENARIO ANALYSIS
# =============================================================================

@dataclass
class Scenario:
    """Container for a complete scenario analysis."""
    watts: float
    year: int
    energy_mix: Dict[str, float]
    compute: Dict[str, float]
    capex: Dict[str, float]
    infrastructure: Dict[str, float]
    tokens: Dict[str, float]
    global_fractions: Dict[str, float]
    
    def summary(self) -> str:
        """Generate a human-readable summary of the scenario."""
        gw = self.watts / 1e9
        summary = f"\n{'='*60}\n"
        summary += f"Scenario: {gw:.1f} GW in {self.year}\n"
        summary += f"Energy Mix: {self.energy_mix}\n"
        summary += f"{'='*60}\n\n"
        
        summary += "COMPUTE:\n"
        summary += f"  H100 equivalents: {self.compute['h100e_count']:.2e}\n"
        summary += f"  Total FLOPS: {self.compute['total_flops']:.2e}\n"
        summary += f"  Watts per H100e: {self.compute['watts_per_h100e']:.1f}\n\n"
        
        summary += "CAPEX:\n"
        summary += f"  Total CapEx: ${self.capex['total_capex']:.2e}\n"
        summary += f"  Compute CapEx: ${self.capex['compute_capex']:.2e}\n"
        summary += f"  CapEx per Watt: ${self.capex['capex_per_watt']:.2f}\n\n"
        
        summary += "INFRASTRUCTURE:\n"
        summary += f"  Transformers needed: {self.infrastructure['transformers']:.0f}\n"
        summary += f"  Switchgear needed: {self.infrastructure['switchgear']:.0f}\n"
        if self.energy_mix.get('solar', 0) > 0:
            summary += f"  PV modules needed: {self.infrastructure['pv_modules']:.2e}\n"
            summary += f"  Battery storage: {self.infrastructure['batteries_mwh']:.0f} MWh\n"
        if self.energy_mix.get('gas', 0) > 0:
            summary += f"  Gas turbines needed: {self.infrastructure['turbines']:.0f}\n\n"
        
        summary += "TOKENS:\n"
        summary += f"  Tokens per second: {self.tokens['tokens_per_second']:.2e}\n"
        summary += f"  Annual tokens: {self.tokens['annual_tokens']:.2e}\n\n"
        
        summary += "GLOBAL RESOURCE USAGE:\n"
        summary += f"  % of world electricity: {self.global_fractions['electricity_fraction']*100:.1f}%\n"
        summary += f"  % of world GDP (for CapEx): {self.global_fractions['gdp_fraction']*100:.2f}%\n"
        
        # Highlight bottlenecks
        bottlenecks = []
        if self.global_fractions['transformer_fraction'] > 0.1:
            bottlenecks.append(f"Transformers ({self.global_fractions['transformer_fraction']*100:.0f}% of global production)")
        if self.global_fractions['pv_fraction'] > 0.1:
            bottlenecks.append(f"PV modules ({self.global_fractions['pv_fraction']*100:.0f}% of global production)")
        if self.global_fractions['turbine_fraction'] > 0.1:
            bottlenecks.append(f"Turbines ({self.global_fractions['turbine_fraction']*100:.0f}% of global production)")
        
        if bottlenecks:
            summary += f"\nPOTENTIAL BOTTLENECKS:\n"
            for bottleneck in bottlenecks:
                summary += f"  ⚠️  {bottleneck}\n"
        
        return summary


def run_scenario(watts: float, year: int, energy_mix: Dict[str, float]) -> Scenario:
    """
    Run a complete scenario analysis.
    
    Args:
        watts: Power consumption in watts
        year: Year for projections
        energy_mix: Energy source mix (e.g., {'solar': 0.5, 'gas': 0.5})
        
    Returns:
        Scenario object with all calculations
    """
    # Normalize energy mix
    total = sum(energy_mix.values())
    if total > 0:
        energy_mix = {k: v/total for k, v in energy_mix.items()}
    
    # Run calculations
    compute = watts_to_h100e(watts, year)
    capex = calculate_capex(watts, year)
    infrastructure = calculate_infrastructure(watts, energy_mix)
    tokens = estimate_token_output(compute['h100e_count'])
    global_fractions = calculate_global_fractions(watts, capex['total_capex'], infrastructure)
    
    return Scenario(
        watts=watts,
        year=year,
        energy_mix=energy_mix,
        compute=compute,
        capex=capex,
        infrastructure=infrastructure,
        tokens=tokens,
        global_fractions=global_fractions
    )


# =============================================================================
# VISUALIZATION FUNCTIONS
# =============================================================================

def plot_efficiency_curves():
    """Plot the three efficiency curves over time."""
    years = np.arange(2025, 2041)
    
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    
    # Moore's Law
    moores_values = [moores_law(y) for y in years]
    axes[0].plot(years, moores_values, 'b-', linewidth=2)
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('H100e per H100-sized die')
    axes[0].set_title("Moore's Law (Compute Density)")
    axes[0].grid(True, alpha=0.3)
    
    # Power Efficiency
    power_values = [power_efficiency(y) for y in years]
    axes[1].plot(years, power_values, 'g-', linewidth=2)
    axes[1].set_xlabel('Year')
    axes[1].set_ylabel('Watts per H100e')
    axes[1].set_title('Power Efficiency')
    axes[1].grid(True, alpha=0.3)
    axes[1].invert_yaxis()  # Lower is better
    
    # Cost Efficiency
    cost_values = [cost_efficiency(y) for y in years]
    axes[2].plot(years, cost_values, 'r-', linewidth=2)
    axes[2].set_xlabel('Year')
    axes[2].set_ylabel('USD per H100e')
    axes[2].set_title('Cost Efficiency')
    axes[2].grid(True, alpha=0.3)
    axes[2].invert_yaxis()  # Lower is better
    
    plt.suptitle('Efficiency Improvement Curves (2025-2040)', fontsize=14, fontweight='bold')
    plt.tight_layout()
    return fig


def plot_power_scaling(years: List[int] = [2025, 2030, 2035, 2040]):
    """Plot how metrics scale with power for different years."""
    powers_gw = np.logspace(1, 3, 20)  # 10 GW to 1000 GW
    powers_w = powers_gw * 1e9
    
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    for year in years:
        h100e_counts = []
        capex_values = []
        electricity_fractions = []
        gdp_fractions = []
        
        for power in powers_w:
            compute = watts_to_h100e(power, year)
            capex = calculate_capex(power, year)
            infrastructure = calculate_infrastructure(power, {'gas': 1.0})
            fractions = calculate_global_fractions(power, capex['total_capex'], infrastructure)
            
            h100e_counts.append(compute['h100e_count'])
            capex_values.append(capex['total_capex'] / 1e12)  # Convert to trillions
            electricity_fractions.append(fractions['electricity_fraction'] * 100)
            gdp_fractions.append(fractions['gdp_fraction'] * 100)
        
        # H100e count
        axes[0, 0].loglog(powers_gw, h100e_counts, label=str(year), linewidth=2)
        axes[0, 0].set_xlabel('Power (GW)')
        axes[0, 0].set_ylabel('H100 Equivalents')
        axes[0, 0].set_title('Compute Capacity vs Power')
        axes[0, 0].legend()
        axes[0, 0].grid(True, alpha=0.3)
        
        # CapEx
        axes[0, 1].loglog(powers_gw, capex_values, label=str(year), linewidth=2)
        axes[0, 1].set_xlabel('Power (GW)')
        axes[0, 1].set_ylabel('CapEx (Trillion USD)')
        axes[0, 1].set_title('Capital Expenditure vs Power')
        axes[0, 1].legend()
        axes[0, 1].grid(True, alpha=0.3)
        
        # Electricity fraction
        axes[1, 0].semilogx(powers_gw, electricity_fractions, label=str(year), linewidth=2)
        axes[1, 0].set_xlabel('Power (GW)')
        axes[1, 0].set_ylabel('% of World Electricity')
        axes[1, 0].set_title('Fraction of Global Electricity')
        axes[1, 0].axhline(y=100, color='r', linestyle='--', alpha=0.5)
        axes[1, 0].legend()
        axes[1, 0].grid(True, alpha=0.3)
        
        # GDP fraction
        axes[1, 1].semilogx(powers_gw, gdp_fractions, label=str(year), linewidth=2)
        axes[1, 1].set_xlabel('Power (GW)')
        axes[1, 1].set_ylabel('% of World GDP')
        axes[1, 1].set_title('CapEx as Fraction of Global GDP')
        axes[1, 1].legend()
        axes[1, 1].grid(True, alpha=0.3)
    
    plt.suptitle('AI Scaling with Power Consumption', fontsize=14, fontweight='bold')
    plt.tight_layout()
    return fig


# =============================================================================
# MAIN EXAMPLE
# =============================================================================

if __name__ == "__main__":
    print("AI Energy and Compute Forecast Model")
    print("="*60)
    
    # Example 1: Run a specific scenario
    scenario_2030 = run_scenario(
        watts=100e9,  # 100 GW
        year=2030,
        energy_mix={'solar': 0.3, 'gas': 0.7}
    )
    print(scenario_2030.summary())
    
    # Example 2: Compare different power levels in 2035
    print("\n" + "="*60)
    print("COMPARISON: Different Power Levels in 2035")
    print("="*60)
    
    for gw in [50, 200, 1000]:
        scenario = run_scenario(
            watts=gw * 1e9,
            year=2035,
            energy_mix={'solar': 0.5, 'gas': 0.5}
        )
        print(f"\n{gw} GW: {scenario.compute['h100e_count']:.2e} H100e, "
              f"${scenario.capex['total_capex']:.2e} CapEx, "
              f"{scenario.global_fractions['electricity_fraction']*100:.1f}% of world electricity")
    
    # Generate plots
    print("\n" + "="*60)
    print("Generating visualizations...")
    
    fig1 = plot_efficiency_curves()
    fig1.savefig('efficiency_curves.png', dpi=150, bbox_inches='tight')
    
    fig2 = plot_power_scaling()
    fig2.savefig('power_scaling.png', dpi=150, bbox_inches='tight')
    
    print("Saved: efficiency_curves.png, power_scaling.png")
    print("\nModel initialization complete!")
