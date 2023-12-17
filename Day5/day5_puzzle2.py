#
# Day 5 Puzzle 2
#
import sys

file = open('Day5/input2.txt', 'r')
Lines = file.readlines()
file_len = len(Lines)


class Range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class MapRow:
  def __init__(self, dstStart, srcStart, num):
    self.dstStart = dstStart
    self.srcStart = srcStart
    self.num = num
  def get_dest(self, source):
      return self.dstStart + source - self.srcStart

def readMap(mapName,map,lineCounter):
    found = False
    while (not found and lineCounter < file_len):
        if mapName in Lines[lineCounter]:
            found = True
        lineCounter = lineCounter + 1
    done = False
    while (not done and lineCounter < file_len):
        row = Lines[lineCounter].split()
        if len(row) != 3:
            done = True
        else:
            dest = int(row[0])
            src = int(row[1])
            range = int(row[2])
            entry = MapRow(dest,src,range)
            
            mapAdded = False
            i=0
            while i<len(map) and not mapAdded:
                if ( map[i].srcStart > src):
                    map.insert(i, entry)
                    mapAdded = True
                else:
                    i += 1
            if not mapAdded:
                map.append(entry)

        lineCounter = lineCounter + 1

    # Fill unmapped regions
    i=0
    src = 0
    while i<len(map):
        if src < map[i].srcStart:
            entry = MapRow(src, src, map[i].srcStart - src)
            map.insert(i,entry)
        src = map[i].srcStart + map[i].num
        i += 1

    src = map[i-1].srcStart+map[i-1].num        
    entry = MapRow(src,src,99999999999999999999)
    map.append(entry)

    return lineCounter


def searchMap(srcList, map):
    destList = []
    for src in srcList:
        i=0
        while src.start > map[i].srcStart + map[i].num - 1:
            i += 1

        destStart = map[i].get_dest(src.start)
        # Found lower end of the range in i, check upper end
        if src.end <= map[i].srcStart + map[i].num - 1:
            destEnd = map[i].get_dest(src.end)
            destList.append(Range(destStart,destEnd))
            i += 1
        else:
            destEnd =  map[i].dstStart + map[i].num -1
            destList.append(Range(destStart,destEnd))
            i += 1

        while i < len(map) and src.end > map[i].srcStart + map[i].num - 1:
            # map whole range and increase i
            destStart = map[i].dstStart
            destEnd = map[i].dstStart + map[i].num
            destList.append(Range(destStart,destEnd))
            i += 1

        # map beginning of range to dest
        if i < len(map) and src.end > map[i].srcStart:
            destStart = map[i].dstStart
            destEnd = map[i].get_dest(src.end) 
            destList.append(Range(destStart,destEnd))
            
    return destList

def dumpRanges(rangeList, name):
    sys.stdout.write(name)
    for range in rangeList:
        sys.stdout.write(str(range.start) + " ... " + str(range.end) + "    " )
    sys.stdout.write("\n")


seed_to_soil_map = []
soil_to_fertilizer_map = []
fertilizer_to_water_map = []
water_to_light_map = []
light_to_temperature_map = []
temperature_to_humidity_map = []
humidity_to_location_map = []
lowestLocation = 99999999999999999999

lineCounter = 0
# Read seeds
seeds = Lines[lineCounter].strip("seeds:").split()
lineCounter = lineCounter + 1
for i in range(0,len(seeds)):
    seeds[i] = int(seeds[i])

# Read all maps
readMap("seed-to-soil map",seed_to_soil_map, lineCounter)
lineCounter = readMap("soil-to-fertilizer map",soil_to_fertilizer_map, lineCounter)
lineCounter = readMap("fertilizer-to-water map",fertilizer_to_water_map, lineCounter)
lineCounter = readMap("water-to-light map",water_to_light_map, lineCounter)
lineCounter = readMap("light-to-temperature map",light_to_temperature_map, lineCounter)
lineCounter = readMap("temperature-to-humidity map",temperature_to_humidity_map, lineCounter)
lineCounter = readMap("humidity-to-location map",humidity_to_location_map, lineCounter)


len_seeds = len(seeds)
seed_index = 0
while seed_index < len_seeds:
    seedStart = seeds[seed_index]
    seedEnd = seedStart+seeds[seed_index+1]-1      
    seed_index = seed_index + 2

    seed = []
    seed.append(Range(seedStart, seedEnd))

    print("seed range", seedStart, "...", seedEnd)
    soil = searchMap(seed, seed_to_soil_map)
    dumpRanges(soil, "soil:")
    fertilizer = searchMap(soil, soil_to_fertilizer_map)
    dumpRanges(fertilizer,"fertilizer:")
    water = searchMap(fertilizer, fertilizer_to_water_map)
    dumpRanges(water,"water:")
    light = searchMap(water, water_to_light_map)
    dumpRanges(light,"light:")
    temperature = searchMap(light, light_to_temperature_map)
    dumpRanges(temperature,"temperature:")
    humidity = searchMap(temperature, temperature_to_humidity_map)
    dumpRanges(humidity,"humidity:")
    location = searchMap(humidity, humidity_to_location_map)
    dumpRanges(location,"location:")

    for loc in location: 
        if (loc.start < lowestLocation):
            lowestLocation = loc.start
            print("New lowest location:", lowestLocation)

    print("\n\n")

print("Lowest Location: ",  lowestLocation )