#
# Day 6 Puzzle 2
#
file = open('Day6/input2.txt', 'r')
Lines = file.readlines()

#Read total times
time_str = Lines[0].split(':')[1]
times = time_str.split()
totalTime = times[0]
for i in range(1,len(times)):
    totalTime = totalTime+times[i]
totalTime = int(totalTime)

#Read total distances
dist_str = Lines[1].split(':')[1]
distances = dist_str.split()
totalDistance = distances[0]
for i in range(1,len(distances)):
    totalDistance = totalDistance + distances[i]
totalDistance = int(totalDistance)

def isWinner(waitTime):
    return(totalTime-waitTime)*waitTime > totalDistance

def binary_search(lower, higher, searchWinner):
    if (higher-lower) > 1:
        midway = lower +(higher-lower)//2
        if isWinner(midway) == searchWinner:
            return binary_search(lower,midway,searchWinner)
        else:
            return binary_search(midway,higher,searchWinner)
    else:
        return higher

step = totalTime // 10
firstWin = -1
lastWin = -1

waitTime=0
while (waitTime < totalTime):
    if isWinner(waitTime):
        if firstWin == -1:
            firstWin = waitTime
    else:
        if firstWin != -1:
            lastWin = waitTime-step
            break
    waitTime = waitTime + step
firstWin = binary_search(0, firstWin, searchWinner=True)
lastWin = binary_search(lastWin,totalTime, searchWinner=False)-1
print("firstWin:",firstWin,"lastWin:",lastWin)
print("winning combinations:",lastWin-firstWin+1)