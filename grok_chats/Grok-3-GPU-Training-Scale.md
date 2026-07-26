# Grok 3: GPU Training Scale

- Source: https://grok.com/share/bGVnYWN5_1f589443-c8a1-457f-aa48-9dcec8600ccb
- Created: 2025-02-28
- Messages: 4

---

## Human

How many GPUs were used to train Grok 3

---

## Assistant

Grok 3 was trained using 200,000 GPUs. This figure comes from the expanded Colossus supercomputer cluster in Memphis, Tennessee, which doubled from its initial 100,000 Nvidia H100 GPUs to 200,000 GPUs for the training process.

---

## Human

Tell me about how fast Colossus was built, and what measures were taken for energy and cooling and more

---

## Assistant

The Colossus supercomputer, developed by xAI in Memphis, Tennessee, is a remarkable feat of engineering, not just for its computational power but for the speed of its construction and the innovative measures implemented to support its energy and cooling needs.

### Construction Speed
Colossus was built at an astonishing pace. The initial phase, featuring 100,000 Nvidia H100 GPUs, was completed in just 122 days—from conception to operational status—going live on July 22, 2024. This rapid timeline is unprecedented for a project of this scale, which typically takes months or even years. The first servers were delivered and running workloads within 19 days, a testament to the efficiency and urgency driving xAI’s efforts. After this initial deployment, xAI doubled the cluster to 200,000 GPUs (including a mix of H100 and H200 GPUs) in an additional 92 days, further showcasing their ability to scale quickly. Nvidia CEO Jensen Huang described this as a "superhuman" achievement, noting that other companies might take a full year to accomplish what xAI did in weeks.

The speed was driven by necessity—xAI needed massive compute power to train Grok 3 after working with a much smaller 8,000-GPU setup for Grok 2. To meet this timeline, xAI repurposed an abandoned Electrolux factory, avoiding the 18–24-month delays quoted for new construction. They leased generators and mobilized a significant portion of the U.S.’s mobile cooling capacity to get started, bypassing traditional delays in infrastructure development.

### Energy Measures
Colossus’s energy demands are immense, reflecting its status as the world’s largest AI training cluster. The initial 100,000-GPU setup required approximately 50 megawatts of power, with the doubled 200,000-GPU cluster now estimated to draw around 250 megawatts—enough to power roughly 160,000 homes. To manage this:

- **Temporary Power Solutions**: Initially, xAI relied on 14 mobile gas turbines from Voltagrid, each providing 2.5 MW, supplementing the local grid’s limited 8 MW capacity. These turbines, burning methane, bridged the gap while permanent infrastructure was developed, though their use sparked environmental concerns over air quality in South Memphis.
- **Grid Upgrades**: Memphis Light, Gas, and Water (MLGW), in collaboration with the Tennessee Valley Authority (TVA), is upgrading the site’s capacity. By August 2024, MLGW provided 50 MW, with plans for a new substation—funded by xAI at $24 million—to deliver an additional 150 MW. This substation, once completed, will be handed over to MLGW after xAI recoups its costs via rebates.
- **Tesla Megapacks**: To handle power fluctuations (AI training can demand sudden bursts of 10–20 MW), xAI integrated Tesla’s Megapack batteries as an energy buffer. These stabilize the load and could potentially allow Colossus to operate independently or even supply power back to the grid during peak demand, aligning with Musk’s vision for sustainability.

Future plans hint at further expansion to 1 million GPUs, potentially requiring 1–1.5 gigawatts—about a third of Memphis’s peak demand—posing a significant challenge to the local grid and necessitating additional substations or power plants.

### Cooling Measures
Cooling a cluster of 200,000 GPUs, each generating substantial heat, required innovative solutions:

- **Liquid Cooling System**: Colossus employs a custom liquid-cooling design, developed with Supermicro, replacing traditional air-cooling fans. Each rack, housing 64 GPUs (eight 4U servers with eight GPUs each), integrates a Cooling Distribution Unit (CDU) that circulates coolant to manage heat. This system, showcased at SC23, uses quick-disconnect fittings for easy maintenance and is critical for maintaining stability at scale.
- **Mobile Cooling Units**: During the rushed initial build, xAI rented a quarter of the U.S.’s mobile cooling capacity to kickstart operations before the permanent system was ready.
- **Water Usage**: The facility draws up to 1.3 million gallons of water daily from the Memphis Aquifer for cooling, about 3% of the local wellfield’s capacity. To mitigate this, xAI plans a $78 million graywater recycling facility, which could reduce aquifer strain by up to 10 million gallons daily once operational.

### Additional Measures and Challenges
- **Networking**: Colossus uses Nvidia’s Spectrum-X Ethernet platform for its RDMA fabric, achieving 95% data throughput with near-zero packet loss—crucial for syncing 200,000 GPUs efficiently.
- **Hardware Debugging**: The rapid assembly faced issues like mismatched BIOS firmware, tangled network cables, and cosmic-ray-induced bit flips, which xAI’s team tackled on the fly to maintain uptime.
- **Environmental and Community Impact**: The project’s speed and scale have raised concerns. Temporary gas turbines prompted criticism from groups like the Southern Environmental Law Center for lacking permits, exacerbating Memphis’s ozone pollution. Residents near the historically Black neighborhoods of South Memphis worry about air quality and resource strain, though xAI’s promised water recycling and grid enhancements aim to address some of these issues.

### Looking Ahead
Colossus’s construction and operation reflect xAI’s aggressive push to lead in AI development, leveraging rapid deployment, cutting-edge hardware, and adaptive infrastructure solutions. Plans to upgrade to Nvidia’s H200 GPUs (141 GB HBM3e memory) and eventually Blackwell GB200 chips (20 PFLOPS each) signal ongoing evolution. However, balancing this technological ambition with environmental and community considerations remains a work in progress, with xAI navigating a complex landscape of innovation and responsibility.
