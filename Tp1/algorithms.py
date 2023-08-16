from tree import Tree
from collections import deque
from game import *
from gameState import GameState
import math


# https://docs.python.org/es/3/library/collections.html#collections.deque
# collections.deque es una implementación alternativa de colas sin límites con operaciones atómicas rápidas
# append() y popleft() que no requieren bloqueo y también soportan indexación.


#TODO: Extraer comportamientos comunes a todos los metodos de busqueda
def bfs(initialGameState:GameState, boardMatrix):
    exploredStates = set()
    frontierNodes = deque()

    tree = Tree(initialGameState)
    root = tree.get_root()
    exploredStates.add(initialGameState)
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
        neighbours = getNeighbours(boardMatrix, currentState.goalsPos, currentState.boxesPos, currentState.playerPos)

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
                exploredStates.add(nextState)
                nextNode = currentNode.add_child(nextState)
                frontierNodes.append(nextNode)

        #exploredStates.append(currentState)

    return 1, 0, len(exploredStates), len(frontierNodes)

def dfs(initialGameState:GameState, boardMatrix):
    exploredStates = set()
    frontierNodes = deque()

    tree = Tree(initialGameState)
    root = tree.get_root()
    exploredStates.add(initialGameState)
    frontierNodes.append(root)

    while len(frontierNodes) > 0:
        currentNode = frontierNodes.pop()
        currentState = currentNode.gameState

        # Verifies if the current state is a solution
        if currentState.isSolved():
            print("I won the game")
            return currentNode.get_root_path(currentNode), currentNode.get_depth(), len(exploredStates), len(frontierNodes) #TODO: Cambiarlo para que no termine la ejecucion
        
        # Get the neighbours of the current state (only the ones that the player can move to)
        neighbours = getNeighbours(boardMatrix, currentState.goalsPos, currentState.boxesPos, currentState.playerPos)

        # For each neighbour, generate the new state and add it to the frontierNodes if it is not explored
        for n in neighbours:
            boxList = currentState.boxesPos.copy()

            # If the neighbour is a box, move it
            if n in boxList:
                boxList.remove(n)
                newBoxPos = (n[0] + (n[0] - currentState.playerPos[0]), n[1] + (n[1] - currentState.playerPos[1]))
                boxList.append(newBoxPos)

            nextState = GameState(n, boxList, currentState.goalsPos)

            if nextState not in exploredStates:
                exploredStates.add(nextState)
                nextNode = currentNode.add_child(nextState)
                frontierNodes.append(nextNode)

    return 1, 0, len(exploredStates), len(frontierNodes)


def greedy(initialGameState:GameState, boardMatrix, heuristic):
    exploredStates = set()
    frontierNodes = []

    tree = Tree(initialGameState)
    root = tree.get_root()
    exploredStates.add(initialGameState)
    frontierNodes.append((root, heuristic(initialGameState, boardMatrix)))

    while len(frontierNodes) > 0:
        currentNode, _ = frontierNodes.pop(0)
        currentState = currentNode.gameState

        # Verifies if the current state is a solution
        if currentState.isSolved():
            print("I won the game")
            return currentNode.get_root_path(currentNode), currentNode.get_depth(), len(exploredStates), len(frontierNodes) #TODO: Cambiarlo para que no termine la ejecucion
        
        # Get the neighbours of the current state (only the ones that the player can move to)
        neighbours = getNeighbours(boardMatrix, currentState.goalsPos, currentState.boxesPos, currentState.playerPos)

        # For each neighbour, generate the new state and add it to the frontierNodes if it is not explored
        for n in neighbours:
            boxList = currentState.boxesPos.copy()
            
            # If the neighbour is a box, move it
            if n in boxList:
                boxList.remove(n)
                newBoxPos = (n[0] + (n[0] - currentState.playerPos[0]), n[1] + (n[1] - currentState.playerPos[1]))
                boxList.append(newBoxPos)

            nextState = GameState(n, boxList, currentState.goalsPos)

            if nextState not in exploredStates:
                exploredStates.add(nextState)
                nextNode = currentNode.add_child(nextState)
                frontierNodes.append((nextNode, heuristic(nextState, boardMatrix)))

        frontierNodes.sort(key=lambda x: x[1])
    return 1, 0, len(exploredStates), len(frontierNodes)
    
def astar(initialGameState:GameState, boardMatrix, heuristic):
    exploredStates = set()
    frontierNodes = []

    tree = Tree(initialGameState)
    root = tree.get_root()
    exploredStates.add(initialGameState)
    frontierNodes.append((root, 0, heuristic(initialGameState, boardMatrix)))

    while len(frontierNodes) > 0:
        currentNode, initalF, initialH = frontierNodes.pop(0)
        currentState = currentNode.gameState

        # Verifies if the current state is a solution
        if currentState.isSolved():
            print("I won the game")
            return currentNode.get_root_path(currentNode), currentNode.get_depth(), len(exploredStates), len(frontierNodes) #TODO: Cambiarlo para que no termine la ejecucion
        
        # Get the neighbours of the current state (only the ones that the player can move to)
        neighbours = getNeighbours(boardMatrix, currentState.goalsPos, currentState.boxesPos, currentState.playerPos)

        # For each neighbour, generate the new state and add it to the frontierNodes if it is not explored
        for n in neighbours:
            boxList = currentState.boxesPos.copy()
            
            # If the neighbour is a box, move it
            if n in boxList:
                boxList.remove(n)
                newBoxPos = (n[0] + (n[0] - currentState.playerPos[0]), n[1] + (n[1] - currentState.playerPos[1]))
                boxList.append(newBoxPos)

            nextState = GameState(n, boxList, currentState.goalsPos)

            if nextState not in exploredStates:
                exploredStates.add(nextState)
                nextNode = currentNode.add_child(nextState)
                h = heuristic(nextState, boardMatrix)
                f = nextNode.depth + h
                frontierNodes.append((nextNode, f, h))

        frontierNodes.sort(key=lambda x: x[1])
    return 1, 0, len(exploredStates), len(frontierNodes)


def distanceHue(gameState:GameState, boardMatrix):
    boxList = gameState.boxesPos.copy()
    goalList = gameState.goalsPos.copy()

    neighbours = getNeighbours(boardMatrix, gameState.goalsPos, gameState.boxesPos, gameState.playerPos)

    
    distance = 0
    for box in boxList:
        minDistance = math.inf
        for goal in goalList:
            aux = abs(box[0] - goal[0]) + abs(box[1] - goal[1])
            if aux < minDistance:
                minDistance = aux
        distance += minDistance
    return distance