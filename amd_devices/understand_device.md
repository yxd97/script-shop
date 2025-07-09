## Get all sites of a certain type and their clock region
can be useful for floorplanning
```tcl
set all_sites [get_sites -filter { SITE_TYPE == "SLICEL" || SITE_TYPE == "SLICEM" } ]
set fd [open "sites.csv" w]
puts $fd "site_name,site_type,clock_region"
foreach site $all_sites {
    set site_name [get_property NAME $site]
    set site_type [get_property SITE_TYPE $site]
    set clock_region [get_property CLOCK_REGION $site]
    puts $fd "$site_name,$site_type,$clock_region"
}
close $fd
```
common types of interest:
- SLICEL
- SLICEM
- DSP48E2
- RAMB36
- RAMB180
- RAMB181
- RAMBFIFO18
- RAMBFIFO36
- FIFO18_0
- FIFO36
- URAM288
- BUFGCTRL
- BUFGCE


## Python script to figure out the range of each SLR
Using U280 as an example.

```python
import csv
import sys
import re
from typing import Tuple

table = sys.argv[1]

columns = ["slice_name", "site_type", "clock_region"]

def get_coord(site_name:str) -> Tuple[int, int]:
    x_coord = int(re.search(r"X(\d+)", site_name).group(1))
    y_coord = int(re.search(r"Y(\d+)", site_name).group(1))
    return x_coord, y_coord

class SLR:
    def __init__(self, xmin:int, xmax:int, ymin:int, ymax:int):
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax

    def __contains__(self, coord:Tuple[int, int]) -> bool:
        x, y = coord
        return self.xmin <= x <= self.xmax and self.ymin <= y <= self.ymax


U280_SLR = (
    SLR(0, 7, 0, 3),
    SLR(0, 7, 4, 7),
    SLR(0, 7, 8, 11),
)

with open(table, "r") as f:
    reader = csv.DictReader(f)
    slice_xmin = {
        0: 9999,
        1: 9999,
        2: 9999
    }
    slice_xmax = {
        0: -9999,
        1: -9999,
        2: -9999
    }
    slice_ymin = {
        0: 9999,
        1: 9999,
        2: 9999
    }
    slice_ymax = {
        0: -9999,
        1: -9999,
        2: -9999
    }
    for row in reader:
        sx, sy = get_coord(row["slice_name"])
        crx, cry = get_coord(row["clock_region"])
        for i, slr in enumerate(U280_SLR):
            if (crx, cry) in slr:
                slice_xmin[i] = min(slice_xmin[i], sx)
                slice_xmax[i] = max(slice_xmax[i], sx)
                slice_ymin[i] = min(slice_ymin[i], sy)
                slice_ymax[i] = max(slice_ymax[i], sy)
    for i in range(3):
        print(f"SLR {i}: SLICE_X{slice_xmin[i]}Y{slice_ymin[i]}:SLICE_X{slice_xmax[i]}Y{slice_ymax[i]}")
```
