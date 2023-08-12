import time
import sys
from utils import readCommand
from game import layoutToGameState
from algorithms import bfs, dfs, greedy, astar

if __name__ == '__main__':
    layout, method, heuristic = readCommand(sys.argv[2:]).values()
    
    gameState = layoutToGameState(layout)
    
    time_start = time.time()

    if method == 'bfs':
        path, exploredNodes, frontierNodes = bfs(gameState)
    elif method == 'dfs':
        path, exploredNodes, frontierNodes = dfs(gameState)
    elif method == 'greedy':
        path, exploredNodes, frontierNodes = greedy(gameState, heuristic)
    else:
        path, exploredNodes, frontierNodes = astar(gameState, heuristic)

    time_end = time.time()

    print('Result: ' + str(path))
    print('Cost of the solution: ' + str(path))
    print('Amount of expanded nodes: ' + str(exploredNodes))
    print('Amount of frontier nodes: ' + str(frontierNodes))
    # TODO: imprimir path (la solution)
    print('Runtime of %s: %.2f second.' %(method, time_end-time_start))
    print("DONE")