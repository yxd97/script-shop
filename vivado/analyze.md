## Get the locations of placed cells

```tcl
# Suppose we have opened a post-placement design checkpoint


# specify the hierarchy we are interested in
# all cells under this hierarchy will be searched
set region_of_interest "ROI"

# open a file to save the locations
set output_fd [open "placement_report.rpt" w]

# use a regular expression to match children cells in the region of interest
set pattern "$region_of_interest/.*"
foreach cell [get_cells -hierarchical -regexp $pattern] {
    set loc [get_property LOC $cell]

    # ignore cells without a location (e.g., power rails)
    if {$loc != ""} {
        puts "Cell: $cell, LOC: $loc"
        puts $output_fd "$cell: $loc"
    }
}

close $output_fd
```

## Get the critical path timing report

```tcl
set slim_options "-no_header -no_pblock -no_pr_attribute -no_report_unconstrained -no_reused_label"
report_timing -path_type full {*}$slim_options -file "critical_path_report.rpt"
```

## Get the detailed routing path of the critical path

```tcl
set cp [get_timing_paths -nworst 1]
set start_ff_clk [get_property STARTPOINT_PIN $cp]
# timing path uses clock-to-q delay and hence starts from C pin, but the routing starts from the Q pin
# we alter the start pin to the Q pin of the start flip-flop
set start_ff_q [get_pins [string map {"/C" "/Q"} [get_property NAME $start_ff_clk]]]
set end_ff_d [get_property ENDPOINT_PIN $cp]
set start_node [get_nodes -of_objects [get_site_pins -of_objects $start_ff_q]]
set end_node [get_nodes -of_objects [get_site_pins -of_objects $end_ff_d]]
set path [find_routing_path -from $start_node -to $end_node -ignore_all_routing -allow_overlap]
foreach node $path {
    puts $node
}
set wns [get_property SLACK $cp]
puts $wns
```
