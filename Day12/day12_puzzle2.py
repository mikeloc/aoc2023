
# Day 12 Puzzle 1
#
from enum import Enum
import sys

countWin = 0
cache = {}

class cacheEntry:
    def __init__(self, mask, summary):
        self.mask = mask
        for s in summary:
            self.mask = self.mask + "_" + str(s)

    def __eq__(self, other):
        return self.mask == other.mask
    
    def __str__(self):
        return self.mask
    
def winning(mask, summary):
    global countWin
    if mask == ".###..##.#.#":
        print("Stop")
    newMask = mask.split(".")
    i=0
    foundError = False
    for m in newMask:
        if i < len(summary) and "#" in m:
            if summary[i] != len(m):
                return False
            i += 1
        else:
            if "#" in m:
                return False
    if ( i == len(summary)):
        countWin += 1
        print(countWin)    
    return i == len(summary)  
 
def setFirstUnkTo(mask, char):
    
    for i in range(len(mask)):
        if mask[i] == "?":
            mask = mask[:i] + char + mask[i + 1:]
            return mask
    return mask


def combinations(mask, summary):
    if not "?" in mask:
        if winning(mask,summary):
            return 1
        else:
            return 0
    else:
        key = cacheEntry(mask,summary)
        if str(key) in cache:

            return cache[str(key)]
        else:
            newMaskA = setFirstUnkTo(mask,".")
            a = combinations(newMaskA,summary)
            key = cacheEntry(newMaskA,summary)
            cache[str(key)] = a

            newMaskB = setFirstUnkTo(mask,"#")
            key = cacheEntry(newMaskB,summary)
            b = combinations(newMaskB, summary)
            cache[str(key)] = b

            return a+b

# Main
#
file = open('Day12/input3.txt', 'r')
lines = file.readlines()
total = 0
lineCount = 0 
for line in lines:
    print(line)

    splitMaskAndSummary = line.strip().split()
    mask = splitMaskAndSummary[0].split(".")
    
    summary = []
    for i in splitMaskAndSummary[1].split(","):
        summary.append(int(i))

#          14              5
        
#     ##??????????#?     ????#   9,2,1,2
#     9,2,1,2                       -                       
#     9,2,1                2        ok
#     9,2                 1,2       ok
#     9                     
        
        2    
        
    newMask = []
    for i in mask:
        if i != "":
            newMask.append(i)
    
    for splitPoint in range(len(summary)):
        left = newMask[:splitPoint]
        right = newMask[splitPoint:]
        

        
        




    

    line_total = 0
    line_total = combinations(mask,summary)
    print("Line Total", line_total)
    total += line_total
    lineCount += 1
print("TOTAL:", total)
