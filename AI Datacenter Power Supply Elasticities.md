

# **An Assessment of Supply Chain Elasticity for Projected AI-Driven Datacenter Expansion**

### **Executive Summary**

This report provides a comprehensive analysis of the industrial and resource viability of a forecast projecting a 70-fold increase in AI-driven datacenter power consumption, from approximately 28 gigawatts (GW) in 2025 to nearly 2,000 GW, or 2 terawatts (TW), by 2040\. The central finding of this analysis is that the forecasted trajectory is not physically viable within the specified timeframe. The projected growth represents a demand shock of unprecedented scale and speed, for which the global energy, manufacturing, and raw material supply chains are fundamentally unprepared.

The primary constraints identified are seavere, structural, and systemic. The most acute and immediate bottleneck is the global supply of **High-Voltage (HV) power transformers**. Current manufacturing lead times have extended to between two and five years, a dramatic increase from mere weeks just a few years ago. This creates a temporal paradox where the forecast's exponential growth outpaces the supply chain's linear and delayed response, rendering equipment obsolete before it can be delivered and installed.

Beyond this critical component, the analysis reveals a cascade of further, formidable constraints:

* **Electrical Switchgear:** While less acute than transformers, the demand for medium-voltage switchgear would consume a disruptive share of global production by the early 2030s.  
* **Power Generation:** Scenario analyses reveal insurmountable obstacles. A 100% solar and battery storage solution would require an annual deployment of solar panels and batteries that eclipses total current global production for all other sectors combined, creating a direct resource conflict with the global transition to electric vehicles. A 100% natural gas solution would consume approximately two-thirds of the world's current annual gas production, causing a catastrophic shock to global energy markets and security.  
* **Foundational Resources:** The forecast faces intractable limits on foundational inputs, including a critical and worsening shortage of skilled labor for construction and operation, unsustainable demands on regional water supplies, and the multi-decade timelines required for building the necessary high-voltage transmission infrastructure.

The scale of the challenge is immense. The projected 2 TW of demand is equivalent to nearly double the entire current electricity generation capacity of the United States. Fulfilling this demand would necessitate a sustained, 15-year industrial mobilization that would dwarf historical precedents.

Consequently, the forecast should not be interpreted as a business-as-usual projection but rather as an unconstrained demand signal. The actual rate of growth for AI-driven power consumption will be dictated not by technological ambition but by the profound inelasticity of these physical-world supply chains. This reality presents both immense investment opportunities in the industrial and resource sectors that form these bottlenecks, and profound systemic risks for projects and policies that fail to account for them.

### **Section 1: The Scale of the Demand Shock: Deconstructing the AI Power Forecast**

The foundation of this analysis is a forecast for AI-specific datacenter power consumption that projects a growth trajectory of historic proportions.1 The provided data indicates a surge from 27.9 GW in 2025 to 1,993 GW by 2040, a 70-fold increase over a 15-year period.1 This corresponds to a Compound Annual Growth Rate (CAGR) of 32.9%. The growth is particularly aggressive in the initial years, with the model projecting a 74% increase from 2025 to 2026 alone, and demand more than doubling every two years through 2029\.1

To fully grasp the magnitude of this projection, it is essential to place these figures in the context of the global energy landscape. The 2040 demand figure of nearly 2 TW is a quantity of power that would fundamentally reshape global energy flows. For perspective:

* The total installed electricity generation capacity of the United States, the world's largest economy, is approximately 1.2 TW. The forecast implies building the equivalent of nearly two entire U.S. grids dedicated solely to AI in 15 years.  
* The annual increase in power demand projected in the later years of the forecast is itself staggering. The increase from 2039 to 2040 alone is approximately 255 GW—a quantity larger than the entire installed generation capacity of France or the United Kingdom.

This forecast reflects the exponential scaling dynamics often seen in digital technology adoption, where computational power and model complexity can grow at a pace dictated by semiconductor advancements and software innovation. However, a critical disconnect arises when this digital-first mindset is applied to the physical world of energy and industrial infrastructure. The development of power plants, the manufacturing of heavy electrical equipment, and the construction of transmission networks are processes that scale linearly, constrained by long lead times, massive capital investment, complex permitting, and finite physical resources. The fundamental tension between the exponential demand signal from the digital realm and the linear, slow-moving response capacity of the physical world is the central conflict that this report will explore. The forecast represents an *unconstrained* demand scenario; the subsequent sections will analyze the *constrained* reality imposed by the supply chains required to meet it.

### **Section 2: Constraint Analysis I: The Grid Connection Bottleneck \- Transformers**

The ability to connect vast new datacenters to the electrical grid, or to step down power within an on-site generation facility, depends entirely on the availability of large power transformers. This analysis indicates that the supply of High-Voltage (HV) and Medium-Voltage (MV) transformers represents the single greatest, most immediate, and most severe bottleneck to achieving the forecasted power consumption growth.

#### **2.1 Estimating Transformer Demand**

Datacenter electrical systems are designed with significant redundancy and capacity for future growth, meaning the apparent power rating of the required transformers, measured in Mega or Giga Volt-Amperes (MVA/GVA), is substantially higher than the real power load, measured in Megawatts (MW) or Gigawatts (GW). This oversizing accounts for factors like power factor correction, harmonic loads, and N+1 or 2N redundancy architectures that ensure uptime.2 The user's provided materials suggest a planning ratio of 2.5 MVA of transformer capacity for every 1 MW of datacenter load.1 This is a reasonable, and potentially conservative, industry metric for hyperscale developments.4

Applying this 2.5x ratio to the AI power forecast reveals a colossal demand for transformer capacity. The 28 GW of power draw in 2025 translates to a need for 70 GVA of new transformers. By 2030, this requirement escalates to 676 GVA. By 2040, the cumulative demand reaches an astronomical 4,982 GVA.1

