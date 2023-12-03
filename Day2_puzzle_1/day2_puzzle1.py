# Python code to
# demonstrate readlines()
total = 0


numRed = 12
numGreen = 13
numBlue = 14

 # Using readlines()
file1 = open('Day2_puzzle_1/input2.txt', 'r')
Lines = file1.readlines()
 
# Strips the newline character
for line in Lines:
    splitGameIdAndGamesData = line.split(':')
    gameAndId = splitGameIdAndGamesData[0].split()

    # Get gameId
    gameId = int(gameAndId[1])
    print(gameId)

    keepGame = True
    gamesData = splitGameIdAndGamesData[1].split(';')
    for game in gamesData:
        picks = game.split(',')
        for pick in picks:
            splitNumAndColor = pick.split()
            num = int(splitNumAndColor[0])
            color = splitNumAndColor[1]

            match color:
                case 'blue':
                    if num > numBlue:
                        keepGame = False
                case 'green':
                    if num > numGreen:
                       keepGame = False
                case 'red':
                    if num > numRed:
                        keepGame = False
    if keepGame:
        total = total + gameId
        print("keeping game ", gameId)

print("total: ", total )        




