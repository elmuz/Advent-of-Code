from functools import total_ordering
from pathlib import Path
from random import random
from typing import Dict, List


@total_ordering
class Range:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
        assert self.start <= self.end
    
    def __contains__(self, item) -> bool:
        if item < self.start:
            return False
        if item > self.end:
            return False
        return True
    
    def __lt__(self, other) -> bool:
        return self.start < other.start
    
    def __eq__(self, other) -> bool:
        return self.start == other.start and self.end == other.end
    
    def __hash__(self):
        return hash(f"{self.start}-{self.end}-{random()}")


class Map:
    def __init__(self, ranges: List[str]):
        self.ranges: Dict[Range, int] = {}
        for line in ranges:
            offset, start, length = [int(num_str) for num_str in line.split(" ")]
            self.ranges[Range(start, start + length - 1)] = offset
    
    def __getitem__(self, item: int) -> int:
        for r, offset in self.ranges.items():
            if item in r:
                return offset + (item - r.start)
        return item
    
    def get_ranges(self, r: Range) -> List[Range]:
        output = []
        for range_i, offset in sorted(self.ranges.items()):
            # 1) disjoint
            if range_i.end < r.start:
                continue
            if range_i.start > r.end:
                break
            # 2) crossing
            overlap_start = max(r.start, range_i.start)
            overlap_end = min(r.end, range_i.end)
            if overlap_start > r.start:
                output.append(Range(r.start, overlap_start - 1))
                r.start = overlap_start
            output.append(Range(offset + overlap_start - range_i.start, offset + overlap_end - range_i.start))
            r.start = overlap_end + 1
        if r.start <= r.end:
            output.append(Range(r.start, r.end))
        return output


class Seeds:
    def __init__(self, line: str):
        seed_values = line.split(" ")
        self.ranges: List[Range] = []
        for start, length in zip(seed_values[::2], seed_values[1::2]):
            self.ranges.append(Range(int(start), int(start) + int(length) - 1))
    
    def __contains__(self, item: int) -> bool:
        for r in self.ranges:
            if item in r:
                return True
        return False
        

def run(fpath: Path) -> int:
    with fpath.open() as f:
        lines = f.readlines()
    
    idx = 0
    assert lines[idx].startswith("seeds:")
    seed_line= lines[idx].split(": ")[1].strip()
    seeds = Seeds(seed_line)
    idx += 2
    
    assert lines[idx].startswith("seed-to-soil")
    idx += 1
    seed_to_soil_lines = []
    while lines[idx].strip() != "":
        seed_to_soil_lines.append(lines[idx])
        idx += 1
    seed_to_soil = Map(seed_to_soil_lines)
    idx += 1
    soils = []
    for s in seeds.ranges:
        soils.extend(seed_to_soil.get_ranges(s))
        
    assert lines[idx].startswith("soil-to-fertilizer")
    idx += 1
    soil_to_fertilizer_lines = []
    while lines[idx].strip() != "":
        soil_to_fertilizer_lines.append(lines[idx])
        idx += 1
    soil_to_fertilizer = Map(soil_to_fertilizer_lines)
    idx += 1
    fertilizers = []
    for s in soils:
        fertilizers.extend(soil_to_fertilizer.get_ranges(s))
    
    assert lines[idx].startswith("fertilizer-to-water")
    idx += 1
    fertilizer_to_water_lines = []
    while lines[idx].strip() != "":
        fertilizer_to_water_lines.append(lines[idx])
        idx += 1
    fertilizer_to_water = Map(fertilizer_to_water_lines)
    idx += 1
    waters = []
    for f in fertilizers:
        waters.extend(fertilizer_to_water.get_ranges(f))
    
    assert lines[idx].startswith("water-to-light")
    idx += 1
    water_to_light_lines = []
    while lines[idx].strip() != "":
        water_to_light_lines.append(lines[idx])
        idx += 1
    water_to_light = Map(water_to_light_lines)
    idx += 1
    lights = []
    for w in waters:
        lights.extend(water_to_light.get_ranges(w))
    
    assert lines[idx].startswith("light-to-temperature")
    idx += 1
    light_to_temp_lines = []
    while lines[idx].strip() != "":
        light_to_temp_lines.append(lines[idx])
        idx += 1
    light_to_temp = Map(light_to_temp_lines)
    idx += 1
    temperatures = []
    for l in lights:
        temperatures.extend(light_to_temp.get_ranges(l))
    
    assert lines[idx].startswith("temperature-to-humidity")
    idx += 1
    temp_to_humidity_lines = []
    while lines[idx].strip() != "":
        temp_to_humidity_lines.append(lines[idx])
        idx += 1
    temp_to_humidity = Map(temp_to_humidity_lines)
    idx += 1
    humidities = []
    for t in temperatures:
        humidities.extend(temp_to_humidity.get_ranges(t))
    
    assert lines[idx].startswith("humidity-to-location")
    idx += 1
    humidity_to_location_lines = []
    while idx < len(lines) and lines[idx].strip() != "":
        humidity_to_location_lines.append(lines[idx])
        idx += 1
    humidity_to_location = Map(humidity_to_location_lines)
    locations = []
    for h in humidities:
        locations.extend(humidity_to_location.get_ranges(h))
    
    return min(locations).start

if __name__ == '__main__':
    assert run(Path("aoc-5-test.txt")) == 46
    print(run(Path("aoc-5.txt")))