#### **2.2 Global Production Capacity vs. Projected Need**

To assess the feasibility of meeting this demand, it is necessary to quantify the world's total manufacturing capacity for large power transformers. As precise unit production data is not readily available, capacity can be estimated by dividing the global market size in monetary terms by an average cost per unit of capacity.

The global market for high-voltage power transformers was valued at approximately USD 22.6 billion in 2024 and is projected to grow at a CAGR of 6.6%.6 Other market analyses offer slightly different figures but confirm a similar growth trajectory in the mid-single digits.7 The cost of these transformers varies significantly with size and voltage, but a blended average for the large units required by datacenters falls in the range of $8,000 to $15,000 per MVA.8 Using a central estimate of

**$10,000 per MVA (or $10 million per GVA)**, the total global production capacity for 2025 can be estimated.

* **Estimated 2025 Global Production:** ($22.6B \* 1.066 CAGR) / $10M per GVA ≈ **2,410 GVA**

The following table compares the escalating transformer demand from the AI forecast against this projected global supply.

| Year | AI Power Draw (GW) | Required Transformer Capacity (GVA) | Est. Annual Global Production (GVA) | Annual AI Share of Global Production |
| :---- | :---- | :---- | :---- | :---- |
| 2025 | 28 | 70 | 2,410 | 2.9% |
| 2026 | 49 | 122 | 2,570 | 4.7% |
| 2027 | 83 | 209 | 2,739 | 7.6% |
| 2028 | 134 | 334 | 2,920 | 11.4% |
| 2029 | 196 | 489 | 3,113 | 15.7% |
| 2030 | 270 | 676 | 3,319 | 20.4% |
| 2031 | 360 | 900 | 3,538 | 25.4% |
| 2032 | 466 | 1,164 | 3,771 | 30.9% |
| 2033 | 589 | 1,473 | 4,019 | 36.6% |
| 2034 | 732 | 1,830 | 4,285 | 42.7% |
| 2035 | 895 | 2,238 | 4,567 | 49.0% |
| 2036 | 1,078 | 2,695 | 4,869 | 55.3% |
| 2037 | 1,279 | 3,197 | 5,191 | 61.6% |
| 2038 | 1,500 | 3,750 | 5,533 | 67.8% |
| 2039 | 1,738 | 4,345 | 5,898 | 73.7% |
| 2040 | 1,993 | 4,982 | 6,288 | 79.2% |

Calculations based on data from 1 and derived cost-per-GVA estimates.

The analysis is stark. While the initial demand in 2025 appears manageable at under 3% of global capacity, the exponential growth curve rapidly collides with the linear growth of manufacturing. By 2030, AI datacenters alone would need to consume over 20% of the world's entire production of large power transformers. By 2036, this single application would require more than half of all transformers produced globally, and by 2040, it would demand nearly 80%. This scenario implies the starvation of all other critical sectors—utility grid replacements and expansion, industrial development, and renewable energy projects—creating an untenable competition for a finite industrial output.

#### **2.3 The Lead Time Crisis and Its Implications**

The most critical factor compounding the supply-demand imbalance is the extreme and growing lead time for transformer delivery. In the pre-2020 period, a utility could procure a large transformer in 12 to 14 weeks.11 Today, that same process is fraught with delays. Multiple industry sources and news reports confirm that lead times for distribution transformers are now one year, while large, high-voltage power transformers require

**three to five years** from order to delivery.11

This is not a simple backlog; it is a structural failure of the supply chain to meet demand, and it creates a fatal scheduling paradox for the user's forecast. The rate of growth required by the model is so rapid that it outpaces the delivery timeline for its most critical component. For example, a planner in 2026, anticipating the need for 83 GW of power in 2027, would need to order the corresponding 209 GVA of transformers. With a three-year lead time, that equipment would not arrive until 2029\. By that time, however, the forecast demands 196 GW of power—more than double what the just-arriving equipment can support.1 The project would be obsolete before it is even energized. This temporal mismatch makes planning for exponential growth impossible. The linear, multi-year reality of industrial procurement cannot service an exponential demand curve that doubles every 18-24 months.

Furthermore, manufacturers are historically wary of such demand spikes, having been burned by previous boom-and-bust cycles, such as the housing market of the 2000s.11 This makes them hesitant to commit the massive capital required for new factories—investments that could take a decade to pay off—to chase a demand signal that could cool, leaving them with expensive, underutilized capacity.13

#### **2.4 Raw Material Headwinds**

The root cause of the manufacturing capacity limits and extended lead times lies further upstream in the supply chain for raw materials. Transformer manufacturing is dependent on two key specialized materials:

1. **Grain-Oriented Electrical Steel (GOES):** This specialized steel is required for the transformer core to minimize energy losses. The U.S. market is almost entirely dependent on a single domestic supplier, creating a severe bottleneck and forcing many manufacturers to source GOES or semi-finished cores from abroad.14  
2. **Copper and Aluminum Windings:** The windings that carry the current are made of high-conductivity copper or aluminum. The process of creating these windings is highly technical, and copper in particular has been identified as a potential production bottleneck, exacerbated by trade policies such as tariffs.14

These upstream material constraints are far less elastic than factory floor space. Expanding GOES production or copper winding capacity involves building new, capital-intensive processing facilities with their own multi-year construction timelines. Therefore, a significant expansion of transformer output cannot be achieved simply by adding assembly lines; it requires a coordinated, decade-long investment strategy across the entire heavy industrial supply chain, from mining and refining to specialized steel production.

### **Section 3: Constraint Analysis II: The Distribution Backbone \- Electrical Switchgear**

