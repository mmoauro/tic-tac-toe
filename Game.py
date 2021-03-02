import Board as board
import Player as player
import Computer as computer
class Game:
    def __init__ (self, j1Name: str, j2Name: str, j1Print: str, j2Print: str):
        self.board = board.Board()
        self.j1 = player.Player(j1Name, j1Print)
        self.j2 = computer.Computer(j2Name, j2Print)
        self.winningLines = [
            [1,2,3],
            [4,5,6],
            [7,8,9],
            [1,5,9],
            [3,5,7],
            [1,4,7],
            [3,6,9],
            [2,5,8]
        ]
    
    def play (self):
        self.board.printBoard()
        i = 0
        while len(self.board.availableNumbers) > 0 and not self.getWinner():
            chooser = self.j1
            if i % 2 != 0:
                chooser = self.j2
            self.board.choose(chooser.chooseNumber(self.board.availableNumbers), chooser.boardLetter)
            i+=1
        
        if not self.getWinner():
            print ("Tie")
        else:
            print(f"The winner is {self.getWinner().name}.")


    def getWinner (self):
        for x in self.j1.getNumberCombations():
            if x in self.winningLines:
                return self.j1
        for i in self.j2.getNumberCombations():
            if i in self.winningLines:
                return self.j2
        return None

game = Game("Manuel", "Pedro", "X", "O")
game.play()