from tree import Tree, Node
from collections import deque
from game import *

# https://docs.python.org/es/3/library/collections.html#collections.deque
# collections.deque es una implementación alternativa de colas sin límites con operaciones atómicas rápidas
# append() y popleft() que no requieren bloqueo y también soportan indexación.

def isSolution(posBoxes, posGoals):
    # Check if all boxes are on the goals
    return sorted(posBoxes) == posGoals

#TODO: Extraer comportamientos comunes a todos los metodos de busqueda
def bfs(initialGameState, boardMatrix):
    exploredNodes:list[Node] = []
    frontierNodes = deque()

    tree = Tree(initialGameState)
    root = tree.get_root()
    frontierNodes.append(root)

    #count = 0
    while len(frontierNodes) > 0:
        current = frontierNodes.popleft()

        #print("Iteration: " + str(count) + "\t" + "Depth: " + str(current.depth) + "\t" + "Player: " + str(current.gameState["P"]) + "\t" + "Boxes: " + str(current.gameState["D"]) + "\t" + "Goals: " + str(current.gameState["*"]))
        #count += 1

        # Verifies if the current state is a solution
        if isSolution(current.gameState["D"], current.gameState["*"]):
            print("\t\tI won the game")
            return 1, len(exploredNodes), len(frontierNodes) #TODO: Cambiarlo para que no termine la ejecucion
            # TODO: return path solution
        
        # Get the neighbours of the current state (only the ones that the player can move to)
        neighbours = getNeighbours(boardMatrix, current.gameState, current.gameState["P"])

        # For each neighbour, generate the new state and add it to the frontierNodes if it is not explored
        for n in neighbours:
            boxList = current.gameState["D"].copy()

            # If the neighbour is a box, move it
            if isBox(current.gameState["D"], n):
                boxList.remove(n)
                newBoxPos = (n[0] + (n[0] - current.gameState["P"][0]), n[1] + (n[1] - current.gameState["P"][1]))
                boxList.append(newBoxPos)

            nextState = generateGameState(n, boxList, current.gameState["*"])

            #TODO: Mejorar la comparacion con un Hash de los estados, en vez de compararlos elemento a elemento
            if not _exploredState(exploredNodes, nextState):
                nextNode = current.add_child(nextState)
                frontierNodes.append(nextNode)

    exploredNodes.append(current)

    return 1, len(exploredNodes), len(frontierNodes)

    
def dfs(gameState):
    return 1,2,3
    
def greedy(gameState, heuristic):
    return 1,2,3
    
def astar(gameState, heuristic):
    return 1,2,3

    
def _exploredState(exploredNodes, state):
    for node in exploredNodes:
        if compareStates(node.gameState, state):
            print("\n\t\tI already explored this state\t\t\n")
            return True
    return False