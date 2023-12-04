#
# Day 4 Puzzle 1
#

file = open('Day4/input2.txt', 'r')
Lines = file.readlines()

total = 0
for line in Lines:
    line = line.rstrip('\n')
    splitCardIdAndNumbers = line.split(":")
    splitWinningAndCardNumbers = splitCardIdAndNumbers[1].split("|")
    winningNumbers = splitWinningAndCardNumbers[0].split()
    cardNumbers = splitWinningAndCardNumbers[1].split()

    cardPoint = 0 
    for cardNumber in cardNumbers:
        if cardNumber in winningNumbers:
            if cardPoint == 0:
                cardPoint = 1
            else:
                cardPoint = cardPoint * 2
    total = total + cardPoint
print("total: ", total )