While transformers handle the bulk conversion of voltage, electrical switchgear is the critical infrastructure responsible for protection, control, and isolation of electrical circuits. It forms the backbone of power distribution within any large facility. A typical large-scale datacenter employs a hierarchical system: utility power enters through high-voltage (HV) switchgear, is stepped down by transformers, and then distributed via medium-voltage (MV) switchgear to numerous low-voltage (LV) switchboards that ultimately feed the IT equipment.16 An analysis of the MV switchgear market reveals another significant, though less acute, industrial constraint.

#### **3.1 Quantifying Switchgear Requirements**

Unlike transformers, a simple power-to-equipment ratio for switchgear is less direct. The number of switchgear units (panels, cubicles, or circuit breakers) depends on the specific electrical design, redundancy level, and the granularity of power distribution. However, a reasonable heuristic can be developed from typical hyperscale datacenter architectures. A 100 MW datacenter is often designed with a central substation that distributes power at a medium voltage (e.g., 13.8 kV to 34.5 kV) to multiple smaller "load centers" or data halls, each handling approximately 3 MW of IT load.2 Each of these load centers requires its own MV switchgear for protection and control.

This architecture implies a need for approximately 33 MV switchgear sections (one for each 3 MW load center) per 100 MW of datacenter capacity. This yields a planning metric of **0.33 MV switchgear units per MW of IT load**. Applying this metric to the AI power forecast allows for an estimation of the total number of MV switchgear units required. For the 2025 demand of 28 GW, this translates to over 9,200 units. By 2040, the 2 TW forecast would require a staggering 658,000 MV switchgear units to be installed in that year alone.

#### **3.2 Assessing Global Manufacturing Capabilities**

The global market for medium-voltage switchgear is substantially larger than that for HV transformers, reflecting its wider use across all industrial, commercial, and utility sectors. The market was valued at approximately USD 52.8 billion in 2024, with a projected CAGR of 6.8%.18 Numerous other market reports corroborate this scale and growth rate.19

The cost per unit of MV switchgear varies widely depending on its voltage, current rating, insulation type (air vs. gas), and inclusion of advanced controls, ranging from under $5,000 to over $50,000 per panel.22 A blended average cost for the type of robust, high-spec equipment used in mission-critical datacenter applications is estimated at

**$40,000 per unit**. This allows for a calculation of the total global production volume.

* **Estimated 2025 Global Production:** ($52.8B \* 1.068 CAGR) / $40,000 per unit ≈ **1.41 million units**

The table below compares the projected demand for MV switchgear from the AI forecast against the total estimated global supply.

| Year | AI Power Draw (GW) | Required MV Switchgear Units | Est. Annual Global Production (Units) | Annual AI Share of Global Production |
| :---- | :---- | :---- | :---- | :---- |
| 2025 | 28 | 9,228 | 1,410,240 | 0.7% |
| 2026 | 49 | 16,097 | 1,506,136 | 1.1% |
| 2027 | 83 | 27,542 | 1,608,554 | 1.7% |
| 2028 | 134 | 44,121 | 1,717,935 | 2.6% |
| 2029 | 196 | 64,534 | 1,834,754 | 3.5% |
| 2030 | 270 | 89,254 | 1,959,517 | 4.6% |
| 2031 | 360 | 118,771 | 2,092,764 | 5.7% |
| 2032 | 466 | 153,668 | 2,234,972 | 6.9% |
| 2033 | 589 | 194,382 | 2,386,950 | 8.1% |
| 2034 | 732 | 241,594 | 2,549,263 | 9.5% |
| 2035 | 895 | 295,383 | 2,722,613 | 10.8% |
| 2036 | 1,078 | 355,689 | 2,907,749 | 12.2% |
| 2037 | 1,279 | 421,993 | 3,105,476 | 13.6% |
| 2038 | 1,500 | 494,927 | 3,316,648 | 14.9% |
| 2039 | 1,738 | 573,568 | 3,542,160 | 16.2% |
| 2040 | 1,993 | 657,665 | 3,783,027 | 17.4% |

Calculations based on data from 1 and derived cost-per-unit estimates.

The analysis shows that the switchgear supply chain is more robust than that for transformers. In the near term, the demand from AI datacenters represents a small fraction of global output. However, the relentless exponential growth means that by the mid-2030s, this single industry would be consuming over 10% of global production, rising to over 17% by 2040\. While not an immediate impossibility like transformers, this level of demand would still place significant strain on the market, likely leading to price increases and extended lead times for all other industrial and utility customers. Reports of lead times for some electrical components already extending to 75-80 weeks indicate that this supply chain is also not immune to stress.24

### **Section 4: Scenario Analysis: Powering the AI Revolution**

To understand the full scope of the infrastructure challenge, this section analyzes the physical requirements of two distinct, self-contained power generation scenarios as requested by the user: one based entirely on renewable energy and another on fossil fuels.

#### **4.1 Scenario A: 100% Off-Grid Solar & Storage**

This scenario envisions each datacenter being powered by a dedicated, off-grid solar photovoltaic (PV) array coupled with a Battery Energy Storage System (BESS) to provide continuous, 24/7 power.

##### **4.1.1 Solar PV Requirements**

Solar panels only generate power when the sun is shining. The ratio of the actual energy produced over a year to the maximum possible output is known as the capacity factor. For utility-scale solar projects in the United States, this factor averages around 25% annually.25 Even in the most ideal, sun-drenched locations, the capacity factor rarely exceeds 34%.27 To provide constant, reliable power around the clock, a solar farm must be significantly overbuilt to generate and store enough excess energy during daylight hours to cover the night and periods of inclement weather. A conservative planning assumption for a mission-critical, off-grid system requires a nameplate capacity that is five times the constant load, corresponding to an effective 24/7 capacity factor of 20%.

* **Calculation:** For every 1 GW of constant datacenter power, **5 GW of solar PV nameplate capacity** is required.

