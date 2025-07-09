# parameters:
# - src_files: {file1, file2, ...}

if {[string equal [get_filesets -quiet "sources_1"] ""]} {
    create_fileset -srcset "sources_1"
}
foreach file $src_files {
    add_files -norecurse $file -fileset [get_filesets "sources_1"]
}
