#
# Day 1 puzzle 2
# 
 
file = open('Day1/input2.txt', 'r')
Lines = file.readlines()
digits = "0123456789"
 
numInLetters = {
        "zero":'0',
        "one":'1',
        "two":'2',
        "three":'3',
        "four":'4',
        "five":'5',
        "six":'6',
        "seven":'7',
        "eight":'8',
        "nine":'9' }

count = 0
for line in Lines:
    firstFound = False
    firstNum = 0
    lastNum = 0
    firstPos = -1
    lastPos = 999999
    curPos = 0

    for char in line:
        if char in digits:
            if not firstFound: 
               firstNum = char
               firstFound = True
               firstPos = curPos
            lastNum = char
            lastPos = curPos
        for num in numInLetters:
            if (line.find(num,curPos,curPos+len(num)) == curPos ):
                if not firstFound: 
                    firstNum = numInLetters[num]
                    firstFound = True
                    firstPos = curPos
                lastNum = numInLetters[num]
                lastPos = curPos
        curPos = curPos + 1

    print("Line", count, line.strip())
    total = int(firstNum+lastNum)
    print("first:", firstNum, " firstPos:", firstPos , " last: ", lastNum,  " lastPos:", lastPos,  " total:", total) 
    count += total
print(count)