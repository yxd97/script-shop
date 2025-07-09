# parameters:
# - module: str (a regex pattern)
# - pblock_name: str
# - loc: str

create_pblock pblock_$pblock_name
resize_pblock [get_pblocks pblock_$pblock_name] -add $loc
add_cells_to_pblock -clear_locs [get_pblocks pblock_$pblock_name] [get_cells -regexp $module]
