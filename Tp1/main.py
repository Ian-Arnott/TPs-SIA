import time
import sys
from utils import readCommand
from game import layoutToGameState, clearDynamicElements, getPlayerPosition, getBoxesPosition, getGoalsPosition
from algorithms import bfs, dfs, greedy, astar
from GameState import GameState

if __name__ == '__main__':
    layout, method, heuristic = readCommand(sys.argv[2:]).values()
    boardMatrix = layoutToGameState(layout)

    initialGameState = GameState(getPlayerPosition(boardMatrix), getBoxesPosition(boardMatrix), getGoalsPosition(boardMatrix))
    clearDynamicElements(boardMatrix, initialGameState)

    time_start = time.time()

    if method == 'bfs':
        path, exploredNodes, frontierNodes = bfs(initialGameState, boardMatrix)
    elif method == 'dfs':
        path, exploredNodes, frontierNodes = dfs(initialGameState)
    elif method == 'greedy':
        path, exploredNodes, frontierNodes = greedy(initialGameState, heuristic)
    else:
        path, exploredNodes, frontierNodes = astar(initialGameState, heuristic)

    time_end = time.time()

    print('\nResult: ' + str(path))
    print('Cost of the solution: ' + str(path))
    print('Amount of expanded nodes: ' + str(exploredNodes))
    print('Amount of frontier nodes: ' + str(frontierNodes))
    # TODO: imprimir path (la solution)
    print('Runtime of %s: %.2f second.' %(method, time_end-time_start))
    print("DONE")