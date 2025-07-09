# parameters:
# - canvas_loc: str
# - master_pblock_name: str
create_pblock $master_pblock_name
resize_pblock [get_pblocks $master_pblock_name] -add $canvas_loc
add_cells_to_pblock -top [get_pblocks $master_pblock_name]
set_property CONTAIN_ROUTING true [get_pblocks $master_pblock_name]
