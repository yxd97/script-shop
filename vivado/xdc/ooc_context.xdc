# parameters:
# - pin: str
# - canvas_loc: str

set_property HD.PARTPIN_RANGE $canvas_loc [get_ports $pin]
