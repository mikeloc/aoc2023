#
# Day 8 Puzzle 2
#
from enum import Enum
import math

directions=[]
nodes={}

class Direction(Enum):
    LEFT = 0
    RIGHT = 1

class Node:
    def __init__(self,left,right):
        self.left = left
        self.right = right

file = open('Day8/input2.txt', 'r')
Lines = file.readlines()

# Load directions 
for dirChar in Lines[0].strip():
    if dirChar == 'L':
        directions.append(Direction.LEFT)
    elif dirChar == 'R':
        directions.append(Direction.RIGHT)
    else:
        print("ERROR - invalid direction")
        exit

# Load Nodes
for i in range(1,len(Lines)):
    str = Lines[i].strip()
    if str:
        trans = str.maketrans('','','=(),')
        str = str.translate(trans).split()
        nodeId = str[0]
        left = str[1]
        right = str[2]
        nodes[nodeId] = Node(left, right)        
    else:
        continue

dir_index = 0 
totalStep = 0
found = False
cycles = []
nodeList = []
for key,node in nodes.items():
    if 'A' in key:
        nodeList.append(key)

for node in nodeList:
    current = nodes[node]
    found = False
    stepCount = 0
    while not found:
        if (directions[dir_index] == Direction.LEFT):
            next = current.left
        else:
            next = current.right 
        stepCount += 1
        dir_index += 1
        if dir_index == len(directions):
            dir_index = 0
        if 'Z' in next:
            found = True
            cycles.append(stepCount)
        else:
            current = nodes[next]
for cycle in cycles:
    print(cycle)

totalStep = math.lcm(*cycles)
print("totalStep",totalStep)