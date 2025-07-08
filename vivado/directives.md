## Vivado Synthesis/Optimization/Placement/Routing Direvtives

Use them in `[synth/opt/place/route]_design -driective <strategy>`

### Synthesis Strategies
 - **default** - Run the default synthesis process.
 - **runtimeoptimized** - Perform fewer timing optimizations and eliminate some RTL optimizations to reduce synthesis run time.
 - **AreaOptimized_high** - Perform general area optimizations including AreaMapLargeShiftRegToBRAM, AreaThresholdUseDSP directives.
 - **AreaOptimized_medium** - Perform general area optimizations including forcing ternary adder implementation, applying new thresholds for use of carry chain in comparators, and implementing area optimized multiplexers.
 - **AlternateRoutability** - Algorithms to improve routability with reduced use of MUXFs and CARRYs.
 - **AreaMapLargeShiftRegToBRAM** - Detects large shift registers and implements them using dedicated blocks of RAM.
 - **AreaMultThresholdDSP** - Lower threshold for dedicated DSP block inference for packing multipliers.
 - **FewerCarryChains** - Higher operand size threshold to use LUTs instead of the carry chain.
 - **PerformanceOptimized** - Perform general timing optimizations including logic level reduction at the expense of area.
 - **LogicCompaction** – Configure LUTs and Carry chains for multipliers in a way that makes it easier for the placer to pack these structures into small areas.

### Optimization Strategies
 - **Explore** - Run additional optimizations to improve results.
 - **ExploreArea** - Run Explore with resynth_area, to reduce the number of LUTs.
 - **ExploreWithRemap** - Run Explore with aggresive_remap optimization to compress logic levels.
 - **ExploreSequentialArea** - Run Explore with resynth_seq_area optimization to reduce registers and related combinational logic.
 - **RuntimeOptimized** - Runs Default without bram_power_opt. Run the fewest optimizations, trading optimization results for faster runtime.
 - **RQS** - Instructs opt_design to select the opt_design directive specified by the report_qor_suggestion strategy suggestion. Requires an RQS file with a strategy suggestion to be read in prior to calling this directive. See report_qor_suggestions -help for more details.
 - **Default** - Run the default optimization.

### Placement Strategies
 - **Explore** - Increased placer effort in detail placement and post-placement optimization .
 - **EarlyBlockPlacement** - Timing-driven placement of RAM and DSP blocks. The RAM and DSP block locations are finalized early in the placement process and are used as anchors to place the remaining logic.
 - **WLDrivenBlockPlacement** - Wire length-driven placement of RAM and DSP blocks. Override timing-driven placement by directing the Vivado™ placer to minimize the distance of connections to and from blocks.
 - **ExtraNetDelay_high** - Increases estimated delay of high fanout and long-distance nets. Three levels of pessimism are supported: high, medium, and low. ExtraNetDelay_high applies the highest level of pessimism.
 - **ExtraNetDelay_low** - Increases estimated delay of high fanout and long-distance nets. Three levels of pessimism are supported: high, medium, and low. ExtraNetDelay_low applies the lowest level of pessimism.
 - **AltSpreadLogic_high** - Spreads logic throughout the device to avoid creating congested regions. Three levels are supported: high, medium, and low. AltSpreadLogic_high achieves the highest level of spreading.
 - **AltSpreadLogic_medium** - Spreads logic throughout the device to avoid creating congested regions. Three levels are supported: high, medium, and low. AltSpreadLogic_medium achieves a medium level of spreading compared to low and high.
 - **AltSpreadLogic_low** - Spreads logic throughout the device to avoid creating congested regions. Three levels are supported: high, medium, and low. AltSpreadLogic_low achieves the lowest level of spreading.
 - **ExtraPostPlacementOpt** - Increased placer effort in post-placement optimization.
 - **ExtraTimingOpt** - Use an alternate algorithm for timing-driven placement with greater effort for timing.
 - **SSI_SpreadLogic_high** - Distribute logic across SLRs. SSI_SpreadLogic_high achieves the highest level of distribution.
 - **SSI_SpreadLogic_low** - Distribute logic across SLRs. SSI_SpreadLogic_low achieves a minimum level of logic distribution, while reducing placement runtime.
 - **SSI_SpreadSLLs** - Partition across SLRs and allocate extra area for regions of higher connectivity.
 - **SSI_BalanceSLLs** - Partition across SLRs while attempting to balance SLLs between SLRs.
 - **SSI_BalanceSLRs** - Partition across SLRs to balance number of cells between SLRs.
 - **SSI_HighUtilSLRs** - Direct the placer to attempt to place logic closer together in each SLR.
 - **RuntimeOptimized** - Run fewest iterations, trade higher design performance for faster runtime.
 - **Quick** - Absolute, fastest runtime, non-timing-driven, performs the minimum required placement for a legal design.
 - **RQS** - Instructs place_design to select the place_design directive specified by the report_qor_suggestion strategy suggestion. Requires an RQS file with a strategy suggestion to be read in prior to calling this directive. See report_qor_suggestions -help for more details.
 - **Auto_1** - Instructs place_design to use machine learning to select the best predicted directive.
 - **Auto_2** - Instructs place_design to use machine learning to select the second best predicted directive.
 - **Auto_3** - Instructs place_design to use machine learning to select the third best predicted directive.
 - **Default** - Run place_design with default settings.

### Routing Strategies
 - **Explore** - Causes the Vivado™ router to explore different critical path routes based on timing, after an initial route.
 - **AggressiveExplore** - Directs the router to further expand its exploration of critical path routes while maintaining original timing budgets. The router runtime might be significantly higher compared to the Explore directive as the router uses more aggressive optimization thresholds to attempt to meet timing constraints.
 - **NoTimingRelaxation** - Prevents the router from relaxing timing to complete routing. If the router has difficulty meeting timing, it will run longer to try to meet the original timing constraints.
 - **MoreGlobalIterations** - Uses detailed timing analysis throughout all stages instead of just the final stages, and will run more global iterations even when timing improves only slightly.
 - **HigherDelayCost** - Adjusts the router's internal cost functions to emphasize delay over iterations, allowing a trade-off of runtime for better performance.
 - **AdvancedSkewModeling** - Uses more accurate skew modeling throughout all routing stages which may improve design performance on higher-skew clock networks.
 - **AlternateCLBRouting** - (UltraScale™ only) Chooses alternate routing algorithms that require extra runtime but may help resolve routing congestion.
 - **RuntimeOptimized** - Run fewest iterations, trade higher design performance for faster runtime.
 - **Quick** - Absolute fastest runtime, non-timing-driven, performs the minimum required routing for a legal design.
 - **Default** - Run route_design with default settings.
