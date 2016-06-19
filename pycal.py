import math
import random
import statistics
import datetime
import re
import string
import time

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
readingListVal = False
stats = False
loopForever = False
readingT = False
temp = []
toEval = []
n1 = []
n2 = []
loopCode = []
iLoopTimes = []
readStr = []
funcName = []
funcCode = []
funcTemp = []
listVal = []
returned = 0
var = 0
op = ""
funcs = {}

def read(tokens):
    tokens = tokens.replace("!p", str(math.pi))
    tokens = tokens.replace("!e", str(math.e))
    tokens = tokens.replace("!h", "1.618033988749895")
    tokens = tokens.replace("!r", str(random.random()))
    tokens = tokens.replace("!R", str(random.randint(0, 100)))
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
    global readingListVal
    global stats
    global loopForever
    global readingT
    global var
    global temp
    global toEval
    global n1
    global n2
    global loopCode
    global iLoopTimes
    global readStr
    global funcName
    global funcCode
    global funcTemp
    global listVal
    global varTemp
    global returned
    global var
    global op
    global funcs
    global read

    if readingT == True:
        if cmd == "1":
            returned = math.acos(var)

        elif cmd == "2":
            returned = math.asin(var)

        elif cmd == "3":
            returned = math.atan(var)

        elif cmd == "4":
            returned = math.atan2(var)

        elif cmd == "5":
            returned = math.cos(var)

        elif cmd == "6":
            returned = math.hypot(var)

        elif cmd == "7":
            returned = math.sin(var)

        elif cmd == "8":
            returned = math.tan(var)

        readingT = False

    if stats == True:
        if cmd == "M":
            var2 = var.split(",")
            for i in range(len(var2)):
                var2[i] = int(var2[i])
                
            returned = statistics.mean(var2)

        elif cmd == "m":
            var2 = var.split(",")
            for i in range(len(var2)):
                var2[i] = int(var2[i])
                
            returned = statistics.median(var2)

        elif cmd == "O":
            var2 = var.split(",")
            for i in range(len(var2)):
                var2[i] = int(var2[i])

            returned = statistics.mode(var2)

        elif cmd == ".":
            stats = False

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
            var = ''.join(readStr)
            read = []

        else:
            readStr.append(cmd)

    elif loopTimes == True:
        if cmd == "[":
            loop = True
            loopTimes = False

        elif cmd == "*":
            loopTimes = False

        elif cmd == "i":
            iLoopTimes.append(input(">> "))

        elif cmd == "I":
            loopForever = True

        else:
            iLoopTimes.append(cmd)

    elif loop == True:
        if cmd == "]":
            loop = False

            if loopForever == True:
                while 1:
                    read(''.join(loopCode))

            else:
                for i in range(0, int(''.join(iLoopTimes))):
                    read(''.join(loopCode))

        else:
            loopCode.append(cmd)

    elif eval1 == True:
        if cmd in ops:
            op = cmd
            eval2 = True
            eval1 = False

        elif cmd == "v":
            n1.append(str(var))

        elif cmd == "r":
            n1.append(str(returned))

        elif cmd == "i":
            n1.append(input(">> "))

        elif cmd == "s":
            n1.append(int(variables[selectedVar]))

        elif cmd == "¤":
            selectedVar += 1

        elif cmd == "#":
            selectedVar -= 1

        else:
            n1.append(cmd)

    elif eval2 == True:
        if cmd == "}":
            eval2 = False
            returned = eval(''.join(n1) + op + ''.join(n2))
            n1 = []
            n2 = []
            op = ""

        elif cmd == "v":
            n2.append(str(var))

        elif cmd == "i":
            n2.append(input(">> "))

        elif cmd == "r":
            n1.append(str(returned))

        else:
            n2.append(cmd)
            

    elif rsi == True:
        if cmd == ")":
            rsi = False
            try:
                var = int(''.join(temp))

            except ValueError:
                try:
                    var = float(''.join(temp))

                except ValueError:
                    var = str(''.join(temp))
                
            temp = []

        elif cmd == "i":
            temp.append(input(">> "))

        else:
            temp.append(cmd)

    elif cmd == "F":
        if additionMode == True:
            returned += fib(var)

        else:
            returned = fib(var)
            
    elif cmd == "(":
        rsi = True

    elif cmd == "{":
        eval1 = True

    elif cmd == "+":
        var += 1

    elif cmd == "-":
        var -= 1

    elif cmd == "[":
        loop = True

    elif cmd == "*":
        loopTimes = True

    elif cmd == "S":
        if additionMode == True:
            returned += math.sqrt(var)

        else:
            returned = math.sqrt(var)

    elif cmd == "C":
        if additionMode == True:
            returned += math.ceil(var)

        else:
            returned = math.ceil(var)

    elif cmd == "f":
        if additionMode == True:
            returned += math.floor(var)

        else:
            returned = math.floor(var)

    elif cmd == "x":
        if additionMode == True:
            returned += math.factorial(var)

        else:
            returned = math.factorial(var)

    elif cmd == "E":
        if additionMode == True:
            returned += math.exp(var)

        else:
            returned = math.exp(var)

    elif cmd == "T":
        t = str(datetime.datetime.now())[11:]
        returned = t[:8]

    elif cmd == "D":
        returned = str(datetime.datetime.now())[:10]

    elif cmd == "!":
        print(returned)

    elif cmd == "^":
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

    elif cmd == "P":
        returned = generatePrimes(var)

    elif cmd == "s":
        stats = True

    elif cmd == "_":
        returned = re.sub("[^0-9]", "", returned)

    elif cmd == "½":
        returned = var/2

    elif cmd == "ö":
        returned = returned[var]

    elif cmd == "Ö":
        var.append(var)

    elif cmd == "ä":
        returned = var.split()

    elif cmd == "Ä":
        var = returned.pop()

    elif cmd == "´":
        var = returned

    elif cmd == "`":
        returned = var

    elif cmd == "=":
        if var == returned:
            returned = 1

        else:
            returned = 0

    elif cmd == ">":
        if var > returned:
            returned = 1

        else:
            returned = 0

    elif cmd == "<":
        if var < returned:
            returned = 1

        else:
            returned = 0

    elif cmd == "¨":
        time.sleep(1)

    elif cmd == "e":
        even = []
        for i in range(0, var):
            even.append(i)
            i += 2

        result = even

    elif cmd == "o":
        odd = []
        for i in range(1, var):
            odd.append(i)
            i += 2

        result = odd

    elif cmd == "~":
        readingT = True
        
def fib(n):
    r = 0
    c = 1
    p = 0

    for i in range(0, n+1):
        r = p + c
        p = c
        c = r
        
    return r

def isPrime(n):
    if n == 2:
        return True

    elif n < 2 or not n % 2:
        return False

    for i in range(3, int(n ** 0.5 + 1), 2):
        if not n % i: return False

    return True

def generatePrimes(n):
    primes = [2,]
    nOfPrimes = 1
    test = 3

    while nOfPrimes < n:
        if isPrime(test):
            primes.append(test)
            nOfPrimes += 1

        test += 2

    return primes

while 1:
    read(input("> "))
