import numpy as np

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
    return tuple(tuple(x) for x in np.argwhere((gameState == BOX) | (gameState == BOX_ON_GOAL)))

def getWallsPosition(gameState):
    return tuple(tuple(x) for x in np.argwhere(gameState == WALL))

def getGoalsPosition(gameState):
    return tuple(tuple(x) for x in np.argwhere((gameState == GOAL) | (gameState == BOX_ON_GOAL)))

def isEndState(gameState):
    return sorted(getBoxesPosition(gameState)) == sorted(getGoalsPosition(gameState))

def getNeighbours(gameState, playerPos:tuple):
    (i, j) = playerPos
    neighbours = []
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] # down, up, right, left

    for direction in directions:
        (di, dj) = direction
        if gameState[i + di, j + dj] != WALL:
            neighbour = (i + di, j + dj)
            neighbours.append(neighbour)

    return neighbours

def clearDynamicElements(gameState, playerPos:tuple, BoxesPos:list[tuple]):
    row, col = playerPos
    gameState[row][col] = FREE_SPACE

    for boxPos in BoxesPos:
        row, col = boxPos
        gameState[row][col] = FREE_SPACE