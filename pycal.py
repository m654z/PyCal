import math
import random

ops = ["+", "-", "*", "/", "%"]
rsi = False
eval1 = False
eval2 = False
loop = False
loopTimes = False
additionMode = False
reading = False
readingFunc = False
readingFunc2 = False
readingFuncName = False
selectedInt = 0
temp = []
toEval = []
n1 = []
n2 = []
loopCode = []
iLoopTimes = []
read = []
funcName = []
funcCode = []
funcTemp = []
var = 0
op = ""
funcs = {}

def read(tokens):
    tokens = tokens.replace("p", str(math.pi))
    tokens = tokens.replace("e", str(math.e))
    tokens = tokens.replace("h", "1.618033988749895")
    tokens = tokens.replace("R", str(random.randint(0, 100)))
    tokens = list(tokens)
    for i in range(0, len(tokens)):
        parse(tokens[i])

def parse(cmd):

    global ops
    global rsi
    global eval1
    global eval2
    global loop
    global loopTimes
    global additionMode
    global reading
    global readingFunc
    global readingFunc2
    global readingFuncName
    global selectedInt
    global temp
    global toEval
    global n1
    global n2
    global loopCode
    global iLoopTimes
    global read
    global funcName
    global funcCode
    global funcTemp
    global var
    global op
    global funcs

    if readingFuncName == True:
        if cmd == "_":
            readingFuncName = False
            read(funcs[''.join(funcTemp)])
            funcTemp = []

        else:
            funcTemp.append(cmd)

    elif readingFunc == True:
        if cmd == '"':
            readingFunc = False
            readingFunc2 = True

        else:
            funcCode.append(cmd)

    elif readingFunc2 == True:
        if cmd == "-":
            readingFunc2 = False
            funcs[''.join(funcName)] = ''.join(funcCode)
            funcName = []
            funcCode = []

        else:
            funcName.append(cmd)

    elif reading == True:
        if cmd == ";":
            reading = False
            var = ''.join(read)
            read = []

        else:
            read.append(cmd)

    elif loopTimes == True:
        if cmd == "[":
            loop = True
            loopTimes = False

        elif cmd == "*":
            loopTimes = False

        elif cmd == "i":
            iLoopTimes.append(input(">> "))

        else:
            iLoopTimes.append(cmd)

    elif loop == True:
        if cmd == "]":
            loop = False
            
            for i in range(0, int(''.join(iLoopTimes))):
                read(''.join(loopCode))

        else:
            loopCode.append(cmd)

    elif eval1 == True:
        if cmd in ops:
            op = cmd
            eval2 = True
            eval1 = False

        elif cmd == "r":
            n1.append(str(var))

        elif cmd == "i":
            n1.append(input(">> "))

        else:
            n1.append(cmd)

    elif eval2 == True:
        if cmd == "}":
            eval2 = False
            var = eval(''.join(n1) + op + ''.join(n2))
            n1 = []
            n2 = []
            op = ""

        elif cmd == "r":
            n2.append(str(var))

        elif cmd == "i":
            n2.append(input(">> "))

        else:
            n2.append(cmd)
            

    elif rsi == True:
        if cmd == ")":
            rsi = False
            selectedInt = int(''.join(temp))
            temp = []

        else:
            temp.append(cmd)

    elif cmd == "F":
        if additionMode == True:
            var += fib(selectedInt)

        else:
            var = fib(selectedInt)
            
    elif cmd == "(":
        rsi = True

    elif cmd == "{":
        eval1 = True

    elif cmd == "+":
        selectedInt += 1

    elif cmd == "-":
        selectedInt -= 1

    elif cmd == "[":
        loop = True

    elif cmd == "*":
        loopTimes = True

    elif cmd == "S":
        if additionMode == True:
            var += math.sqrt(selectedInt)

        else:
            var = math.sqrt(selectedInt)

    elif cmd == "C":
        if additionMode == True:
            var += math.ceil(selectedInt)

        else:
            var = math.ceil(selectedInt)

    elif cmd == "f":
        if additionMode == True:
            var += math.floor(selectedInt)

        else:
            var = math.floor(selectedInt)

    elif cmd == "x":
        if additionMode == True:
            var += math.factorial(selectedInt)

        else:
            var = math.factorial(selectedInt)

    elif cmd == "E":
        if additionMode == True:
            var += math.exp(selectedInt)

        else:
            var = math.factorial(selectedInt)

    elif cmd == "!":
        print(var)

    elif cmd == ".":
        additionMode = True

    elif cmd == ",":
        additionMode = False

    elif cmd == "I":
        var = int(input(">> "))

    elif cmd == "i":
        var = input(">> ")

    elif cmd == "n":
        try:
            var = int(var)

        except ValueError:
            print("ValueError: can't convert a string to an integer")

    elif cmd == ":":
        reading = True

    elif cmd == '"':
        readingFunc = True

    elif cmd == "/":
        readingFuncName = True

def fib(n):
    r = 0
    c = 1
    p = 0

    for i in range(0, n+1):
        r = p + c
        p = c
        c = r
        
    return r

while 1:
    read(input("> "))
