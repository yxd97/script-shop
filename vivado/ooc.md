## Example out-of-context (OOC) build script for Vivado

```tcl
# may add -force to overwrite existing project
create_project "baseline" "build" -part "xcu280-fsvh2892-2L-e"

# add source RTL files
if {[string equal [get_filesets -quiet "sources_1"] ""]} {
  create_fileset -srcset "sources_1"
}
add_files ../../rtl/reg.v -fileset [get_filesets "sources_1"]
add_files ../../hls/build/mm_si/impl/verilog/mm_si_mul_32s_32s_32_1_1.v -fileset [get_filesets "sources_1"]
add_files ../../hls/build/mm_si/impl/verilog/mm_si_mm_si_Pipeline_VITIS_LOOP_35_3.v -fileset [get_filesets "sources_1"]
add_files ../../hls/build/mm_so/impl/verilog/mm_so.v -fileset [get_filesets "sources_1"]
add_files ../../hls/build/mm_si/impl/verilog/mm_si.v -fileset [get_filesets "sources_1"]
add_files ../../hls/build/mm_so/impl/verilog/mm_so_flow_control_loop_pipe.v -fileset [get_filesets "sources_1"]
add_files ../../hls/build/mm_si/impl/verilog/mm_si_mul_32s_32s_32_5_1.v -fileset [get_filesets "sources_1"]
add_files ../../rtl/top.v -fileset [get_filesets "sources_1"]
add_files ../../hls/build/mm_so/impl/verilog/mm_so_mul_32s_32s_32_5_1.v -fileset [get_filesets "sources_1"]
add_files ../../rtl/ram.v -fileset [get_filesets "sources_1"]
add_files ../../hls/build/mm_so/impl/verilog/mm_so_mul_32s_32s_32_1_1.v -fileset [get_filesets "sources_1"]
add_files ../../hls/build/mm_si/impl/verilog/mm_si_flow_control_loop_pipe_sequential_init.v -fileset [get_filesets "sources_1"]

# the first top is a command keyword, the second top refers to the top-level module named "top"
set_property top top [get_filesets "sources_1"]

# add ooc constraints
if {[string equal [get_filesets -quiet "constrs_1"] ""]} {
  create_fileset -constrset "constrs_1"
}
add_files constraints.xdc -fileset [get_filesets "constrs_1"]
set_property USED_IN {implementation out_of_context} [get_files constraints.xdc]


synth_design -mode out_of_context -flatten_hierarchy rebuilt -verilog_define PIPE_STAGES=1 -top top -directive default
write_checkpoint -force baseline_synthed.dcp

opt_design -directive Default
write_checkpoint -force baseline_opted.dcp

place_design -directive Default
write_checkpoint -force baseline_placed.dcp

route_design -directive Default
write_checkpoint -force baseline_routed.dcp


close_project
```

## OOC Constraints
```tcl
# create clock
create_clock [get_ports ap_clk] -period 3.33 -waveform {0.000 1.665} -name ap_clk

# create master pblock, which is the boundary of the ooc module
# here I used the entire SLR0
create_pblock pblock_top
resize_pblock [get_pblocks pblock_top] -add CLOCKREGION_X0Y0:CLOCKREGION_X7Y3
add_cells_to_pblock -top [get_pblocks pblock_top]

# setup ooc context

# keep all routing within the master pblock
set_property CONTAIN_ROUTING true [get_pblocks pblock_top]

# pick a clock source for the design
set_property HD.CLK_SRC BUFGCTRL_X0Y15 [get_ports ap_clk]

# specify where should the top-level IOs should be placed
# here I used the same region as the master pblock (entire SLR0), which is the weakest constraint
set_property HD.PARTPIN_RANGE SLICE_X0Y0:SLICE_X232Y239 [get_ports ap_rst]
set_property HD.PARTPIN_RANGE SLICE_X0Y0:SLICE_X232Y239 [get_ports ap_start]
set_property HD.PARTPIN_RANGE SLICE_X0Y0:SLICE_X232Y239 [get_ports ap_done]
set_property HD.PARTPIN_RANGE SLICE_X0Y0:SLICE_X232Y239 [get_ports ap_idle]
set_property HD.PARTPIN_RANGE SLICE_X0Y0:SLICE_X232Y239 [get_ports ap_ready]
set_property HD.PARTPIN_RANGE SLICE_X0Y0:SLICE_X232Y239 [get_ports mm_so_A_address0*]
set_property HD.PARTPIN_RANGE SLICE_X0Y0:SLICE_X232Y239 [get_ports mm_so_A_ce0*]
set_property HD.PARTPIN_RANGE SLICE_X0Y0:SLICE_X232Y239 [get_ports mm_so_A_q0*]
set_property HD.PARTPIN_RANGE SLICE_X0Y0:SLICE_X232Y239 [get_ports mm_so_B_address0*]
set_property HD.PARTPIN_RANGE SLICE_X0Y0:SLICE_X232Y239 [get_ports mm_so_B_ce0*]
set_property HD.PARTPIN_RANGE SLICE_X0Y0:SLICE_X232Y239 [get_ports mm_so_B_q0*]
set_property HD.PARTPIN_RANGE SLICE_X0Y0:SLICE_X232Y239 [get_ports mm_si_B_address0*]
set_property HD.PARTPIN_RANGE SLICE_X0Y0:SLICE_X232Y239 [get_ports mm_si_B_ce0*]
set_property HD.PARTPIN_RANGE SLICE_X0Y0:SLICE_X232Y239 [get_ports mm_si_B_q0*]
set_property HD.PARTPIN_RANGE SLICE_X0Y0:SLICE_X232Y239 [get_ports mm_si_C_address0*]
set_property HD.PARTPIN_RANGE SLICE_X0Y0:SLICE_X232Y239 [get_ports mm_si_C_ce0*]
set_property HD.PARTPIN_RANGE SLICE_X0Y0:SLICE_X232Y239 [get_ports mm_si_C_we0*]
set_property HD.PARTPIN_RANGE SLICE_X0Y0:SLICE_X232Y239 [get_ports mm_si_C_d0*]
set_property HD.PARTPIN_RANGE SLICE_X0Y0:SLICE_X232Y239 [get_ports mm_si_C_address1*]
set_property HD.PARTPIN_RANGE SLICE_X0Y0:SLICE_X232Y239 [get_ports mm_si_C_ce1*]
set_property HD.PARTPIN_RANGE SLICE_X0Y0:SLICE_X232Y239 [get_ports mm_si_C_q1*]

# optional: floorplanning of submodules
create_pblock pblock_mm_so_inst
set_property PARENT [get_pblocks pblock_top] [get_pblocks pblock_mm_so_inst]
add_cells_to_pblock -clear_locs [get_pblocks pblock_mm_so_inst] [get_cells -regexp mm_so_inst]
resize_pblock [get_pblocks pblock_mm_so_inst] -add CLOCKREGION_X0Y0

create_pblock pblock_mm_si_inst
set_property PARENT [get_pblocks pblock_top] [get_pblocks pblock_mm_si_inst]
add_cells_to_pblock -clear_locs [get_pblocks pblock_mm_si_inst] [get_cells -regexp mm_si_inst]
resize_pblock [get_pblocks pblock_mm_si_inst] -add CLOCKREGION_X7Y3

create_pblock pblock_registers
set_property PARENT [get_pblocks pblock_top] [get_pblocks pblock_registers]
add_cells_to_pblock -clear_locs [get_pblocks pblock_registers] [get_cells -regexp additional_regs.*]
resize_pblock [get_pblocks pblock_registers] -add CLOCKREGION_X0Y0:CLOCKREGION_X7Y3

```