from tree import Tree
from collections import deque
from game import *
from gameState import GameState
import math


# https://docs.python.org/es/3/library/collections.html#collections.deque
# collections.deque es una implementación alternativa de colas sin límites con operaciones atómicas rápidas
# append() y popleft() que no requieren bloqueo y también soportan indexación.


#TODO: Extraer comportamientos comunes a todos los metodos de busqueda
def bfs(initialGameState:GameState, boardMatrix, goals):
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
        if currentState.isSolved(goals):
            return currentNode.get_root_path(currentNode), currentNode.get_depth(), len(exploredStates), len(frontierNodes)
        
        # Get the neighbours of the current state (only the ones that the player can move to)
        neighbours = getNeighbours(boardMatrix, goals, currentState.boxesPos, currentState.playerPos)

        # For each neighbour, generate the new state and add it to the frontierNodes if it is not explored
        for n in neighbours:
            boxList = currentState.boxesPos.copy()

            # If the neighbour is a box, move it
            if n in boxList:
                boxList.remove(n)
                newBoxPos = (n[0] + (n[0] - currentState.playerPos[0]), n[1] + (n[1] - currentState.playerPos[1]))
                boxList.append(newBoxPos)

            nextState = GameState(n, boxList)
            
            if nextState not in exploredStates:
                exploredStates.add(nextState)
                nextNode = currentNode.add_child(nextState)
                frontierNodes.append(nextNode)

    return 1, 0, len(exploredStates), len(frontierNodes)

def dfs(initialGameState:GameState, boardMatrix, goals):
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
        if currentState.isSolved(goals):
            # print("I won the game")
            return currentNode.get_root_path(currentNode), currentNode.get_depth(), len(exploredStates), len(frontierNodes) #TODO: Cambiarlo para que no termine la ejecucion
        
        # Get the neighbours of the current state (only the ones that the player can move to)
        neighbours = getNeighbours(boardMatrix, goals, currentState.boxesPos, currentState.playerPos)

        # For each neighbour, generate the new state and add it to the frontierNodes if it is not explored
        for n in neighbours:
            boxList = currentState.boxesPos.copy()

            # If the neighbour is a box, move it
            if n in boxList:
                boxList.remove(n)
                newBoxPos = (n[0] + (n[0] - currentState.playerPos[0]), n[1] + (n[1] - currentState.playerPos[1]))
                boxList.append(newBoxPos)

            nextState = GameState(n, boxList)

            if nextState not in exploredStates:
                exploredStates.add(nextState)
                nextNode = currentNode.add_child(nextState)
                frontierNodes.append(nextNode)

    return 1, 0, len(exploredStates), len(frontierNodes)


def greedy(initialGameState:GameState, boardMatrix, goals, heuristic):
    exploredStates = set()
    frontierNodes = []

    tree = Tree(initialGameState)
    root = tree.get_root()
    exploredStates.add(initialGameState)
    frontierNodes.append((root, heuristic(initialGameState, goals)))

    while len(frontierNodes) > 0:
        currentNode, _ = frontierNodes.pop(0)
        currentState = currentNode.gameState

        # Verifies if the current state is a solution
        if currentState.isSolved(goals):
            # print("I won the game")
            return currentNode.get_root_path(currentNode), currentNode.get_depth(), len(exploredStates), len(frontierNodes) #TODO: Cambiarlo para que no termine la ejecucion
        
        # Get the neighbours of the current state (only the ones that the player can move to)
        neighbours = getNeighbours(boardMatrix, goals, currentState.boxesPos, currentState.playerPos)

        # For each neighbour, generate the new state and add it to the frontierNodes if it is not explored
        for n in neighbours:
            boxList = currentState.boxesPos.copy()
            
            # If the neighbour is a box, move it
            if n in boxList:
                boxList.remove(n)
                newBoxPos = (n[0] + (n[0] - currentState.playerPos[0]), n[1] + (n[1] - currentState.playerPos[1]))
                boxList.append(newBoxPos)

            nextState = GameState(n, boxList)

            if nextState not in exploredStates:
                exploredStates.add(nextState)
                nextNode = currentNode.add_child(nextState)
                frontierNodes.append((nextNode, heuristic(nextState, goals)))

        frontierNodes.sort(key=lambda x: x[1])
    return 1, 0, len(exploredStates), len(frontierNodes)
    
def astar(initialGameState:GameState, boardMatrix, goals, heuristic):
    exploredStates = set()
    frontierNodes = []

    tree = Tree(initialGameState)
    root = tree.get_root()
    exploredStates.add(initialGameState)
    frontierNodes.append((root, 0, heuristic(initialGameState, goals)))

    while len(frontierNodes) > 0:
        currentNode, initalF, initialH = frontierNodes.pop(0)
        currentState = currentNode.gameState

        # Verifies if the current state is a solution
        if currentState.isSolved(goals):
            # print("I won the game")
            return currentNode.get_root_path(currentNode), currentNode.get_depth(), len(exploredStates), len(frontierNodes) #TODO: Cambiarlo para que no termine la ejecucion
        
        # Get the neighbours of the current state (only the ones that the player can move to)
        neighbours = getNeighbours(boardMatrix, goals, currentState.boxesPos, currentState.playerPos)

        # For each neighbour, generate the new state and add it to the frontierNodes if it is not explored
        for n in neighbours:
            boxList = currentState.boxesPos.copy()
            
            # If the neighbour is a box, move it
            if n in boxList:
                boxList.remove(n)
                newBoxPos = (n[0] + (n[0] - currentState.playerPos[0]), n[1] + (n[1] - currentState.playerPos[1]))
                boxList.append(newBoxPos)

            nextState = GameState(n, boxList)

            if nextState not in exploredStates:
                exploredStates.add(nextState)
                nextNode = currentNode.add_child(nextState)
                h = heuristic(nextState, goals)
                f = 1 + nextNode.depth + h
                frontierNodes.append((nextNode, f, h))

        frontierNodes.sort(key=lambda x: x[1])
    return 1, 0, len(exploredStates), len(frontierNodes)


def manhattan(gameState: GameState, goals):
    boxList = gameState.boxesPos

    distance = 0
    for box in boxList:
        minDistance = min(abs(box[0] - goal[0]) + abs(box[1] - goal[1]) for goal in goals)
        distance += minDistance
    return distance

def combined(gameState: GameState, goals):
    # Similar to Manhattan but account for alignment, a solution is better if the box is already aligned with a goal
    # An aligned solution only requires to push the box
    boxList = gameState.boxesPos

    distance = 0
    for box in boxList:
        minDistanceWithTurns = float('inf')
        for goal in goals:
            manhattanDistance = abs(box[0] - goal[0]) + abs(box[1] - goal[1]) # Same manhattan distance
            turnsNeeded = 0 if (box[0] - goal[0]) * (box[1] - goal[1]) == 0 else 1
            distanceWithTurns = manhattanDistance + turnsNeeded * 2 # Account for turns needed to align with goal
            minDistanceWithTurns = min(minDistanceWithTurns, distanceWithTurns)
        distance += minDistanceWithTurns
    return distance
