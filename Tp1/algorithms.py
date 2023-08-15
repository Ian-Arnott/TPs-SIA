from Tree import Tree, Node
from collections import deque
from game import *
from GameState import GameState

# https://docs.python.org/es/3/library/collections.html#collections.deque
# collections.deque es una implementación alternativa de colas sin límites con operaciones atómicas rápidas
# append() y popleft() que no requieren bloqueo y también soportan indexación.



#TODO: Extraer comportamientos comunes a todos los metodos de busqueda
def bfs(initialGameState:GameState, boardMatrix):
    exploredNodes:list[Node] = []
    frontierNodes = deque()

    tree = Tree(initialGameState)
    root = tree.get_root()
    frontierNodes.append(root)

    count = 0
    while len(frontierNodes) > 0:
        currentNode = frontierNodes.popleft()
        currentState = currentNode.gameState

        print("Iteration: " + str(count) + "\t" + "Depth: " + str(currentNode.depth) + "\t" + str(currentState))
        count += 1

        # Verifies if the current state is a solution
        if currentState.isSolved():
            print("\t\tI won the game")
            return 1, len(exploredNodes), len(frontierNodes) #TODO: Cambiarlo para que no termine la ejecucion
            # TODO: return path solution
        
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
            if nextState not in exploredNodes:
                nextNode = currentNode.add_child(nextState)
                frontierNodes.append(nextNode)

        exploredNodes.append(currentNode)

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
            return True
    return False