## Basic Vitis HLS Script

```tcl
# can use -reset to reset the project
open_project $project_name

# add source files, use -cflags to specify compiler flags such as include dir
add_files $file -cflags $flags
# add testbench files
add_files -tb $tb_file -cflags $flags

# open a solution and select the top function
# one set of files can have multiple solutions with different top functions
open_solution $solution_name
set_top $top_function

# can use xxxMHz for period. Tool will convert it to ns
create_clock -period $clock_period

csim_design -argv $tb_args -ldflags $flags

csynth_design

# -O means enable compiler optimizations
# -trace_level options: all port port_hier
cosim_design -argv $tb_args -ldflags $flags -trace_level all -O

exit
```