In 2024, the world installed a record-breaking 600 GW of new solar capacity.28 While impressive, this entire global effort would be dwarfed by the demands of the AI forecast. By 2028, the annual

*increase* in AI power demand (51 GW) would require 255 GW of new solar panels, consuming nearly half of the current global supply. By the early 2030s, the solar capacity required annually for new AI datacenters alone would exceed the entire record-breaking global installation volume of 2024\.

##### **4.1.2 Battery Storage (BESS) Requirements**

The cornerstone of an off-grid solar strategy is energy storage. The BESS must be large enough to power the entire datacenter facility through the longest expected period without solar generation. A standard requirement for grid reliability is several hours of storage; for a fully off-grid, mission-critical facility, a minimum of **16 hours of storage** at full load is a reasonable assumption to cover overnight operation and some contingency.

* **Calculation:** For every 1 GW of datacenter power, **16 GWh of battery storage** is required.

Global battery manufacturing capacity, driven by the electric vehicle boom, reached 3 TWh (3,000 GWh) in 2024 and is expanding rapidly.30 However, the scale of demand in this scenario is simply overwhelming. To power the full 2 TW forecast by 2040 would require a one-time installation of 32,000 GWh (32 TWh) of batteries. This single application would demand a quantity of batteries equivalent to more than ten times the entire current annual global production for all sectors combined.

The table below summarizes the immense scale of the solar and battery requirements relative to global production.

| Year | Required Solar PV (GW) | Required BESS (GWh) |
| :---- | :---- | :---- |
| 2025 | 140 | 447 |
| 2026 | 244 | 782 |
| 2027 | 417 | 1,335 |
| 2028 | 668 | 2,140 |
| 2029 | 978 | 3,129 |
| 2030 | 1,352 | 4,327 |
| 2035 | 4,476 | 14,322 |
| 2040 | 9,965 | 31,887 |

Calculations based on data from 1 and derived requirements.

##### **4.1.3 Raw Material Deep Dive: A Competing Revolution**

The viability of this scenario ultimately collapses at the level of raw material extraction. Lithium-ion batteries are complex devices requiring specific critical minerals, primarily lithium, nickel, cobalt, and graphite.31 Global supply chains for these minerals are already under strain from the accelerating transition to electric vehicles (EVs).33

The International Energy Agency projects that in a scenario aligned with climate goals, expected supply from existing mines and projects will meet only half of the required lithium and cobalt demand by 2030\.31 The market is facing potential deficits and tight supply for battery-grade nickel and lithium for the remainder of the decade.35

This creates a direct and irreconcilable conflict between two global technological revolutions: the electrification of transport and the rise of AI. Both are competing for the exact same, limited pool of battery raw materials and manufacturing capacity. The demand generated by the AI forecast under this 100% solar and storage scenario is so vast that it would completely derail the global EV transition. The 32 TWh of batteries required for the 2040 forecast would consume all available battery production for over a decade, absorbing every gram of lithium, cobalt, and nickel that could otherwise be used to build hundreds of millions of electric vehicles. This is not a matter of market competition; it is a physical impossibility without a multi-decade mining, refining, and manufacturing expansion of a scale never before witnessed.

#### **4.2 Scenario B: 100% On-Site Natural Gas Generation**

This scenario explores powering the datacenters with on-site natural gas combustion turbines, a common technology for large-scale, reliable power generation.

##### **4.2.1 Gas Turbine Demand vs. Production**

Industrial gas turbines are available in a wide range of sizes, from small units under 1 MW to massive utility-scale machines over 300 MW.36 For large, distributed industrial applications like datacenter campuses, a common and flexible size is in the 20-50 MW range. This analysis will use a representative

**40 MW simple-cycle gas turbine** as the standard unit of deployment.

* **Calculation:** To generate the forecasted 2 TW of power in 2040 would require the installation and operation of **50,000** such 40 MW turbines.

The global industrial gas turbine market is mature but grows at a modest pace. In 2023, a total of 453 units were sold globally, corresponding to 44.1 GW of capacity.38 The market is projected to grow at a CAGR of between 2.7% and 5.1% through 2033\.39 The demand from the AI forecast would require the global gas turbine manufacturing industry to scale its output by more than an order of magnitude. By the early 2030s, the annual demand for turbines for AI datacenters would exceed the entire current global production for all other utility and industrial customers.

##### **4.2.2 Fuel Consumption and Reserve Viability**

The most significant constraint in this scenario is the fuel itself. To calculate the natural gas consumption, an optimistic fleet-wide electrical efficiency of 50% is assumed. This is higher than typical simple-cycle turbines (around 40%) but achievable with advanced combined-cycle gas turbine (CCGT) plants, where waste heat is used to drive a secondary steam turbine.41

* **Calculation:** Generating 2 TW of electricity continuously for a year (8,760 hours) at 50% efficiency requires approximately 35,040 TWh of thermal energy from natural gas. This is equivalent to roughly **3.3 trillion cubic meters (Tcm)** of natural gas per year.

This level of consumption must be compared against global production and reserves.

* **Global Annual Production:** In 2024, total global natural gas production was approximately 4.2 Tcm.42  
* **Global Proven Reserves:** Total proven reserves of natural gas worldwide are estimated to be around 200 Tcm.44

The analysis reveals a staggering conclusion: powering the 2 TW AI forecast with natural gas would require **79% of the world's entire current natural gas production**. Such a massive new source of demand would cause a catastrophic shock to the global energy system. It would trigger unprecedented price spikes, create severe shortages for residential heating, industrial processes, and existing power generation worldwide, and have profound geopolitical consequences. Furthermore, this single application would be capable of depleting the world's entire proven natural gas reserves in approximately 60 years. This scenario is not only economically and geopolitically destabilizing but is fundamentally unsustainable from a resource perspective.

### **Section 5: Constraint Analysis III: Foundational and Overlooked Elasticities**

