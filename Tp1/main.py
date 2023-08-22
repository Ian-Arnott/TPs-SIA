import time
import sys
from utils import readCommand, print_solution
from game import layoutToGameState, clearDynamicElements, getPlayerPosition, getBoxesPosition, getGoalsPosition
from algorithms import bfs, dfs, greedy, astar, manhattan, combined, hamming
from gameState import GameState

def runGame(args):
    layout, method, heuristic = readCommand(args).values()
    boardMatrix = layoutToGameState(layout)

    goals = getGoalsPosition(boardMatrix)
    initialGameState = GameState(getPlayerPosition(boardMatrix), getBoxesPosition(boardMatrix))
    clearDynamicElements(boardMatrix, initialGameState)

    if heuristic == "manhattan":
        heuristicFunction = manhattan
    elif heuristic == "combined":
        heuristicFunction = combined
    elif heuristic == "hamming":
        heuristicFunction = hamming 

    time_start = time.time()

    if method == 'bfs':
        path, cost, exploredNodes, frontierNodes = bfs(initialGameState, boardMatrix, goals)
    elif method == 'dfs':
        path, cost, exploredNodes, frontierNodes = dfs(initialGameState, boardMatrix, goals)
    elif method == 'greedy':
        path, cost, exploredNodes, frontierNodes = greedy(initialGameState, boardMatrix, goals, heuristicFunction)
    elif method == 'astar':
        path, cost, exploredNodes, frontierNodes = astar(initialGameState, boardMatrix, goals, heuristicFunction)

    time_end = time.time()

    return {'success': path!=1, 'method': method, 'level': args[2], 'heuristic': heuristic, 'cost': cost,
            'exploredNodes': exploredNodes, 'frontierNodes': frontierNodes, 'runtime': time_end-time_start}

if __name__ == '__main__':
    layout, method, heuristic = readCommand(sys.argv).values()
    boardMatrix = layoutToGameState(layout)

    goals = getGoalsPosition(boardMatrix)
    initialGameState = GameState(getPlayerPosition(boardMatrix), getBoxesPosition(boardMatrix))
    clearDynamicElements(boardMatrix, initialGameState)

    if heuristic == "manhattan":
        heuristicFunction = manhattan
    elif heuristic == "combined":
        heuristicFunction = combined
    elif heuristic == "hamming":
        heuristicFunction = hamming 

    time_start = time.time()

    if method == 'bfs':
        path, cost, exploredNodes, frontierNodes = bfs(initialGameState, boardMatrix, goals,)
    elif method == 'dfs':
        path, cost, exploredNodes, frontierNodes = dfs(initialGameState, boardMatrix, goals)
    elif method == 'greedy':
        path, cost, exploredNodes, frontierNodes = greedy(initialGameState, boardMatrix, goals, heuristicFunction)
    elif method == 'astar':
        path, cost, exploredNodes, frontierNodes = astar(initialGameState, boardMatrix, goals, heuristicFunction)

    time_end = time.time()

    print('\nResult: Solution found' if path != 1 else '\nResult: Couldn\'t find solution\n')
    print('Search method: ' + method)
    if method == 'greedy' or method == 'astar':
        print('Heuristic: ' + heuristic)
    print('Cost of the solution: ' + str(cost))
    print('Expanded nodes: ' + str(exploredNodes))
    print('Frontier nodes: ' + str(frontierNodes))
    print('Runtime of %s: %.3f seconds.' %(method, time_end-time_start))
    if path != 1:
        print_solution(path, boardMatrix, goals)
    print("DONE")