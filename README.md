# AI Energy and Compute Forecast Model

## Project Motivation & Context

### The Problem We're Solving

We started with a fundamental observation: **Energy is becoming the substrate of AI progress**. Everyone in the industry is obsessed with power availability, transformer procurement, and datacenter construction. Yet most AI discourse focuses on model capabilities rather than the physical infrastructure that will determine deployment scale.

Our original approach (in the CSV file) tried to model AI hardware growth directly - predicting how fast AI gets better, how that drives revenue, how that drives CapEx, etc. But we realized this has too many unknown unknowns. **Hardware growth is an exogenous variable with massive uncertainty**.

### Our Key Insight

**Instead of predicting compute growth, we use power (watts) as the independent variable**. This flips the question from:
- ❌ "When will AI need X amount of compute?" (impossible to predict)
- ✅ "If AI needs X watts of power, what are the implications?" (we can calculate)

This makes us **agnostic about the timeline** while focusing on the physical and economic implications at different scales. We can then graph these relationships with year as a parameter (since efficiency improvements are year-dependent).

### Why This Matters

As Dwarkesh notes: "As AI actually becomes capable of substituting for human labor, your country's GDP will be denominated by your AI population size, which is downstream of energy."

The goal is to understand:
1. **What breaks first?** - Will it be energy availability, manufacturing capacity, or economic constraints?
2. **What are the supply elasticities?** - Can we actually build enough transformers, turbines, PV modules?
3. **What does the world look like** if these projections materialize?

## The Core Questions We're Answering

1. **Energy Scaling**: At different power levels (10 GW to 10 TW), what fraction of world electricity would AI consume?
2. **Economic Scaling**: What CapEx is required and how does it compare to world GDP?
3. **Infrastructure Bottlenecks**: What physical equipment is needed and can the world produce it?
4. **Compute Translation**: How many H100-equivalents and tokens can be generated?
5. **Feasibility Analysis**: Which scenarios are plausible vs physically impossible?

## Implementation Philosophy

### Design Principles

1. **Simplicity First**: The code is intentionally simple - no complex frameworks, just clear functions
2. **Transparency**: Every calculation is explicit and documented
3. **Modularity**: Each component (efficiency curves, infrastructure, etc.) is independent
4. **Extensibility**: Easy to add new energy sources, update constants, or modify assumptions

### Model Architecture

```
Power (Watts) → [Year-Dependent Efficiency Curves] → Compute (H100e)
                                ↓
                        Infrastructure Needs
                                ↓
                    Global Resource Comparisons
                                ↓
                        Feasibility Analysis
```

## How We Built This

### Phase 1: Core Model (`energy_model.py`)

We started by implementing the fundamental relationships:

1. **Efficiency Curves**: Three key trends that improve over time
   - `moores_law(year)`: Compute density (H100e per die area)
   - `power_efficiency(year)`: Watts per H100e
   - `cost_efficiency(year)`: Dollars per H100e

2. **Conversion Functions**: 
   - `watts_to_h100e()`: Given power and year, how many H100-equivalents?
   - `calculate_capex()`: What's the total cost?
   - `calculate_infrastructure()`: What equipment is needed?

3. **Global Comparisons**:
   - What fraction of world electricity/GDP/production capacity?

### Phase 2: Analysis Framework (`analysis.py`)

Built comprehensive scenario analysis:
- Matrix of scenarios: 6 power levels × 4 years × 4 energy mixes = 96 scenarios
- Bottleneck identification
- Visualization of feasibility landscapes
- Comparison with original CSV projections

### Key Implementation Decisions

1. **Why Python?** Simple, readable, standard scientific stack (numpy, pandas, matplotlib)
2. **Why not a Jupyter notebook?** We want scriptable, version-controlled analysis
3. **Why these specific efficiency curves?** Based on historical trends with conservative decay
4. **Why only solar and gas?** Starting simple; nuclear/wind/etc can be added later

## Understanding the Outputs

