# Python code to
# demonstrate readlines()
 
 # Using readlines()
file1 = open('day1_puzzle_1/input2.txt', 'r')
Lines = file1.readlines()
 


count = 0
# Strips the newline character
for line in Lines:
    firstFound = False
    firstNum = 0
    lastNum = 0
    for char in line:
        if (char >= '0') and (char <= '9'):
            if not firstFound: 
               firstNum = char
               firstFound = True
            lastNum = char
        
    print("Line{}: {}".format(count, line.strip()))
    total = int(firstNum+lastNum)
    print(firstNum, " ", lastNum, " ", total) 
    count += total
print(count)