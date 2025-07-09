# parameters:
# - module: str (a regex pattern)
# - pblock_name: str
# - loc: str
# - parent_pblock_name: str

create_pblock $pblock_name
resize_pblock [get_pblocks $pblock_name] -add $loc
add_cells_to_pblock -clear_locs [get_pblocks $pblock_name] [get_cells -regexp $module]
set_property PARENT [get_pblocks $parent_pblock_name] [get_pblocks $pblock_name]

