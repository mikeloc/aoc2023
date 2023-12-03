# Python code to
# demonstrate readlines()
 
 # Using readlines()
file1 = open('Day1_puzzle_2/input2.txt', 'r')
Lines = file1.readlines()
 
numInLetters = ['zero','one','two','three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def strToDigit(a_str):
    numInLet = {
        "zero":'0',
        "one":'1',
        "two":'2',
        "three":'3',
        "four":'4',
        "five":'5',
        "six":'6',
        "seven":'7',
        "eight":'8',
        "nine":'9'
    }
    return numInLet[a_str]

count = 0
# Strips the newline character
for line in Lines:
    firstFound = False
    firstNum = 0
    lastNum = 0
    firstPos = -1
    lastPos = 999999
    curPos = 0

    for char in line:
        if (char >= '0') and (char <= '9'):
            if not firstFound: 
               firstNum = char
               firstFound = True
               firstPos = curPos
            lastNum = char
            lastPos = curPos
        for num in numInLetters:
            if (line.find(num,curPos,curPos+len(num)) == curPos ):
                if not firstFound: 
                    firstNum = strToDigit(num)
                    firstFound = True
                    firstPos = curPos
                lastNum = strToDigit(num)
                lastPos = curPos
        curPos = curPos + 1

    print("Line{}: {}".format(count, line.strip()))
    total = int(firstNum+lastNum)
    print("first:", firstNum, " firstPos:", firstPos , " last: ", lastNum,  " lastPos:", lastPos,  " total:", total) 
    count += total
print(count)