## USE Python XML library to read the HLS report file

```python
import os
import xml.etree.ElementTree as ET
from dataclasses import dataclass

@dataclass
class VitisHLSResourceUtilization:
    usage = 0.0
    available = 0.0
    percentage = 0.0

    def from_xml(self, used:ET.Element, available:ET.Element):
        self.usage = float(used.text)
        self.available = float(available.text)
        self.percentage = (self.usage / self.available) * 100
        return self

@dataclass
class VitisHLSAreaResult:
    lut = VitisHLSResourceUtilization()
    ff = VitisHLSResourceUtilization()
    bram = VitisHLSResourceUtilization()
    uram = VitisHLSResourceUtilization()
    dsp = VitisHLSResourceUtilization()

    def from_xml(self, used:ET.Element, available:ET.Element):
        self.lut = VitisHLSResourceUtilization().from_xml(
            used.find('LUT'),
            available.find('LUT')
        )
        self.ff = VitisHLSResourceUtilization().from_xml(
            used.find('FF'),
            available.find('FF')
        )
        self.bram = VitisHLSResourceUtilization().from_xml(
            used.find('BRAM_18K'),
            available.find('BRAM_18K')
        )
        self.uram = VitisHLSResourceUtilization().from_xml(
            used.find('URAM'),
            available.find('URAM')
        )
        self.dsp = VitisHLSResourceUtilization().from_xml(
            used.find('DSP'),
            available.find('DSP')
        )
        return self

@dataclass
class VitisHLSTimingResult:
    target_cycle_time_ns:float
    estimated_cycle_time_ns:float
    slack_ns:float

def read_synth_report(report_file:str) -> Tuple[VitisHLSTimingResult, VitisHLSAreaResult]:
    if not os.path.exists(report_file):
        raise FileNotFoundError(f"Report file {report_file} does not exist. Please build first.")
    tree = ET.parse(report_file)
    cycle_time = tree.find('PerformanceEstimates/SummaryOfTimingAnalysis/EstimatedClockPeriod')
    cycle_time = float(cycle_time.text)
    timing = VitisHLSTimingResult(
        target_cycle_time_ns = self.clock_period_ns,
        estimated_cycle_time_ns = cycle_time,
        slack_ns = self.clock_period_ns - cycle_time
    )
    used_resources = tree.find('AreaEstimates/Resources')
    available_resources = tree.find('AreaEstimates/AvailableResources')
    area = VitisHLSAreaResult().from_xml(used_resources, available_resources)
    return timing, area
```
