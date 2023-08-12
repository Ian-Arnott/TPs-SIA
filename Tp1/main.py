import os
import sys
import numpy as np
import time
from optparse import OptionParser
from sokoban import Sokoban

SEARCH_METHODS = ["bfs", "dfs", "greedy", "astar"]
HEURISTICS = ["heu1", "heu2"]

def readCommand(argv):
    parser = OptionParser()
    parser.add_option('-l', '--level', dest='board', help='level of game to play', default='level1.txt')
    parser.add_option('-m', '--method', dest='method', help='research method', default='bfs')
    parser.add_option('-H', '--heuristic', dest='heuristic', help='heuristic', default='heu1')
    args = dict()
    options, _ = parser.parse_args(argv)

    file_path = 'boards/' + options.board
    file_exists = os.path.exists(file_path)

    if file_exists == False:
        print("We are still working on that level!")
    if options.method not in SEARCH_METHODS:
        print("Choose a supported research method")
    if options.heuristic not in HEURISTICS:
        print("Choose a supported heuristic")
        
    with open(file_path,"r") as f: 
        layout = f.readlines()
    args['layout'] = layout
    args['method'] = options.method
    args['heuristic'] = options.heuristic
    return args

def transferToGameState(layout):
    """Transfer the layout of initial puzzle"""
    # layout = [x.replace('\n','') for x in layout]
    # layout = [','.join(layout[i]) for i in range(len(layout))]
    # layout = [x.split(',') for x in layout]
    # maxColsNum = max([len(x) for x in layout])
    # for irow in range(len(layout)):
    #     for icol in range(len(layout[irow])):
              #TODO: Con un diccionario se resuelve el problema de los if
    #         if layout[irow][icol] == ' ': layout[irow][icol] = 0   # free space
    #         elif layout[irow][icol] == '#': layout[irow][icol] = 1 # wall
    #         elif layout[irow][icol] == 'P': layout[irow][icol] = 2 # player
    #         elif layout[irow][icol] == 'D': layout[irow][icol] = 3 # box
    #         elif layout[irow][icol] == '*': layout[irow][icol] = 4 # goal
    #         elif layout[irow][icol] == 'X': layout[irow][icol] = 5 # box on goal
    #     colsNum = len(layout[irow])
    #     if colsNum < maxColsNum:
    #         layout[irow].extend([1 for _ in range(maxColsNum-colsNum)]) 
    # return np.array(layout)
    return "gamestate"


if __name__ == '__main__':
    layout, method, heuristic = readCommand(sys.argv[2:]).values()
    
    gameState = transferToGameState(layout)
    
    time_start = time.time()

    if method == 'bfs':
        path, exploredNodes, frontierNodes = Sokoban.bfs(gameState)
    elif method == 'dfs':
        path, exploredNodes, frontierNodes = Sokoban.dfs(gameState)
    elif method == 'greedy':
        path, exploredNodes, frontierNodes = Sokoban.greedy(gameState, heuristic)
    else:
        path, exploredNodes, frontierNodes = Sokoban.astar(gameState, heuristic)

    time_end = time.time()

    print('Result: ' + str(path))
    print('Cost of the solution: ' + str(path))
    print('Amount of expanded nodes: ' + str(exploredNodes))
    print('Amount of frontier nodes: ' + str(frontierNodes))
    # TODO: imprimir path (la solution)
    print('Runtime of %s: %.2f second.' %(method, time_end-time_start))
    print("DONE")