Beyond the specific equipment and generation technologies, the AI power forecast confronts a set of deeper, foundational constraints that are even less elastic and may ultimately prove to be the most difficult to overcome.

#### **5.1 The Human Element: Skilled Labor Shortage**

The construction and operation of energy and datacenter infrastructure is a human-intensive endeavor requiring highly specialized skills. The industry is already facing a severe and worsening labor shortage. Datacenter construction sites for current projects are reporting a "MASSIVE shortage" of skilled tradespeople, including electricians, pipefitters, and HVAC technicians, with single projects demanding over 2,000 workers concurrently.45 The shortage extends beyond construction to operations, with a critical lack of experienced senior technicians needed to run these complex facilities.45

This is not a future problem; it is an acute crisis today, before the forecast's exponential growth has even begun. The scale of construction implied by the 2 TW forecast—tens of thousands of new facilities and power plants—would require a workforce of millions of skilled tradespeople. These are not roles that can be created overnight; they require years of apprenticeship, training, and experience. In many developed nations, demographic trends show a declining, not growing, population of skilled trade workers. This human capital bottleneck may prove to be even more intractable than equipment manufacturing, as a skilled workforce cannot be scaled with the same speed as a factory production line.

#### **5.2 Physical Footprint: Land and Water**

Datacenters have a significant physical and environmental footprint. The land required for a single hyperscale campus can exceed 800 acres.46 More critically, they are intensely thirsty facilities. Water is the primary medium for cooling the servers that form the heart of a datacenter.

A single large datacenter can consume between **1 to 5 million gallons of water per day**—an amount equivalent to a small city.47 The industry metric for water efficiency, Water Usage Effectiveness (WUE), averages 1.8 liters of water per kilowatt-hour (L/kWh) of IT energy consumed.49

* **Calculation:** The 2 TW forecast, running continuously, would consume 17,520 TWh of electricity annually. At an average WUE of 1.8 L/kWh, this translates to a total water consumption of **31.5 trillion liters (approximately 8.3 trillion gallons) per year**.

This volume of water is immense, equivalent to more than double the total annual water consumption of the entire United Kingdom. This level of demand would place an unbearable and politically untenable strain on local and regional water resources, particularly as many ideal datacenter locations are in arid or semi-arid climates. The competition for water rights and the permitting challenges associated with such massive consumption would represent a hard physical and political limit to growth.

#### **5.3 The Final Mile: High-Voltage Transmission**

While the scenarios in Section 4 explored self-contained, off-grid power solutions, a more realistic future involves a mix of on-site generation and grid connectivity. This introduces the final, and perhaps most complex, bottleneck: the electrical grid itself. The infrastructure required to transmit terawatts of power from new, large-scale generation sources (such as vast solar farms in remote deserts) to datacenter clusters (often located near existing fiber optic and population centers) largely does not exist.

Building new high-voltage transmission lines is a notoriously slow and arduous process, fraught with challenges related to permitting, land acquisition, and environmental reviews. A single major transmission project can take **five to fifteen years** from conception to energization.50 While upgrading existing lines with advanced conductors—a process known as reconductoring—can add capacity more quickly (in 18-36 months), it is not a panacea and can only leverage existing rights-of-way.50 The sheer number of new lines and substations required to support a 2 TW load would represent the largest infrastructure build-out in a century, a process that would take many decades, not 15 years, to complete.

### **Section 6: Synthesis and Strategic Recommendations**

#### **6.1 Consolidated Bottleneck Analysis**

The analysis reveals a multi-layered system of constraints, each with a different timeline and severity. The viability of the forecast is not determined by a single factor but by the compounding effect of these interconnected bottlenecks. They can be ranked as follows:

* **Immediate (1-5 Year Horizon):**  
  1. **HV Power Transformers:** The most severe and immediate constraint. Multi-year lead times and a structural deficit in global manufacturing capacity make exponential growth physically impossible.  
  2. **Skilled Labor:** An existing, acute shortage of construction and operations talent that cannot be scaled rapidly.  
* Medium-Term (5-10 Year Horizon):  
  3\. Electrical Switchgear: A more elastic supply chain than transformers, but one that would come under significant strain, leading to price inflation and delays.  
  4\. Gas Turbine Production: A mature industry with limited ability to rapidly scale production by the required order of magnitude.  
  5\. Grid Transmission Capacity: The multi-decade timeline for planning and building new transmission lines will severely limit the ability to connect new large-scale generation to datacenter loads.  
  6\. Battery Raw Material Refining: Expanding the capacity to refine lithium, cobalt, and nickel into battery-grade materials is a capital-intensive, multi-year process that is already lagging behind EV demand.  
* Long-Term (10+ Year Horizon):  
  7\. Water Availability: A hard environmental and political limit that will render many potential datacenter sites non-viable.  
  8\. Battery Raw Material Mining: Opening new mines is a decade-plus process, making the supply of primary minerals highly inelastic.  
  9\. Natural Gas Reserves: While vast, the sheer consumption rate in the gas scenario makes it an unsustainable long-term solution.

#### **6.2 Final Verdict on the 2040 Forecast**

The cumulative weight of these constraints leads to an unequivocal conclusion: the forecast of reaching nearly 2 TW of AI-specific datacenter power draw by 2040 is not viable. The growth of this sector will be **supply-gated, not demand-driven**. The trajectory will be forcibly flattened from an exponential curve into a more linear, S-curve shape, with the rate of growth dictated by the slowest-moving bottleneck in the supply chain at any given time. In the near term, that bottleneck is unequivocally the supply of power transformers.

A more realistic projection for 2040, while still representing enormous growth, would likely be an order of magnitude lower than the 2 TW forecast. A global capacity in the range of 200-400 GW dedicated to AI workloads by 2040 would still constitute a monumental industrial challenge but falls closer to the realm of physical possibility.

