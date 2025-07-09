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

def add_ooc_constraint(constraint_file: str) -> list[str]:
    return [
        f"set constraint_file {constraint_file}\n",
    ] + _load_template("add_ooc_constraint.tcl")

def add_sources(src_files: list[str]) -> list[str]:
    tcl_list = " ".join(src_files)
    return [
        f"set src_files {{{tcl_list}}}\n",
    ] + _load_template("add_sources.tcl")

def create_project(project_name: str, project_work_dir: str, part_number: str) -> list[str]:
    return [
        f"set project_name {project_name}\n",
        f"set project_work_dir {project_work_dir}\n",
        f"set part_number {part_number}\n",
    ] + _load_template("create_project.tcl")

def ooc_synthesis(
    project_name: str,
    project_work_dir: str,
    flatten_hierarchy: str,
    top: str,
    verilog_defines: dict[str, str],
    synth_directive: str,
) -> list[str]:
    verilog_defines_str = " ".join(
        f"{k}={v}" for k, v in verilog_defines.items()
    )
    return [
        f"set project_name {project_name}\n",
        f"set project_work_dir {project_work_dir}\n",
        f"set flatten_hierarchy {flatten_hierarchy}\n",
        f"set top {top}\n",
        f"set verilog_defines {{{verilog_defines_str}}}\n",
        f"set synth_directive {synth_directive}\n",
    ] + _load_template("ooc_synthesis.tcl")

def implementation(
    project_name: str,
    project_work_dir: str,
    opt_directive: str,
    place_directive: str,
    route_directive: str,
) -> list[str]:
    return [
        f"set project_name {project_name}\n",
        f"set project_work_dir {project_work_dir}\n",
        f"set opt_directive {opt_directive}\n",
        f"set place_directive {place_directive}\n",
        f"set route_directive {route_directive}\n",
    ] + _load_template("implementation.tcl")

def open_checkpoint(dcp_file: str) -> list[str]:
    return [
        f"set dcp_file {dcp_file}\n",
    ] + _load_template("open_checkpoint.tcl")

def report_critical_path(
    critical_path_report_file: str,
    column_style: str = "anchor_left",
) -> list[str]:
    '''
    Use "anchor_left" for human-readable report.
    Use "fixed_width" for easier parsing.
    '''
    return [
        f"set critical_path_report_file {critical_path_report_file}\n",
        f"set column_style {column_style}\n",
    ] + _load_template("report_critical_path.tcl")

def report_placement(placement_report_file: str, cells_of_interest: list[str]) -> list[str]:
    tcl_list = " ".join(cells_of_interest)
    return [
        f"set placement_report_file {placement_report_file}\n",
        f"set cells_of_interest {{{tcl_list}}}\n",
    ] + _load_template("report_placement.tcl")
