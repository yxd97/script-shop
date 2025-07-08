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
