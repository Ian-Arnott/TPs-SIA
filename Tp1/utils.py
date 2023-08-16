import os
from optparse import OptionParser

SEARCH_METHODS = ['bfs', 'dfs', 'greedy', 'astar']
HEURISTICS = ['distance', 'heu2']

def readCommand(argv):
    parser = OptionParser()
    parser.add_option('-l', '--level', dest='board', help='level of game to play', default='level2.txt')
    parser.add_option('-m', '--method', dest='method', help='research method', default='bfs')
    parser.add_option('-H', '--heuristic', dest='heuristic', help='heuristic', default='distance')
    args = dict()
    options, _ = parser.parse_args(argv)

    file_path = 'boards/' + options.board
    file_exists = os.path.exists(file_path)

    if file_exists == False:
        print("We are still working on that level!")
        exit(1)
    if options.method not in SEARCH_METHODS:
        print("Choose a supported research method")
        exit(1)
    if options.heuristic not in HEURISTICS:
        print("Choose a supported heuristic")
        exit(1)
        
    with open(file_path,"r") as f: 
        layout = f.readlines()
    args['layout'] = layout
    args['method'] = options.method
    args['heuristic'] = options.heuristic
    return args


def print_solution(path, boardMatrix):
    output = open('./' + "solution.txt", 'w+', encoding='utf-8')
    output.write("\nSolution:\n")
    stepCount = 0;
    for step in path:
        output.write("Step " + str(stepCount) + ":\n")
        output.write(step.print_game_state(boardMatrix))
        output.write("---------------------------------------\n")
        stepCount += 1