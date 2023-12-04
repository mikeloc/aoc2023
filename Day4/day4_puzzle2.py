#
# Day 4 Puzzle 1
#
file = open('Day4_puzzle_2/input2.txt', 'r')
Lines = file.readlines()
cardData = [0]

# Polutate cardId for all card starting with 1 card for each
for line in Lines:
    line = line.rstrip('\n')
    splitCardIdAndNumbers = line.split(":")
    cardId = int(splitCardIdAndNumbers[0].split()[1])
    cardData.insert(cardId, 1)

for line in Lines:
    line = line.rstrip('\n')
    splitCardIdAndNumbers = line.split(":")
    cardId = int(splitCardIdAndNumbers[0].split()[1])
    splitWinningAndCardNumbers = splitCardIdAndNumbers[1].split("|")
    winningNumbers = splitWinningAndCardNumbers[0].split()
    cardNumbers = splitWinningAndCardNumbers[1].split()

    cardPoint = 0
    for cardNumber in cardNumbers:
        if cardNumber in winningNumbers:
            cardPoint = cardPoint + 1
    
    # X cardPoints means the next X card will add the
    for i in range(cardId+1,cardId+cardPoint+1): 
        cardData[i] = cardData[i] + cardData[cardId]

total = 0
for cardPoints in cardData:
    total = total+cardPoints
 
print("total: ", total )