### When you run a scenario, you get:

```python
============================================================
Scenario: 100.0 GW in 2030
Energy Mix: {'solar': 0.3, 'gas': 0.7}
============================================================

COMPUTE:
  H100 equivalents: 3.44e+08      # Number of H100-equivalent chips
  Total FLOPS: 3.86e+24            # Computational capacity
  Watts per H100e: 291.1           # Power efficiency

CAPEX:
  Total CapEx: $4.33e+12           # Total investment needed
  Compute CapEx: $2.40e+12         # Just for chips
  CapEx per Watt: $43.33           # Capital efficiency

INFRASTRUCTURE:
  Transformers needed: 50000       # Grid equipment
  PV modules needed: 4.80e+08      # Solar panels
  Gas turbines needed: 70000       # Power generation

GLOBAL RESOURCE USAGE:
  % of world electricity: 2.5%     # Sustainability check
  % of world GDP: 3.90%            # Economic feasibility

POTENTIAL BOTTLENECKS:
  ⚠️  Transformers (500% of global production)  # Red flags!
```

## Current Limitations & Known Issues

### What's Missing
1. **Depreciation**: Chips die over time (5-10 year lifespan) - not modeled yet
2. **Geographic constraints**: Treats the world as one pool of resources
3. **Learning curves**: Doesn't model how scale might accelerate cost reductions
4. **Grid dynamics**: Assumes perfect power delivery, ignores transmission losses
5. **Nuclear option**: Only models solar/gas, not nuclear which might be crucial

### Placeholder Values
Many infrastructure constants are estimates:
- Transformers per MW: 0.5 (needs validation)
- PV modules per MW: 4000 (rough estimate)
- Global production capacities (order of magnitude estimates)

## How to Extend This Model

### For Future LLMs Working on This:

1. **To add a new energy source** (e.g., nuclear):
   - Add constants to `energy_model.py` (e.g., `REACTORS_PER_GW`)
   - Extend `calculate_infrastructure()` to handle the new source
   - Update `energy_mix` dictionaries in analysis

2. **To improve efficiency curves**:
   - Modify the interpolation in `moores_law()`, `power_efficiency()`, `cost_efficiency()`
   - Consider adding new curves (e.g., `interconnect_efficiency()`)

3. **To add geographic modeling**:
   - Create regional variants of global constants
   - Add location parameter to `run_scenario()`
   - Model transmission losses and constraints

4. **To add depreciation**:
   - Track chip age distribution
   - Model replacement cycles
   - Adjust net compute availability

### For Human Collaborators:

The model is structured so you can:
1. **Run scenarios**: Just call `run_scenario()` with your parameters
2. **Update constants**: Edit the constants at the top of `energy_model.py`
3. **Add visualizations**: Use the scenario data structure for new plots
4. **Validate assumptions**: Compare outputs to real-world data

## The Blog Post Vision

This model supports a blog post (collaboration between Dwarkesh and Romeo) that will:

1. **Show the incompatibility** between AI growth projections and business-as-usual economy
2. **Identify specific bottlenecks** (transformers, turbines, etc.)
3. **Explore solutions** (behind-the-meter generation, overbuilding solar, etc.)
4. **Compare US vs China** capabilities and constraints
5. **Project the "energy singularity"** where AI civilization's output is measured in watts not GDP

### Key Narratives to Explore

- "By 2036, AI could use more electricity than the entire world produces today"
- "The datacenter of geniuses problem: How do we measure value when AI deflates prices?"
- "Why your country's future GDP equals its AI population × energy availability"
- "The 10TW gap: Can we close it with solar, gas, or do we need fusion?"

## Questions for Further Investigation

1. **Manufacturing**: Can we ramp turbine/transformer production 100x?
2. **China advantage**: Does State Grid's expansion give them an edge?
3. **Financing**: After big tech FCF runs out, where does funding come from?
4. **Lead times**: How do permitting and construction timelines change the picture?
5. **Inference vs Training**: How does the workload mix affect power needs?

