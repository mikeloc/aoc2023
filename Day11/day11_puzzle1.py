#
# Day 9 Puzzle 1
#
from enum import Enum
import sys

galaxyID = 1

class Pos:
    def __init__(self, posX, posY):
        self.posX = posX
        self.posY = posY
    def __eq__(self, other):
        return self.posX == other.posX and self.posY == other.posY
    

class Galaxy:
    def __init__(self, pos):
        global galaxyID
        self.pos = pos
        self.galaxyId = galaxyID
        galaxyID += 1
    

isEmptyRow = []
isEmptyColumn = []
map = []

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

def expandUniverse(sizeOfUniverse):
    for i in range(sizeOfUniverse.posX):
        isEmptyColumn.append(True)
    for i in range(sizeOfUniverse.posY):
        isEmptyRow.append(True)

    for galaxy in map:
        isEmptyColumn[galaxy.pos.posX] = False
        isEmptyRow[galaxy.pos.posY] = False

    # Expand horizontally
    posX = 0
    while posX < len(isEmptyColumn):
        if isEmptyColumn[posX] == True:
            # Anyhthing right from posX gets shifted
            for galaxy in map:
                if galaxy.pos.posX > posX:
                    galaxy.pos.posX += 1
            isEmptyColumn.insert(posX, True)
            posX += 1
        posX += 1
        
    # Expand vertically
    posY = 0
    while posY < len(isEmptyRow):
        if isEmptyRow[posY] == True:
            # Anyhthing  down from Y gets shifted
            for galaxy in map:
                if galaxy.pos.posY > posY:
                    galaxy.pos.posY += 1
            isEmptyRow.insert(posY, True)
            posY += 1
        posY += 1

    print("Expand")

    
def sumOfAllPaths():
    total = 0
    startGalaxyIdx = 0
    while startGalaxyIdx < len(map): 
        for destGalaxyIdx in range(startGalaxyIdx+1, len(map)):
            dist = abs(map[startGalaxyIdx].pos.posX - map[destGalaxyIdx].pos.posX) + abs(map[startGalaxyIdx].pos.posY - map[destGalaxyIdx].pos.posY)
            total += dist
 #           print("Distance between", map[startGalaxyIdx].galaxyId, "and", map[destGalaxyIdx].galaxyId, "is:", dist )
        startGalaxyIdx += 1
#        print()
    return total

#
# Main
#

sizeOfUniverse = loadInputFile()
sizeOfUniverse = expandUniverse(sizeOfUniverse)
count = sumOfAllPaths()

print("Done count is ", count)
