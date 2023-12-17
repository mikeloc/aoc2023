#
# Day 9 Puzzle 1
#
from enum import Enum
import sys

nice = True
class Pipes:
    def __init__(self, char):
        self.char = char
        self.inLoop = False
        self.insideLoop = True

    def __str__(self):
        if nice:
            match self.char:
                case 'F':
                    return "\u250F"
                case 'J':
                     return "\u251B"
                case "L":
                    return "\u2517"
                case "7":
                    return "\u2513"
                case "|":
                    return "\u2503"
                case "-":
                    return "\u2501" 
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

def loadFile():
    file = open('Day10/input2.txt', 'r')
    lines = file.readlines()
    posY = 0
    for line in lines:
        map.append([])
        posX = 0
        for char in line.strip():
            map[posY].append(Pipes(char))
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

def getStartPointPipe(first, last):
    if first == Direction.UP:
        if last == Direction.LEFT:
            return "L"
        elif last == Direction.UP:
            return "|"
        elif last == Direction.RIGHT:
            return 'J'
    elif first == Direction.DOWN:
        if last == Direction.DOWN:
            return "|"
        elif last == Direction.LEFT:
            return 'F'
        elif last == Direction.RIGHT:
            return '7'
    elif first == Direction.RIGHT:
        if last == Direction.UP:
            return 'F'
        elif last == Direction.DOWN:
            return 'L'
        elif last == Direction.RIGHT:
            return '-'
    elif first == Direction.LEFT:
        if last == Direction.UP:
            return '7'
        elif last == Direction.DOWN:
            return 'J'
        elif last == Direction.LEFT:
            return '-'

def findLoop(start):
    listPos = []
    listPos.append(start)
    current,direction = findNextStep(start, Direction.START)
    start_direction = direction
    while current != start:
        listPos.append(current)
        current,direction = findNextStep(current,direction)
    end_direction = direction
    S_pipe = getStartPointPipe(start_direction,end_direction)
    print("Number of pipes in loop", len(listPos))
    for pos in listPos:
        map[pos.posY][pos.posX].inLoop = True
    return S_pipe

def findPipesInsideLoop(S_pipe):
    map[start.posY][start.posX].char = S_pipe
    count = 0
    for i in range(0,len(map)):
        inside = False
        lastCorner = ""
        for j in range(len(map[i])):
            if not map[i][j].inLoop:
                if inside:
                    count += 1
                map[i][j].insideLoop = inside
            else:
                if map[i][j].char == 'F':
                    inside = not inside
                    lastCorner = 'F'
            
                if map[i][j].char == '7':
                    if (lastCorner == 'F'):
                        inside = not inside
                    lastCorner = '7'

                if map[i][j].char == 'J':
                    if (lastCorner == 'L'):
                        inside = not inside
                    lastCorner = 'J'

                if map[i][j].char == 'L':
                    inside = not inside
                    lastCorner = 'L'

                if map[i][j].char == "|":
                    inside = not inside
    map[start.posY][start.posX].char = 'S'
    return count
            
def printMap():
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
                        sys.stdout.write("\033[31m"+str(map[i][j]))
                    else:
                        sys.stdout.write("\033[94m"+str(map[i][j]))
        print(" ")

#
# Main
#
start = loadFile()
S_pipe = findLoop(start)
count = findPipesInsideLoop(S_pipe)
nice = False
printMap()
print("Count inside:", count, "\n\n")