#### **6.3 Strategic Considerations for Stakeholders**

The infeasibility of the forecast does not negate the underlying trend; it reframes it as a physical infrastructure challenge rather than a purely technological one. This has critical implications for all stakeholders.

* **For Datacenter Developers and Operators:** The traditional model of short-term, project-based procurement is no longer viable for critical power equipment. The strategic imperative must shift to extremely long-term planning (5-10 years) and deep, strategic partnerships with equipment manufacturers. This may include co-investment in new manufacturing facilities, vertical integration, or placing non-cancellable, multi-year orders to secure production slots. Site selection must prioritize locations with existing, robust power and water infrastructure above all other considerations.  
* **For Investors:** The analysis highlights that the most significant and potentially mispriced investment opportunities are not solely in AI software and semiconductor companies, but in the essential "picks and shovels" of the AI gold rush. This includes the publicly traded manufacturers of transformers, switchgear, and gas turbines; companies involved in the mining and refining of critical battery minerals; and engineering and construction firms specializing in energy infrastructure. The market valuation of these incumbent industrial firms may not yet fully reflect the magnitude of the coming demand signal.  
* **For Policymakers:** Enabling the economic benefits of the AI revolution is now fundamentally an industrial policy challenge. Governments must recognize that the transformer and electrical grid supply chain crisis represents a significant national economic and security risk. Policy priorities should include:  
  * **Permitting Reform:** Streamlining the permitting process for new manufacturing plants for critical components like transformers and GOES, as well as for new high-voltage transmission lines.  
  * **Strategic Industrial Investment:** Using industrial policy tools, such as grants, loan guarantees, and tax incentives, to de-risk and encourage domestic investment in expanding manufacturing capacity for the entire electrical equipment supply chain.  
  * **Workforce Development:** Launching a massive, coordinated effort to fund and expand skilled trades education, apprenticeship programs, and vocational training to address the critical labor shortage.  
  * **Standardization:** Working with industry to standardize equipment specifications, such as for distribution transformers, to enable mass production and reduce manufacturing complexity.51

#### **Works cited**

