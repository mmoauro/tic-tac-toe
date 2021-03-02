import Player as player
import random
class Computer(player.Player):
    def __init__ (self, name: str, boardLetter: str):
        super().__init__(name, boardLetter)
    
    def chooseNumber (self, numbers: list):
        number = random.choice(numbers);
        print(f"{self.name} choose {number}")
        self.addChoosenNumber(number)
        return number
