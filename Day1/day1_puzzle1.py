# 
# Day 1 puzzle 1
# 

file = open('Day1/input2.txt', 'r')
Lines = file.readlines()
digits = "0123456789"

count = 0
# Strips the newline character
for line in Lines:
    firstFound = False
    firstNum = 0
    lastNum = 0
    for char in line:
        if char in digits:
            if not firstFound: 
               firstNum = char
               firstFound = True
            lastNum = char
        
    print("Line{}: {}".format(count, line.strip()))
    total = int(firstNum+lastNum)
    print(firstNum, " ", lastNum, " ", total) 
    count += total
print(count)