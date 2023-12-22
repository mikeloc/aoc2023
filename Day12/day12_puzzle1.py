
# Day 12 Puzzle 1
#
from enum import Enum
import sys

def winning(mask, summary):
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
        a = combinations(setFirstUnkTo(mask,"."),summary)
        b = combinations(setFirstUnkTo(mask,"#"), summary)
        return a+b

# Main
#
file = open('Day12/input2.txt', 'r')
lines = file.readlines()
total = 0
lineCount = 0 
for line in lines:
    print(line)

    splitMaskAndSummary = line.strip().split()
    mask = splitMaskAndSummary[0]
    
    summary = []
    for i in splitMaskAndSummary[1].split(","):
        summary.append(int(i))

    line_total = 0
    
    line_total = combinations(mask,summary)
    print("Line Total", line_total)
    total += line_total
    lineCount += 1
print("TOTAL:", total)
