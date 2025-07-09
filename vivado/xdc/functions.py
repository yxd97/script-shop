import os

def _get_template_path(template_name: str) -> str:
    return os.path.abspath(os.path.join(os.path.dirname(__file__), template_name))

def _load_template(template_name: str) -> list[str]:
    template = _get_template_path(template_name)
    with open(template, "r") as f:
        lines = f.readlines()
    return [
        line for line in lines
        if not line.startswith("#") and len(line.strip()) > 0
    ] + ["\n"]

def floorplan_module(
    module: str,
    pblock_name: str,
    loc: str,
    parent_pblock_name: str|None = None,
) -> list[str]:
    commands = [
        f"set module {module}\n",
        f"set pblock_name {pblock_name}\n",
        f"set loc {loc}\n",
    ]
    if parent_pblock_name is not None:
        commands.append(f"set parent_pblock_name {parent_pblock_name}\n")
        return commands + _load_template("nested_floorplan_module.xdc")
    return commands + _load_template("floorplan_module.xdc")

def ooc_context(pins: list[str], canvas_loc: str) -> list[str]:
    tcl_routine = _load_template("ooc_context.xdc")
    commands = []
    for pin in pins:
        commands.extend(
            [
                f"set pin {pin}\n",
                f"set canvas_loc {canvas_loc}\n",
            ] + tcl_routine
        )
    return commands

def ooc_create_clock(clk_period_ns: float, clk_pin: str, clk_source: str) -> list[str]:
    return [
        f"set clk_period_ns {clk_period_ns}\n",
        f"set clk_pin {clk_pin}\n",
        f"set clk_source {clk_source}\n",
    ] + _load_template("ooc_create_clock.xdc")

def ooc_master_pblock(canvas_loc: str, master_pblock_name: str) -> list[str]:
    return [
        f"set canvas_loc {canvas_loc}\n",
        f"set master_pblock_name {master_pblock_name}\n",
    ] + _load_template("ooc_master_pblock.xdc")
