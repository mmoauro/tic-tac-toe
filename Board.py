class Board:
    def __init__ (self):
        self.availableNumbers = [1,2,3,4,5,6,7,8,9]
        self.board = [1,2,3,4,5,6,7,8,9]
    
    def choose (self, number: int, print: str):
        self.board[number - 1] = print
        self.availableNumbers.remove(number)
        self.printBoard()
    
    def printBoard (self):
        print(f"{self.board[0]} | {self.board[1]} | {self.board[2]}")
        print("---------")
        print(f"{self.board[3]} | {self.board[4]} | {self.board[5]}")
        print("---------")
        print(f"{self.board[6]} | {self.board[7]} | {self.board[8]}")