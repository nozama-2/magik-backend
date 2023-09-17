import math
import random


def equationGenerate(numOperations=1, ansDigits=1, allowedOps=['+', '-']):
    ans = ''
    valid = False

    while not valid:
        ops = [random.choice(allowedOps) for _ in range(numOperations)]
        nums = [random.randint(0, 10**ansDigits-1)
                for _ in range(numOperations+1)]

        for i in range(numOperations):
            op = ops[i]

            if op == '/':
                nums[i+1] = nums[i] // random.randint(2, nums[i+1])
            elif op == '*':
                nums[i+1] = random.randint(0, 9)
            elif op == '-':
                nums[i], nums[i+1] = max(nums[i],
                                         nums[i+1]), min(nums[i], nums[i+1])

        eqString = str(nums[0]) + "".join([ops[i] + str(nums[i+1])
                                           for i in range(numOperations)])

        # Make sure string is valid
        ans = eval(eqString)
        if ans > 0 and len(str(ans)) <= ansDigits:
            valid = True

    return eqString + '=' + str(ans)


def createBlanks(eqString, numBlanks=2):
    eqArr = list(eqString)
    for _ in range(numBlanks):
        i = random.randint(0, len(eqArr)-1)
        while eqArr[i] == '_' or eqArr[i] == '=':
            i = random.randint(0, len(eqArr)-1)

        eqArr[i] = '_'
    return ''.join(eqArr)


def getHints(eqStringAns, eqString):
    # Find blanks
    blankIndies = []
    for i in range(len(eqString)):
        if eqString[i] == '_':
            blankIndies.append(i)

    hintInd = random.choice(blankIndies)
    hintEqArr = list(eqString)
    hintEqArr[hintInd] = eqStringAns[hintInd]

    return ''.join(hintEqArr)
