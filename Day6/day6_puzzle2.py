#
# Day 6 Puzzle 2
#
file = open('Day6/input2.txt', 'r')
Lines = file.readlines()

time_str = Lines[0].split(':')[1]
times = time_str.split()
totalTime = times[0]
for i in range(1,len(times)):
    totalTime = totalTime+times[i]
totalTime = int(totalTime)

dist_str = Lines[1].split(':')[1]
distances = dist_str.split()
totalDistance = distances[0]
for i in range(1,len(distances)):
    totalDistance = totalDistance + distances[i]
totalDistance = int(totalDistance)

firstWin = False
lastWin = False
win = 0
for waitTime in range(0, totalTime):
    if (totalTime-waitTime)*waitTime > totalDistance:
        if not firstWin:
            print("firstWin:", waitTime)
            firstWin=True
        win = win+1
    else:
        if firstWin and not lastWin:
            print("lastWin", waitTime)
            lastWin = False
            break
print("winning combination",win)