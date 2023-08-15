import numpy as np
from GameState import GameState

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
    return list(tuple(x) for x in np.argwhere((gameState == BOX) | (gameState == BOX_ON_GOAL)))

def getWallsPosition(gameState):
    return tuple(tuple(x) for x in np.argwhere(gameState == WALL))

def getGoalsPosition(gameState):
    return tuple(tuple(x) for x in np.argwhere((gameState == GOAL) | (gameState == BOX_ON_GOAL)))

def isEndState(gameState):
    return sorted(getBoxesPosition(gameState)) == sorted(getGoalsPosition(gameState))

def getNeighbours(boardMatrix, playerPos:tuple):
    """ Returns possible moves from a given position"""
    i, j = playerPos
    neighbours = []
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] # down, up, right, left

    for direction in directions:
        nextPos = (i + direction[0], j + direction[1])
        #TODO: En el sokoban, una vez que coloco una caja en un goal, queda fija?
        if boardMatrix[nextPos[0], nextPos[1]] != WALL and boardMatrix[nextPos[0], nextPos[1]] != BOX_ON_GOAL: 
            if boardMatrix[nextPos[0], nextPos[1]] == BOX:
                if boardMatrix[nextPos[0] + direction[0], nextPos[1] + direction[1]] == WALL or boardMatrix[nextPos[0] + direction[0], nextPos[1] + direction[1]] == BOX_ON_GOAL:
                    continue
            neighbours.append(nextPos)
            
    return neighbours

def clearDynamicElements(boardMatrix, initialGameState:GameState):
    row, col = initialGameState.playerPos
    boardMatrix[row][col] = FREE_SPACE

    for boxPos in initialGameState.boxesPos:
        row, col = boxPos
        boardMatrix[row][col] = FREE_SPACE

def printBoard(gameState):
    for row in gameState:
        print(''.join(row))