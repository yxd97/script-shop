# parameters:
# - constraint_file: str

if {[string equal [get_filesets -quiet "constrs_1"] ""]} {
    create_fileset -constrset "constrs_1"
}
add_files -fileset [get_filesets "constrs_1"] $constraint_file
set_property USED_IN {implementation out_of_context} [get_files $constraint_file]
