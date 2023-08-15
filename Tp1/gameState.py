class GameState(object):
    """Represents the state of the game (position of movable objects and goals) at a given moment"""
    def __init__(self, playerPos:tuple, boxesPos:list[tuple], goalsPos:list[tuple]):
        self.playerPos = playerPos
        self.boxesPos = boxesPos
        self.goalsPos = sorted(goalsPos)


    def __eq__(self, other):
        result =  self.__class__ == other.__class__ and \
            self.playerPos == other.playerPos and \
            sorted(self.boxesPos) == sorted(other.boxesPos)
        #print("Comparo {} con {} y da {}".format(self, other, result))
        return result
    
    def __hash__(self):
        return hash((self.playerPos, self.boxesPos))
    
    def __repr__(self) -> str:
        return f"Player: {self.playerPos}\tBoxes: {self.boxesPos}\tGoals: {self.goalsPos}"
    
    def isSolved(self) -> bool:
        """ Checks if all the boxes are on the goals """
        return sorted(self.boxesPos) == self.goalsPos
    
    def printGameState(self, boardMatrix):
        """ Prints the game state in a readable format """
        toPrint = ""
        for i in range(len(boardMatrix)):
            for j in range(len(boardMatrix[i])):
                if (i,j) == self.playerPos:
                    toPrint += "P"
                elif (i,j) in self.boxesPos:
                    if (i,j) in self.goalsPos:
                        toPrint += "X"
                    else:
                        toPrint += "D"
                elif (i,j) in self.goalsPos:
                    toPrint += "*"
                elif boardMatrix[i][j] == "#":
                    toPrint += "#"
                else:
                    toPrint += " "
            toPrint += "\n"
        return toPrint