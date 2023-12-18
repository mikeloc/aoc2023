#
# Day 11 Puzzle 2
#
from enum import IntEnum

galaxyID = 1

class Dimension(IntEnum):
    VERTICAL = 0
    HORIZONTAL = 1

class EmptySpace:
    def __init__(self):
        self.map=[]
        self.map.append(Dimension.VERTICAL)
        self.map.append(Dimension.HORIZONTAL)
        self.map[Dimension.VERTICAL] = []
        self.map[Dimension.HORIZONTAL] = []

class Pos:
    def __init__(self, posX, posY):
        self.coord = []
        self.coord.append(Dimension.VERTICAL)
        self.coord.append(Dimension.HORIZONTAL)
        self.coord[Dimension.HORIZONTAL] = posX
        self.coord[Dimension.VERTICAL] = posY

class Galaxy:
    def __init__(self, pos):
        global galaxyID
        self.pos = pos
        self.galaxyId = galaxyID
        galaxyID += 1

map = []
emptySpace = EmptySpace()

def loadInputFile():
    file = open('Day11/input2.txt', 'r')
    lines = file.readlines()
    posY = 0
    for line in lines:
        posX = 0
        for char in line.strip():
            if char == "#":
                map.append(Galaxy(Pos(posX,posY)))
            posX += 1
        posY += 1
    return Pos(posX,posY)


def findEmpty(dimension):
    for i in range (sizeOfUniverse.coord[dimension]):
        found = False
        for galaxy in map:
            if galaxy.pos.coord[dimension] == i:
                found = True
                break
        if not found:
            emptySpace.map[dimension].append(i)

def expand(dimension):
    for galaxy in map:
        numExpansion = 0
        i=0
        while i < len(emptySpace.map[dimension]) and galaxy.pos.coord[dimension] > emptySpace.map[dimension][i]:
            i += 1
            numExpansion += 1
        galaxy.pos.coord[dimension] = galaxy.pos.coord[dimension] + numExpansion * 999999

def expandUniverse(sizeOfUniverse):
    # Vertical expansion
    findEmpty(Dimension.VERTICAL)
    expand(Dimension.VERTICAL)
    #Horizontal expansion
    findEmpty(Dimension.HORIZONTAL)
    expand(Dimension.HORIZONTAL)

def sumOfAllPaths():
    total = 0
    startGalaxyIdx = 0
    while startGalaxyIdx < len(map):
        for destGalaxyIdx in range(startGalaxyIdx+1, len(map)):
            dist = abs(map[startGalaxyIdx].pos.coord[Dimension.HORIZONTAL] - map[destGalaxyIdx].pos.coord[Dimension.HORIZONTAL]) + \
                abs(map[startGalaxyIdx].pos.coord[Dimension.VERTICAL] - map[destGalaxyIdx].pos.coord[Dimension.VERTICAL])
            total += dist
        startGalaxyIdx += 1
    return total

#
# Main
#
sizeOfUniverse = loadInputFile()
sizeOfUniverse = expandUniverse(sizeOfUniverse)
count = sumOfAllPaths()

print("Done count is ", count)