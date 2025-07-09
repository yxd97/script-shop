# parameters:
# - critical_path_report_file: str
# - column_style: str (anchor_left, fixed_width)
set slim_options "-no_header -no_pblock -no_pr_attribute -no_report_unconstrained -no_reused_label"
report_timing -path_type full {*}$slim_options -column_style $column_style -file $critical_path_report_file

