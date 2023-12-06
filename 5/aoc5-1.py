from pathlib import Path
from typing import List


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
        self.ranges = {}
        for line in ranges:
            offset, start, length = [int(num_str) for num_str in line.split(" ")]
            self.ranges[offset] = Range(start, start + length - 1)
    
    def __getitem__(self, item: int) -> int:
        for offset, r in self.ranges.items():
            if item in r:
                return offset + (item - r.start)
        return item
    

def run(fpath: Path) -> int:
    with fpath.open() as f:
        lines = f.readlines()
    
    idx = 0
    assert lines[idx].startswith("seeds:")
    seeds = [int(s) for s in lines[idx].split(": ")[1].split(" ")]
    idx += 2
    
    assert lines[idx].startswith("seed-to-soil")
    idx += 1
    seed_to_soil_lines = []
    while lines[idx].strip() != "":
        seed_to_soil_lines.append(lines[idx])
        idx += 1
    seed_to_soil = Map(seed_to_soil_lines)
    idx += 1
    
    assert lines[idx].startswith("soil-to-fertilizer")
    idx += 1
    soil_to_fertilizer_lines = []
    while lines[idx].strip() != "":
        soil_to_fertilizer_lines.append(lines[idx])
        idx += 1
    soil_to_fertilizer = Map(soil_to_fertilizer_lines)
    idx += 1
    
    assert lines[idx].startswith("fertilizer-to-water")
    idx += 1
    fertilizer_to_water_lines = []
    while lines[idx].strip() != "":
        fertilizer_to_water_lines.append(lines[idx])
        idx += 1
    fertilizer_to_water = Map(fertilizer_to_water_lines)
    idx += 1
    
    assert lines[idx].startswith("water-to-light")
    idx += 1
    water_to_light_lines = []
    while lines[idx].strip() != "":
        water_to_light_lines.append(lines[idx])
        idx += 1
    water_to_light = Map(water_to_light_lines)
    idx += 1
    
    assert lines[idx].startswith("light-to-temperature")
    idx += 1
    light_to_temp_lines = []
    while lines[idx].strip() != "":
        light_to_temp_lines.append(lines[idx])
        idx += 1
    light_to_temp = Map(light_to_temp_lines)
    idx += 1
    
    assert lines[idx].startswith("temperature-to-humidity")
    idx += 1
    temp_to_humidity_lines = []
    while lines[idx].strip() != "":
        temp_to_humidity_lines.append(lines[idx])
        idx += 1
    temp_to_humidity = Map(temp_to_humidity_lines)
    idx += 1
    
    assert lines[idx].startswith("humidity-to-location")
    idx += 1
    humidity_to_location_lines = []
    while idx < len(lines) and lines[idx].strip() != "":
        humidity_to_location_lines.append(lines[idx])
        idx += 1
    humidity_to_location = Map(humidity_to_location_lines)
    
    locations = [humidity_to_location[temp_to_humidity[
        light_to_temp[water_to_light[fertilizer_to_water[soil_to_fertilizer[seed_to_soil[seed]]]]]]] for seed in
                 seeds]

    return min(locations)

if __name__ == '__main__':
    assert run(Path("aoc-5-test.txt")) == 35
    print(run(Path("aoc-5.txt")))
