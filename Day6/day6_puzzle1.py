#
# Day 6 Puzzle 1
#
total = 1

file = open('Day6/input2.txt', 'r')
Lines = file.readlines()

time_str = Lines[0].split(':')[1]
times = time_str.split()
for i in range(0,len(times)):
    times[i] = int(times[i])

dist_str = Lines[1].split(':')[1]
distances = dist_str.split()
for i in range(0,len(distances)):
    distances[i] = int(distances[i])

numRaces = len(distances)
for i in range(0,numRaces):
    win = 0
    for waitTime in range(0, times[i]):
        if (times[i]-waitTime)*waitTime > distances[i]:
            win = win+1
    print("Race",i,"winning combination",win)
    total = total * win
print("total:", total)