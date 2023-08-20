import numpy as np
from gameState import GameState

PLAYER = 'P'
WALL = '#'
BOX = 'D'
GOAL = '*'
FREE_SPACE = ' '
BOX_ON_GOAL = 'X'

def layoutToGameState(layout):
    layout = [x.replace('\n','') for x in layout]
    layout = [','.join(layout[i]) for i in range(len(layout))]
    layout = [x.split(',') for x in layout]

    maxColsNum = max([len(x) for x in layout])
    for irow in range(len(layout)):
        colsNum = len(layout[irow])
        if colsNum < maxColsNum:
            layout[irow].extend([FREE_SPACE for _ in range(maxColsNum-colsNum)])
    return np.array(layout)

def getPlayerPosition(gameState):
    return tuple(np.argwhere(gameState == PLAYER)[0])

def getBoxesPosition(gameState):
    return sorted(list(tuple(x) for x in np.argwhere((gameState == BOX) | (gameState == BOX_ON_GOAL))))

def getGoalsPosition(gameState):
    return sorted(list(tuple(x) for x in np.argwhere((gameState == GOAL) | (gameState == BOX_ON_GOAL))))

    
# TODO: check deadlocks
def getNeighbours(boardMatrix, goalPos:tuple, boxesPos:tuple, playerPos:tuple):
    """ Returns possible moves from a given position"""
    i, j = playerPos
    neighbours = []
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] # down, up, right, left

    for direction in directions:
        nextPos = (i + direction[0], j + direction[1])
        if boardMatrix[nextPos[0], nextPos[1]] != WALL or ((nextPos[0], nextPos[1]) in boxesPos and (nextPos[0], nextPos[1]) not in goalPos): 
            if (nextPos[0], nextPos[1]) in boxesPos:
                if boardMatrix[nextPos[0] + direction[0], nextPos[1] + direction[1]] == WALL:
                    continue
                if (nextPos[0] + direction[0], nextPos[1] + direction[1]) in boxesPos:
                    continue
            neighbours.append(nextPos)
            
    return neighbours

def clearDynamicElements(boardMatrix, initialGameState:GameState):
    row, col = initialGameState.playerPos
    boardMatrix[row][col] = FREE_SPACE

    for boxPos in initialGameState.boxesPos:
        row, col = boxPos
        boardMatrix[row][col] = FREE_SPACE