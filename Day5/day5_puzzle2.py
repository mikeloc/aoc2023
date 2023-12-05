#
# Day 5 Puzzle 2
#

file = open('Day5/input2.txt', 'r')
Lines = file.readlines()
file_len = len(Lines)

class Range:
  def __init__(self, dstStart, srcStart, num):
    self.dstStart = dstStart
    self.srcStart = srcStart
    self.num = num

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
            entry = Range(dest,src,range)
            map.append(entry)
        lineCounter = lineCounter + 1
    return lineCounter

def searchMap(src, map):
    for mapEntry in map:
        if src >= mapEntry.srcStart and src < mapEntry.srcStart + mapEntry.num:
            return mapEntry.dstStart + src - (mapEntry.srcStart)
    return src

seed_to_soil_map = []
soil_to_fertilizer_map = []
fertilizer_to_water_map = []
water_to_light_map = []
light_to_temperature_map = []
temperature_to_humidity_map = []
humidity_to_location_map = []
LowestLocation = 99999999999999999999

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
    print("seed range", seedStart, "...", seedEnd)
    count = 0
    for seed in range(seedStart,seedEnd):
        soil = searchMap(seed, seed_to_soil_map)
        fertilizer = searchMap(soil, soil_to_fertilizer_map)
        water = searchMap(fertilizer, fertilizer_to_water_map)
        light = searchMap(water, water_to_light_map)
        temperature = searchMap(light, light_to_temperature_map)
        humidity = searchMap(temperature, temperature_to_humidity_map)
        location = searchMap(humidity, humidity_to_location_map)
        count = count+1
        if (count % 1000000 == 0):
            print(seed)
#            print("Seed:", seed, "soil", soil, "fertilizer", fertilizer, "water", water, "light",light, "temperature",temperature, "humidity", humidity, "location", location )

        if (location < LowestLocation):
            LowestLocation = location

print("Lowest Location: ",  LowestLocation )