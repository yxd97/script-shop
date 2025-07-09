# parameters:
# - opt_directive: str
# - place_directive: str
# - route_directive: str
# - project_work_dir: str
# - project_name: str

opt_design -directive $opt_directive
write_checkpoint -force ${project_work_dir}/${project_name}_opted.dcp
place_design -directive $place_directive
write_checkpoint -force ${project_work_dir}/${project_name}_placed.dcp
route_design -directive $route_directive
write_checkpoint -force ${project_work_dir}/${project_name}_routed.dcp
