#
# Day 9 Puzzle 1
#
from enum import Enum
import sys

class Pipes:
    def __init__(self, char):
        self.char = char
        self.inLoop = False
        self.insideLoop = False

    def __str__(self):
#        match self.char:
#            case 'F':
#                return "\u250F"
#            case 'J':
#                return "\u251B"
#            case "L":
#                return "\u2517"
#            case "7":
#                return "\u2513"
#            case "|":
#                return "\u2503"
#            case "-":
#                return "\u2501" 
        return self.char

class Pos:
    def __init__(self, posX, posY):
        self.posX = posX
        self.posY = posY
    def __eq__(self, other):
        return self.posX == other.posX and self.posY == other.posY

    def up(self):
        return Pos(self.posX, self.posY-1)
    def right(self):
        return Pos(self.posX+1, self.posY)
    def down(self):
        return Pos(self.posX, self.posY+1)
    def left(self):
        return Pos(self.posX-1, self.posY)

class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3
    START = 4

map = []
start = Pos(0,0)
total = 0

def loadFile():
    file = open('Day10/input4.txt', 'r')
    lines = file.readlines()
    posY = 0
    for line in lines:
        map.append([])
        posX = 0
        for char in line.strip():
            map[posY].append(Pipes(char))
            if (posX==11) and (posY==76):
                print("toto")
            if char == 'S':
                startPos = Pos(posX, posY)
            posX += 1
        posY += 1
    return startPos

def findNextStep(curStep, direction):
    if map[curStep.posY][curStep.posX].char == "7":
        if direction == direction.RIGHT:
            return curStep.down(), Direction.DOWN
        elif direction == Direction.UP:
            return curStep.left(), Direction.LEFT
        else:
            print("error", curStep, direction)
    
    if map[curStep.posY][curStep.posX].char == "F":
        if direction == direction.LEFT:
            return curStep.down(), Direction.DOWN
        elif direction == Direction.UP:
            return curStep.right(), Direction.RIGHT
        else:
            print("error", curStep, direction)

    if map[curStep.posY][curStep.posX].char == "J":
        if direction == direction.RIGHT:
            return curStep.up(), Direction.UP
        elif direction == Direction.DOWN:
            return curStep.left(), Direction.LEFT
        else:
            print("error", curStep, direction)

    if map[curStep.posY][curStep.posX].char == "L":
        if direction == direction.LEFT:
            return curStep.up(), Direction.UP
        elif direction == Direction.DOWN:
            return curStep.right(), Direction.RIGHT
        else:
            print("error", curStep, direction)

    if map[curStep.posY][curStep.posX].char == "-":
        if direction == direction.RIGHT:
            return curStep.right(), Direction.RIGHT
        elif direction == Direction.LEFT:
            return curStep.left(), Direction.LEFT
        else:
            print("error", curStep, direction)

    if map[curStep.posY][curStep.posX].char == "|":
        if direction == direction.UP:
            return curStep.up(), Direction.UP
        elif direction == Direction.DOWN:
            return curStep.down(), Direction.DOWN
        else:
            print("error", curStep, direction)

    if direction == Direction.START:
        upPos = start.up()
        if (map[upPos.posY][upPos.posX].char in '7F|'):
            return upPos, Direction.UP
        
        rightPos = start.right()
        if ( map[rightPos.posY][rightPos.posX].char in 'J7-'):
            return rightPos, Direction.RIGHT

        downPos = start.down()
        if (map[downPos.posY][downPos.posX].char in 'JL|'):
            return downPos, Direction.DOWN

        leftPos = start.left()
        if (map[leftPos.posY][leftPos.posX].char in 'FL-'):
            return leftPos, Direction.LEFT

listPos = []
start = loadFile()
listPos.append(start)
current,direction = findNextStep(start, Direction.START)
while current != start:
    listPos.append(current)
    current,direction = findNextStep(current,direction)

for pos in listPos:
    map[pos.posY][pos.posX].inLoop = True

count = 0
for i in range(len(map)):
    insideLoop = False
    if map[i][0].inLoop:
       insideLoop=True

    for j in range(1,len(map[i])):
        if insideLoop and not map[i][j].inLoop and map[i][j].char != '-':
            insideLoop = False
        elif not insideLoop and map[i][j].inLoop and map[i][j].char != '-':
            insideLoop = True
        else:
            if not map[i][j].inLoop:
                map[i][j].insideLoop = insideLoop

            if map[i][j].insideLoop:
                count += 1

for i in range(len(map)):
    sys.stdout.write("%03d " % (i,))
    for j in range(len(map[i])):
        if start.posX == j and start.posY == i:
            sys.stdout.write("\033[31m"+"S")
        else:
            if map[i][j].inLoop:
                sys.stdout.write("\033[33m"+str(map[i][j]))
            else:
                if map[i][j].insideLoop:
                    sys.stdout.write("\033[22m"+str(map[i][j]))
                else:
                    sys.stdout.write("\033[94m"+str(map[i][j]))
    print(" ")

   
print(count)