from tree import Tree
from collections import deque
from game import *
from gameState import GameState

# https://docs.python.org/es/3/library/collections.html#collections.deque
# collections.deque es una implementación alternativa de colas sin límites con operaciones atómicas rápidas
# append() y popleft() que no requieren bloqueo y también soportan indexación.


#TODO: Extraer comportamientos comunes a todos los metodos de busqueda
def bfs(initialGameState:GameState, boardMatrix):
    exploredStates:list[GameState] = []
    frontierNodes = deque()

    tree = Tree(initialGameState)
    root = tree.get_root()
    exploredStates.append(initialGameState)
    frontierNodes.append(root)

    #count = 0
    while len(frontierNodes) > 0:
        currentNode = frontierNodes.popleft()
        currentState = currentNode.gameState

        #print("Iteration: " + str(count) + "\t" + "Depth: " + str(currentNode.depth) + "\t" + str(currentState))
        #count += 1

        # Verifies if the current state is a solution
        if currentState.isSolved():
            print("I won the game")
            return currentNode.get_root_path(currentNode), currentNode.get_depth(), len(exploredStates), len(frontierNodes) #TODO: Cambiarlo para que no termine la ejecucion
        
        # Get the neighbours of the current state (only the ones that the player can move to)
        neighbours = getNeighbours(boardMatrix, currentState.playerPos)

        # For each neighbour, generate the new state and add it to the frontierNodes if it is not explored
        for n in neighbours:
            boxList = currentState.boxesPos.copy()

            # If the neighbour is a box, move it
            if n in boxList:
                boxList.remove(n)
                newBoxPos = (n[0] + (n[0] - currentState.playerPos[0]), n[1] + (n[1] - currentState.playerPos[1]))
                boxList.append(newBoxPos)

            nextState = GameState(n, boxList, currentState.goalsPos)

            #TODO: Mejorar la comparacion con un Hash de los estados, en vez de compararlos elemento a elemento
            if nextState not in exploredStates:
                exploredStates.append(nextState)
                nextNode = currentNode.add_child(nextState)
                frontierNodes.append(nextNode)

        #exploredStates.append(currentState)

    return 1, 0, len(exploredStates), len(frontierNodes)

def dfs(initialGameState):
    return 1,2,3


def greedy(gameState, heuristic):
    return 1,2,3
    
def astar(gameState, heuristic):
    return 1,2,3