1. Energy forecast Romeo and Dwarkesh.xlsx  
2. Rethinking Data Center Power \- HDR, accessed September 6, 2025, [https://www.hdrinc.com/insights/rethinking-data-center-power](https://www.hdrinc.com/insights/rethinking-data-center-power)  
3. Data Center Power: A Comprehensive Overview of Energy \- Dgtl Infra, accessed September 6, 2025, [https://dgtlinfra.com/data-center-power/](https://dgtlinfra.com/data-center-power/)  
4. What is the relationship between installed generator & transformer capacity, accessed September 6, 2025, [https://help.leonardo-energy.org/hc/en-us/articles/202722652-What-is-the-relationship-between-installed-generator-transformer-capacity](https://help.leonardo-energy.org/hc/en-us/articles/202722652-What-is-the-relationship-between-installed-generator-transformer-capacity)  
5. Electrical Transformers for Data Centers: Technical Requirements. \- Grupo Edmar, accessed September 6, 2025, [https://www.grupoedmar.com/en/post/electrical-transformers-for-data-centers-technical-requirements](https://www.grupoedmar.com/en/post/electrical-transformers-for-data-centers-technical-requirements)  
6. High Voltage Power Transformer Market Size, Report 2025-2034, accessed September 6, 2025, [https://www.gminsights.com/industry-analysis/high-voltage-power-transformer-market](https://www.gminsights.com/industry-analysis/high-voltage-power-transformer-market)  
7. High Voltage Power Transformer Market Size, Share \[Latest\] \- MarketsandMarkets, accessed September 6, 2025, [https://www.marketsandmarkets.com/Market-Reports/high-voltage-power-transformer-market-54126096.html](https://www.marketsandmarkets.com/Market-Reports/high-voltage-power-transformer-market-54126096.html)  
8. How Much Does a Transformer Cost? Price Factors Explained, accessed September 6, 2025, [https://www.taishantransformer.com/how-much-does-a-transformer-cost/](https://www.taishantransformer.com/how-much-does-a-transformer-cost/)  
9. Power Transformer: Learn the Purpose, Cost, and Lead Time to Procure | PEguru, accessed September 6, 2025, [https://peguru.com/2019/08/power-transformer/](https://peguru.com/2019/08/power-transformer/)  
10. Substation Cost Estimator \- PEguru, accessed September 6, 2025, [https://peguru.com/substation-cost-estimator/](https://peguru.com/substation-cost-estimator/)  
11. Understanding the electric transformer shortage \- Latitude Media, accessed September 6, 2025, [https://www.latitudemedia.com/news/catalyst-understanding-the-electric-transformer-shortage/](https://www.latitudemedia.com/news/catalyst-understanding-the-electric-transformer-shortage/)  
12. Transformer supply bottleneck threatens power system stability as ..., accessed September 6, 2025, [https://www.utilitydive.com/news/electric-transformer-shortage-nrel-niac/738947/](https://www.utilitydive.com/news/electric-transformer-shortage-nrel-niac/738947/)  
13. Transformer, breaker backlogs persist, despite reshoring progress \- Utility Dive, accessed September 6, 2025, [https://www.utilitydive.com/news/reshore-electrical-equipment-backlogs-transformer-breaker-nema/749265/](https://www.utilitydive.com/news/reshore-electrical-equipment-backlogs-transformer-breaker-nema/749265/)  
14. Transformer troubles: manufacturing and policy constraints hit US ..., accessed September 6, 2025, [https://www.woodmac.com/news/opinion/transformer-troubles-manufacturing-and-policy-constraints-hit-us-transformer-supply/](https://www.woodmac.com/news/opinion/transformer-troubles-manufacturing-and-policy-constraints-hit-us-transformer-supply/)  
15. Aluminum vs. Copper in Distribution Transformers, accessed September 6, 2025, [https://www.maddox.com/resources/articles/aluminum-vs-copper-in-distribution-transformers](https://www.maddox.com/resources/articles/aluminum-vs-copper-in-distribution-transformers)  
16. What Is a Data Center Switchgear? \- Sunbird DCIM, accessed September 6, 2025, [https://www.sunbirddcim.com/glossary/data-center-switchgear](https://www.sunbirddcim.com/glossary/data-center-switchgear)  
17. Electrical Distribution Equipment in Data Center Environments, accessed September 6, 2025, [https://www.lorisweb.com/CMGT235/DIS21/VAVR-8W4MEX\_R1\_EN.pdf](https://www.lorisweb.com/CMGT235/DIS21/VAVR-8W4MEX_R1_EN.pdf)  
18. Medium Voltage Switchgear Market Size, 2025-2034 Report, accessed September 6, 2025, [https://www.gminsights.com/industry-analysis/medium-voltage-switchgear-market](https://www.gminsights.com/industry-analysis/medium-voltage-switchgear-market)  
19. Medium Voltage Switchgear Market: Global Industry Analysis And Forecast (2025-2032), accessed September 6, 2025, [https://www.maximizemarketresearch.com/market-report/global-medium-voltage-switchgear-market/23603/](https://www.maximizemarketresearch.com/market-report/global-medium-voltage-switchgear-market/23603/)  
20. Switchgear Market Size, Share and Industry Analysis \- 2030 | MarketsandMarkets, accessed September 6, 2025, [https://www.marketsandmarkets.com/Market-Reports/switchgear-market-1162268.html](https://www.marketsandmarkets.com/Market-Reports/switchgear-market-1162268.html)  
21. Switchgear Market Size, Industry Share Report 2034 \- Global Market Insights, accessed September 6, 2025, [https://www.gminsights.com/industry-analysis/switchgears-market](https://www.gminsights.com/industry-analysis/switchgears-market)  
22. Medium voltage switchgear \- Edwards Supply, accessed September 6, 2025, [https://www.edwardssupply.com/electrical-systems-and-lighting-and-components-and-accessories-and-supplies/electrical-equipment-and-components-and-supplies/distribution-and-control-centers-and-accessories/medium-voltage-switchgear/](https://www.edwardssupply.com/electrical-systems-and-lighting-and-components-and-accessories-and-supplies/electrical-equipment-and-components-and-supplies/distribution-and-control-centers-and-accessories/medium-voltage-switchgear/)  
23. Buy Cheap medium voltage switchgear At Low Price On Made-in-China.com, accessed September 6, 2025, [https://www.made-in-china.com/price/medium-voltage-switchgear-price.html](https://www.made-in-china.com/price/medium-voltage-switchgear-price.html)  
24. 2+ Year Lead Time on Electrical Equipment : r/AskEngineers \- Reddit, accessed September 6, 2025, [https://www.reddit.com/r/AskEngineers/comments/11b2yr2/2\_year\_lead\_time\_on\_electrical\_equipment/](https://www.reddit.com/r/AskEngineers/comments/11b2yr2/2_year_lead_time_on_electrical_equipment/)  
25. Southwestern states have better solar resources and higher solar PV capacity factors \- U.S. Energy Information Administration (EIA), accessed September 6, 2025, [https://www.eia.gov/todayinenergy/detail.php?id=39832](https://www.eia.gov/todayinenergy/detail.php?id=39832)  
26. 2022 monthly US solar capacity factors underscore winter doldrums \- S\&P Global, accessed September 6, 2025, [https://www.spglobal.com/market-intelligence/en/news-insights/research/2022-monthly-us-solar-capacity-factors-underscore-winter-doldrums](https://www.spglobal.com/market-intelligence/en/news-insights/research/2022-monthly-us-solar-capacity-factors-underscore-winter-doldrums)  
27. Utility-Scale PV | Electricity | 2023 \- NREL ATB, accessed September 6, 2025, [https://atb.nrel.gov/electricity/2023/utility-scale\_pv](https://atb.nrel.gov/electricity/2023/utility-scale_pv)  
28. Global Market Outlook for Solar Power 2025-2029 \- SolarPower Europe, accessed September 6, 2025, [https://www.solarpowereurope.org/insights/outlooks/global-market-outlook-for-solar-power-2025-2029/detail](https://www.solarpowereurope.org/insights/outlooks/global-market-outlook-for-solar-power-2025-2029/detail)  
29. New report: World installed 600 GW of solar in 2024, could be installing 1 TW per year by 2030 \- SolarPower Europe, accessed September 6, 2025, [https://www.solarpowereurope.org/press-releases/new-report-world-installed-600-gw-of-solar-in-2024-could-be-installing-1-tw-per-year-by-2030](https://www.solarpowereurope.org/press-releases/new-report-world-installed-600-gw-of-solar-in-2024-could-be-installing-1-tw-per-year-by-2030)  
30. The battery industry has entered a new phase – Analysis \- IEA, accessed September 6, 2025, [https://www.iea.org/commentaries/the-battery-industry-has-entered-a-new-phase](https://www.iea.org/commentaries/the-battery-industry-has-entered-a-new-phase)  
31. Executive summary – The Role of Critical Minerals in Clean Energy Transitions – Analysis \- IEA, accessed September 6, 2025, [https://www.iea.org/reports/the-role-of-critical-minerals-in-clean-energy-transitions/executive-summary](https://www.iea.org/reports/the-role-of-critical-minerals-in-clean-energy-transitions/executive-summary)  
32. The EV Battery Supply Chain Explained \- RMI, accessed September 6, 2025, [https://rmi.org/the-ev-battery-supply-chain-explained/](https://rmi.org/the-ev-battery-supply-chain-explained/)  
33. Breaking Free from Cobalt Reliance in Lithium-Ion Batteries \- PMC \- PubMed Central, accessed September 6, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC7501431/](https://pmc.ncbi.nlm.nih.gov/articles/PMC7501431/)  
34. Lithium, Cobalt and Nickel: The Gold Rush of the 21st Century \- The Faraday Institution, accessed September 6, 2025, [https://www.faraday.ac.uk/wp-content/uploads/2022/09/Faraday\_Insights\_6\_Updated\_Sept2022\_FINAL.pdf](https://www.faraday.ac.uk/wp-content/uploads/2022/09/Faraday_Insights_6_Updated_Sept2022_FINAL.pdf)  
35. Lithium-based batteries supply chain challenges \- RMIS, accessed September 6, 2025, [https://rmis.jrc.ec.europa.eu/analysis-of-supply-chain-challenges-49b749](https://rmis.jrc.ec.europa.eu/analysis-of-supply-chain-challenges-49b749)  
36. Combustion Turbines \- Environmental Protection Agency (EPA), accessed September 6, 2025, [https://www.epa.gov/sites/default/files/2015-07/documents/catalog\_of\_chp\_technologies\_section\_3.\_technology\_characterization\_-\_combustion\_turbines.pdf](https://www.epa.gov/sites/default/files/2015-07/documents/catalog_of_chp_technologies_section_3._technology_characterization_-_combustion_turbines.pdf)  
37. 3.1 Stationary Gas Turbines For Electricity Generation 3.1.1 General, accessed September 6, 2025, [https://gaftp.epa.gov/ap42/ch03/s01/final/c03s01\_oct1996.pdf](https://gaftp.epa.gov/ap42/ch03/s01/final/c03s01_oct1996.pdf)  
38. Gas Turbine Market Forecast, accessed September 6, 2025, [https://gasturbineworld.com/market-forecast/](https://gasturbineworld.com/market-forecast/)  
39. Gas Turbine Market Size And Share | Industry Report, 2033 \- Grand View Research, accessed September 6, 2025, [https://www.grandviewresearch.com/industry-analysis/gas-turbine-market](https://www.grandviewresearch.com/industry-analysis/gas-turbine-market)  
40. Gas turbine market projections | 2031, accessed September 6, 2025, [https://www.araner.com/blog/gas-turbine-market-projections-2031](https://www.araner.com/blog/gas-turbine-market-projections-2031)  
41. Section 3\. Technology Characterization – Combustion Turbines, accessed September 6, 2025, [https://www.epa.gov/sites/production/files/2015-07/documents/catalog\_of\_chp\_technologies\_section\_3.\_technology\_characterization\_-\_combustion\_turbines.pdf](https://www.epa.gov/sites/production/files/2015-07/documents/catalog_of_chp_technologies_section_3._technology_characterization_-_combustion_turbines.pdf)  
42. Global Natural Gas Production | World gas natural statistics | Enerdata, accessed September 6, 2025, [https://yearbook.enerdata.net/natural-gas/world-natural-gas-production-statistics.html](https://yearbook.enerdata.net/natural-gas/world-natural-gas-production-statistics.html)  
43. Natural gas – Global Energy Review 2025 – Analysis \- IEA, accessed September 6, 2025, [https://www.iea.org/reports/global-energy-review-2025/natural-gas](https://www.iea.org/reports/global-energy-review-2025/natural-gas)  
44. Natural Gas Statistics 2025 By Reserves, Production, Consumption, accessed September 6, 2025, [https://media.market.us/natural-gas-statistics/](https://media.market.us/natural-gas-statistics/)  
45. Data center electricians/HVAC techs \- is there actually a skilled ..., accessed September 6, 2025, [https://www.reddit.com/r/datacenter/comments/1n1gvf0/data\_center\_electricianshvac\_techs\_is\_there/](https://www.reddit.com/r/datacenter/comments/1n1gvf0/data_center_electricianshvac_techs_is_there/)  
46. AI Data Centers Are Coming for Your Land, Water and Power \- CNET, accessed September 6, 2025, [https://www.cnet.com/tech/services-and-software/features/ai-data-centers-are-coming-for-your-land-water-and-power/](https://www.cnet.com/tech/services-and-software/features/ai-data-centers-are-coming-for-your-land-water-and-power/)  
47. Data centers and water use: What to consider, accessed September 6, 2025, [https://freshwater.org/wp-content/uploads/2025/06/Data-Centers-and-Water-Use\_Freshwater.pdf](https://freshwater.org/wp-content/uploads/2025/06/Data-Centers-and-Water-Use_Freshwater.pdf)  
48. Data Centers and Water Consumption | Article | EESI \- Environmental and Energy Study Institute, accessed September 6, 2025, [https://www.eesi.org/articles/view/data-centers-and-water-consumption](https://www.eesi.org/articles/view/data-centers-and-water-consumption)  
49. Data Center Water Usage: A Comprehensive Guide \- Dgtl Infra, accessed September 6, 2025, [https://dgtlinfra.com/data-center-water-usage/](https://dgtlinfra.com/data-center-water-usage/)  
50. Reconductoring US power lines could quadruple new transmission capacity by 2035: report, accessed September 6, 2025, [https://www.utilitydive.com/news/reconductoring-power-lines-transmission-capacity-goldman-gridlab/712643/](https://www.utilitydive.com/news/reconductoring-power-lines-transmission-capacity-goldman-gridlab/712643/)  
51. DOE and Industry Team Up to Keep the Lights On for America | Department of Energy, accessed September 6, 2025, [https://www.energy.gov/oe/articles/doe-and-industry-team-keep-lights-america](https://www.energy.gov/oe/articles/doe-and-industry-team-keep-lights-america)