# parameters:
# - flatten_hierarchy: str (rebuilt, full, none)
# - top: str
# - verilog_defines: {MACRO1=value1 MACRO2=value2 ...}
# - synth_directive: str (default, ...)
# - project_work_dir: str
# - project_name: str

synth_design -mode out_of_context -flatten_hierarchy $flatten_hierarchy -top $top -verilog_define $verilog_defines -directive $synth_directive
write_checkpoint -force ${project_work_dir}/${project_name}_ooc_synthesis.dcp
