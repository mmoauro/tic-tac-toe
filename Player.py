from itertools import combinations
class Player:
    def __init__ (self, name: str, boardLetter: str):
        self.name = name
        self.boardLetter = boardLetter
        self.choosenNumbers = []
    
    def chooseNumber (self, numbers: list):
        number = 0
        while not number in numbers:
            try:
                number = int (input (f"{self.name} turns (enter a free board number):  "))
            except:
                return self.chooseNumber(numbers)
                
        self.addChoosenNumber(number)
        return number
    
    def addChoosenNumber (self, number: int):
        self.choosenNumbers.append(number)
        self.choosenNumbers.sort()

    def getNumberCombations (self):
        return sum([list(map(list, combinations(self.choosenNumbers, 3))) for i in range(len(self.choosenNumbers) + 1)], [])