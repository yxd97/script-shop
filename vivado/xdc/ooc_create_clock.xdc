# parameters:
# - clk_period_ns: float
# - clk_pin: str
# - clk_source: str
create_clock -period $clk_period_ns [get_ports $clk_pin]
set_property HD.CLK_SRC $clk_source [get_ports $clk_pin]
