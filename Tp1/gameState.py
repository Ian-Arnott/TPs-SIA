class GameState(object):
    """Represents the state of the game (position of movable objects and goals) at a given moment"""
    def __init__(self, playerPos:tuple, boxesPos:list[tuple]):
        self.playerPos = playerPos
        self.boxesPos = boxesPos

    def __eq__(self, other):
        result =  self.__class__ == other.__class__ and \
            self.playerPos == other.playerPos and \
            self.boxesPos == other.boxesPos
        return result
    
    def __hash__(self):
        return hash((self.playerPos, tuple(self.boxesPos)))
    
    def __repr__(self) -> str:
        return f"Player: {self.playerPos}\tBoxes: {self.boxesPos}"
    
    def isSolved(self, goals) -> bool:
        """ Checks if all the boxes are on the goals. Goals and Boxes lists must be sorted beforehand """
        return self.boxesPos == goals
    
    def printGameState(self, boardMatrix, goals):
        """ Prints the game state in a readable format """
        toPrint = ""
        for i in range(len(boardMatrix)):
            for j in range(len(boardMatrix[i])):
                if (i,j) == self.playerPos:
                    toPrint += "P"
                elif (i,j) in self.boxesPos:
                    if (i,j) in goals:
                        toPrint += "X"
                    else:
                        toPrint += "D"
                elif (i,j) in goals:
                    toPrint += "*"
                elif boardMatrix[i][j] == "#":
                    toPrint += "#"
                else:
                    toPrint += " "
            toPrint += "\n"
        return toPrint