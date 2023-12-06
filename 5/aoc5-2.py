from pathlib import Path
from typing import Dict, List


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


class Map:
    def __init__(self, ranges: List[str]):
        self.ranges: Dict[int, Range] = {}
        for line in ranges:
            offset, start, length = [int(num_str) for num_str in line.split(" ")]
            self.ranges[offset] = Range(start, start + length - 1)
    
    def __getitem__(self, item: int) -> int:
        for offset, r in self.ranges.items():
            if item in r:
                return offset + (item - r.start)
        return item


class InvMap:
    def __init__(self, ranges: List[str]):
        self.ranges: Dict[int, Range] = {}
        for line in ranges:
            start, offset, length = [int(num_str) for num_str in line.split(" ")]
            self.ranges[offset] = Range(start, start + length - 1)
    
    def __getitem__(self, item: int) -> int:
        for offset, r in self.ranges.items():
            if item in r:
                return offset + (item - r.start)
        return item


class Seeds:
    def __init__(self, line: str):
        seed_values = line.split(" ")
        self.ranges: List[Range] = []
        for start, length in zip(seed_values[::2], seed_values[1::2]):
            self.ranges.append(Range(int(start), int(start) + int(length)))
    
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
    soil_to_seed = InvMap(seed_to_soil_lines)
    idx += 1
    
    assert lines[idx].startswith("soil-to-fertilizer")
    idx += 1
    soil_to_fertilizer_lines = []
    while lines[idx].strip() != "":
        soil_to_fertilizer_lines.append(lines[idx])
        idx += 1
    fertilizer_to_soil = InvMap(soil_to_fertilizer_lines)
    idx += 1
    
    assert lines[idx].startswith("fertilizer-to-water")
    idx += 1
    fertilizer_to_water_lines = []
    while lines[idx].strip() != "":
        fertilizer_to_water_lines.append(lines[idx])
        idx += 1
    water_to_fertilizer = InvMap(fertilizer_to_water_lines)
    idx += 1
    
    assert lines[idx].startswith("water-to-light")
    idx += 1
    water_to_light_lines = []
    while lines[idx].strip() != "":
        water_to_light_lines.append(lines[idx])
        idx += 1
    light_to_water = InvMap(water_to_light_lines)
    idx += 1
    
    assert lines[idx].startswith("light-to-temperature")
    idx += 1
    light_to_temp_lines = []
    while lines[idx].strip() != "":
        light_to_temp_lines.append(lines[idx])
        idx += 1
    temp_to_light = InvMap(light_to_temp_lines)
    idx += 1
    
    assert lines[idx].startswith("temperature-to-humidity")
    idx += 1
    temp_to_humidity_lines = []
    while lines[idx].strip() != "":
        temp_to_humidity_lines.append(lines[idx])
        idx += 1
    humidity_to_temp = InvMap(temp_to_humidity_lines)
    idx += 1
    
    assert lines[idx].startswith("humidity-to-location")
    idx += 1
    humidity_to_location_lines = []
    while idx < len(lines) and lines[idx].strip() != "":
        humidity_to_location_lines.append(lines[idx])
        idx += 1
    location_to_humidity = InvMap(humidity_to_location_lines)
    
    location = 0
    seed = soil_to_seed[fertilizer_to_soil[water_to_fertilizer[light_to_water[temp_to_light[humidity_to_temp[location_to_humidity[location]]]]]]]
    while seed not in seeds:
        location += 1
        seed = soil_to_seed[fertilizer_to_soil[water_to_fertilizer[light_to_water[temp_to_light[humidity_to_temp[location_to_humidity[location]]]]]]]
        print(location, "->", seed)
    
    return location

if __name__ == '__main__':
    assert run(Path("aoc-5-test.txt")) == 46
    print(run(Path("aoc-5.txt")))
