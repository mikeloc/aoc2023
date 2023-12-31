#
# Day 3 Puzzle 1
#

class Positions:
  def __init__(self, posX, posY, size, num):
    self.posX = posX
    self.posY = posY
    self.size = size
    self.num = num


def adjacent(number, symbol):
    deltaX=0
    deltaY=0
    if symbol.posX > number.posX:
        deltaX = symbol.posX - number.posX - number.size + 1
    else:
        deltaX = number.posX - symbol.posX
    
    if symbol.posY > number.posY:
        deltaY = symbol.posY - number.posY
    else:
        deltaY = number.posY - symbol.posY
    return deltaX <= 1 and deltaY <= 1


total = 0
symbols = '!@#$%^&*()_+-=/'
digits = '0123456789'

file = open('Day3/input2.txt', 'r')
Lines = file.readlines()

symbolsFound = []
numbersFound = []

numberInProgress = False
currentNumber = 0
currentNumDigits = 0

YPos = 0
for line in Lines:
    XPos = 0
    for char in line:
        if char in digits:
            if not numberInProgress:
              numberInProgress = True
              currentNumber = int(char)
              currentNumDigits = 1
            else:
              currentNumber = currentNumber * 10 + int(char)
              currentNumDigits = currentNumDigits + 1
        else:
            if char in symbols:
                symbolsFound.append(Positions(XPos,YPos,1,-1))
            elif char != '.':
                  print("*************************  Found  ", char, "   *************************")

            if numberInProgress:
                numbersFound.append(Positions(XPos-currentNumDigits,YPos,currentNumDigits,currentNumber))
                print("Found number ", currentNumber, "  of size ", currentNumDigits, " at position ", XPos-currentNumDigits,",", YPos  )

                numberInProgress = False
                currentNumber = 0
                currentNumDigits = 0
                  
        XPos = XPos+1
    # Find all symbols and record postion
    YPos = YPos + 1

# Sum numbers which have at least one adjcacent symbols
for number in numbersFound:
   for symbol in symbolsFound:
        if adjacent(number,symbol):
            total = total + number.num
            break

print("total: ", total )