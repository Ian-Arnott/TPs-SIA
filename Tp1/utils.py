import os
import sys
from optparse import OptionParser

SEARCH_METHODS = ['bfs', 'dfs', 'greedy', 'astar']
HEURISTICS = ['heu1', 'heu2']

def readCommand(argv):
    parser = OptionParser()
    parser.add_option('-l', '--level', dest='board', help='level of game to play', default='level2.txt')
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