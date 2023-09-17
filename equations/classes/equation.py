import random
from classes.block import Block


class Equation:
    def __init__(self, screen, blockSize, marginSize):
        self.screen = screen
        self.blockSize = blockSize
        self.marginSize = marginSize
        self.ansEquation = self.equationGenerate()
        self.currEq = self.createBlanks()
        self.questionEquation = self.currEq
        self.displayedEquation = self.currEq
        self.hide = False

        self.blocks = []
        self.getBlocks()

    def renderHint(self):
        self.updateDisplayedEquation(self.getHints())

    def unrenderHint(self):
        self.displayedEquation = self.currEq
        self.updateDisplayedEquation(self.currEq)

    def updateDisplayedEquation(self, dispEq):
        self.displayedEquation = dispEq
        for i in range(len(dispEq)):
            self.blocks[i].data = dispEq[i]

    def getClicked(self, xPos, yPos):
        for b in self.blocks:
            b.selected = False
            if b.isIn(xPos, yPos):
                b.selected = True
                return b
        return None

    def isFilled(self):
        return "_" not in self.currEq

    def isCorrect(self):
        return self.isFilled() and str(
            eval(self.currEq[: self.currEq.index("=")])
        ) == str(self.currEq[self.currEq.index("=") + 1 :])

    def displayEquation(self):
        if not self.hide:
            for b in self.blocks:
                b.drawBlock()

    def reset(self):
        self.ansEquation = self.equationGenerate()
        self.currEq = self.createBlanks()
        self.displayedEquation = self.currEq
        self.getBlocks()

    def getBlocks(self):
        self.blocks = []
        w, h = self.screen.get_size()

        numBlocks = len(self.displayedEquation)

        lenEquation = numBlocks * self.blockSize + (numBlocks - 1) * self.marginSize

        xCoord = (w - lenEquation) / 2
        yCoord = (h - self.blockSize) / 2

        for i in range(len(self.displayedEquation)):
            self.blocks.append(
                Block(
                    xCoord,
                    yCoord,
                    self.screen,
                    self.displayedEquation[i],
                    self.blockSize,
                )
            )
            xCoord += self.blockSize + self.marginSize

    def getHints(self):
        # Find blanks
        blankIndies = []
        for i in range(len(self.currEq)):
            if self.currEq[i] == "_":
                blankIndies.append(i)

        hintInd = random.choice(blankIndies)
        hintEqArr = list(self.currEq)
        hintEqArr[hintInd] = self.ansEquation[hintInd]

        return "".join(hintEqArr)

    def createBlanks(self, numBlanks=2):
        eqArr = list(self.ansEquation)
        for _ in range(numBlanks):
            i = random.randint(0, len(eqArr) - 1)
            while eqArr[i] == "_" or eqArr[i] == "=" or eqArr[i] in "+-/*":
                i = random.randint(0, len(eqArr) - 1)

            eqArr[i] = "_"
        return "".join(eqArr)

    def equationGenerate(self, numOperations=1, ansDigits=2, allowedOps=["+", "-"]):
        ans = ""
        valid = False

        while not valid:
            ops = [random.choice(allowedOps) for _ in range(numOperations)]
            nums = [
                random.randint(0, 10**ansDigits - 1) for _ in range(numOperations + 1)
            ]

            for i in range(numOperations):
                op = ops[i]

                if op == "/":
                    nums[i + 1] = nums[i] // random.randint(2, nums[i + 1])
                elif op == "*":
                    nums[i + 1] = random.randint(0, 9)
                elif op == "-":
                    nums[i], nums[i + 1] = max(nums[i], nums[i + 1]), min(
                        nums[i], nums[i + 1]
                    )

            eqString = str(nums[0]) + "".join(
                [ops[i] + str(nums[i + 1]) for i in range(numOperations)]
            )

            # Make sure string is valid
            ans = eval(eqString)
            if ans > 0 and len(str(ans)) <= ansDigits:
                valid = True

        return eqString + "=" + str(ans)