## Repository Structure

```
ai-predictions/
├── energy_model.py          # Core model with efficiency curves
├── analysis.py              # Scenario analysis and visualizations
├── README.md               # This file
├── Energy forecast Romeo and Dwarkesh - clean (2).csv  # Original data
├── scenario_analysis.csv   # Generated scenario results
├── efficiency_curves.png   # Visualization of improvement trends
├── feasibility_landscape.png # Heatmap of feasible scenarios
├── power_scaling.png       # How metrics scale with power
└── cost_curves.png         # Economic trends over time
```

## Authors

- **Dwarkesh Patel**: Vision, requirements, blog post lead
- **Romeo Dean**: Energy modeling expertise, compute forecasting

## Quick Start

```bash
# Install dependencies
pip3 install numpy pandas matplotlib scipy

# Run basic model
python3 energy_model.py

# Run comprehensive analysis
python3 analysis.py
```

## Model Structure

### Core Components

1. **Energy Model (`energy_model.py`)**: The foundational model with:
   - Efficiency curves (Moore's Law, power efficiency, cost efficiency)
   - Power-to-compute conversion
   - Infrastructure calculations
   - Global resource comparisons

2. **Analysis Suite (`analysis.py`)**: Comprehensive scenario analysis:
   - Multiple power levels (10 GW to 2 TW)
   - Multiple years (2025-2040)
   - Different energy mixes (solar, gas, hybrid)
   - Bottleneck identification

## Key Assumptions

### Efficiency Improvements (Year-over-Year)

#### Moore's Law (Compute Density)
- **2025**: 1.35x improvement/year
- **2040**: 1.25x improvement/year
- Gradual decay interpolated between these years
- Represents H100 equivalents per H100-sized die

#### Power Efficiency
- **2025**: 1000W per H100 equivalent, improving at 1.3x/year
- **2040**: Improvement rate decays to 1.2x/year
- Accounts for the death of Dennard Scaling

#### Cost Efficiency
- **2025**: $24,000 per H100 equivalent, improving at 1.3x/year
- **2040**: Improvement rate decays to 1.2x/year
- Includes both chip costs and manufacturing improvements

### Infrastructure Requirements

Per MW of datacenter capacity:
- **Transformers**: 0.5 HV transformers
- **Switchgear**: 2.0 units
- **Solar**: 4,000 PV modules + 4 MWh batteries (accounting for 25% capacity factor)
- **Natural Gas**: 1.0 turbine

### Global Baselines (2024)

- **World Electricity**: 35.2 PWh/year
- **World GDP**: $111 trillion
- **World Final Energy**: 180 PWh/year

## Model Outputs

For each scenario (power level, year, energy mix), the model calculates:

### Compute Metrics
- H100 equivalent count
- Total FLOPS capacity
- Watts per H100e

### Economic Metrics
- Total CapEx (compute + non-compute)
- CapEx per watt
- Cost per H100e
- Percentage of world GDP

### Infrastructure Requirements
- Grid equipment (transformers, switchgear)
- Solar infrastructure (PV modules, batteries)
- Gas infrastructure (turbines)
- Comparison to global production capacity

### Token Generation
- Tokens per second capacity
- Annual token output
- Effective utilization estimates

### Global Impact
- Percentage of world electricity consumption
- Percentage of world GDP for CapEx
- Infrastructure bottleneck identification

## Key Insights from Initial Analysis

### 1. Electricity Constraints
The model shows that even modest AI growth quickly hits electricity limits:
- 100 GW ≈ 2.5% of current world electricity (feasible)
- 1 TW ≈ 25% of current world electricity (challenging)
- 2 TW ≈ 50% of current world electricity (requires massive grid expansion)

### 2. Economic Scale
By 2030, AI infrastructure CapEx could represent:
- 100 GW: $4.3T (3.9% of world GDP)
- 500 GW: $21.7T (19.5% of world GDP)
- 1 TW: $43.3T (39.0% of world GDP)

### 3. Efficiency Gains (2025 → 2040)
- Moore's Law: 66x improvement in compute density
- Power Efficiency: 27x improvement
- Cost Efficiency: 27x improvement

### 4. Infrastructure Bottlenecks
Major bottlenecks identified:
- **Transformers**: Current global production severely constrains deployment
- **Turbines**: Natural gas scenarios quickly exceed global turbine production
- **PV Modules**: Solar scenarios require significant fraction of global production

## Visualizations

The model generates several key visualizations:

1. **Efficiency Curves**: Shows improvement trajectories for Moore's Law, power, and cost
2. **Power Scaling**: How metrics scale with power consumption across different years
3. **Feasibility Landscape**: Heatmap of feasibility scores across power/year combinations
4. **Cost Curves**: Economic trends over time for different power levels

## Limitations and Caveats

1. **Placeholder Infrastructure Constants**: The infrastructure requirements (transformers, PV modules, etc.) are estimates and should be refined with industry data.

2. **Linear Scaling Assumptions**: The model assumes linear scaling of infrastructure with power, which may not hold at extreme scales.

3. **No Geographic Differentiation**: The model treats global resources as a pool, not accounting for regional constraints.

4. **Static Global Baselines**: World electricity and GDP are held constant at 2024 levels for comparison.

5. **Simplified Energy Mix**: Only models solar and natural gas, not nuclear, wind, or other sources.

6. **No Learning Curves**: Doesn't model how massive scale might drive down costs faster than baseline assumptions.

## Future Enhancements

Planned improvements include:

1. **Supply Chain Modeling**: Detailed modeling of manufacturing capacity and ramp rates
2. **Geographic Analysis**: Regional constraints and opportunities
3. **Nuclear Power**: Adding nuclear as an energy source option
4. **Dynamic Baselines**: Projecting world electricity and GDP growth
5. **Depreciation Modeling**: Accounting for hardware replacement cycles
6. **Training vs Inference**: Different power/compute profiles for different workloads
7. **Continual Learning**: Modeling the impact of online learning on compute requirements

## Data Sources

- H100 specifications from NVIDIA public documentation
- World electricity data from IEA
- GDP data from World Bank
- Solar capacity factors from NREL
- Original projections from "Energy forecast Romeo and Dwarkesh - clean (2).csv"

## Usage Examples

### Basic Scenario
```python
from energy_model import run_scenario

# Run a 100 GW datacenter in 2030 with 70% gas, 30% solar
scenario = run_scenario(
    watts=100e9,  # 100 GW
    year=2030,
    energy_mix={'solar': 0.3, 'gas': 0.7}
)

print(scenario.summary())
```

### Comparing Years
```python
for year in [2025, 2030, 2035, 2040]:
    scenario = run_scenario(watts=500e9, year=year, energy_mix={'solar': 0.5, 'gas': 0.5})
    print(f"{year}: {scenario.compute['h100e_count']:.2e} H100e, ${scenario.capex['total_capex']:.2e}")
```

### Finding Bottlenecks
```python
scenario = run_scenario(watts=1e12, year=2035, energy_mix={'solar': 1.0, 'gas': 0.0})
fractions = scenario.global_fractions

if fractions['pv_fraction'] > 0.5:
    print(f"⚠️ Requires {fractions['pv_fraction']*100:.0f}% of global PV production!")
```

## Contributing

To contribute to this model:

1. Improve infrastructure constants with real-world data
2. Add new energy sources (nuclear, wind, hydro)
3. Enhance geographic modeling
4. Add supply chain dynamics
5. Improve depreciation and replacement modeling

## License

This model is provided for research and educational purposes. Please cite the authors when using this work.

## Contact

For questions and collaboration:
- Dwarkesh Patel: [contact info]
- Romeo Dean: [contact info]

## Acknowledgments

Thanks to Duncan [last name] for infrastructure insights and Carl Shulman for feedback on the economic modeling approach.

# ai-predictions
