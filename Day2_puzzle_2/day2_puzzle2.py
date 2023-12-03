# Python code to
# demonstrate readlines()
total = 0

 # Using readlines()
file1 = open('Day2_puzzle_2/input2.txt', 'r')
Lines = file1.readlines()

# Strips the newline character
for line in Lines:
    minRed = 0
    minGreen = 0
    minBlue = 0

    splitGameIdAndGamesData = line.split(':')
    gameAndId = splitGameIdAndGamesData[0].split()
    gameId = int(gameAndId[1])
    print(gameId)

    games = splitGameIdAndGamesData[1].split(';')
    for game in games:
        picks = game.split(',')
        for pick in picks:
            splitNumAndColor = pick.split()
            num = int(splitNumAndColor[0])
            color = splitNumAndColor[1]

            match color:
                case 'blue':
                    if num > minBlue:
                        minBlue = num
                case 'green':
                    if num > minGreen:
                       minGreen = num
                case 'red':
                    if num > minRed:
                        minRed = num
    total = total + minRed * minGreen * minBlue
print("total: ", total )        




