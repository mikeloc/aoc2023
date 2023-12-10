#
# Day 9 Puzzle 1
#
from enum import Enum

def allZeros(data):
    for i in range(len(data)):
        if data[i] != 0:
            return False
    return True

file = open('Day9/input1.txt', 'r')
lines = file.readlines()
total = 0

for line in lines:
    i=0
    data = []
    data.append([])
    string_numbers = line.strip().split()
    for index in range(len(string_numbers)):
        data[i].append(int(string_numbers[index]))

    while not allZeros(data[i]):
        i += 1
        data.append([])    
        for index in range(len(data[i-1])-1):
            data[i].append(data[i-1][index+1] - data[i-1][index])

    data[i].append(0)
    i -= 1
    while i >= 0:
        data[i].append(data[i][-1] + data[i+1][-1])
        i -= 1
    total += data[0][-1]    
print(total)