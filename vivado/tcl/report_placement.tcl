# parameters:
# - cells_of_interest: {cell1, cell2, ...}
# - placement_report_file: str
set fd [open $placement_report_file "w"]
puts $fd "cell,loc"
foreach cell $cells_of_interest {
    set pattern "$cell/.*"
    foreach children [get_cells -hierarchical -regexp $pattern] {
        set loc [get_property LOC $children]
        puts $fd "$children,$loc"
    }
}
close $fd
