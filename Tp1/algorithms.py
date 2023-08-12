from tree import Tree
from collections import deque

# https://docs.python.org/es/3/library/collections.html#collections.deque
# collections.deque es una implementación alternativa de colas sin límites con operaciones atómicas rápidas
# append() y popleft() que no requieren bloqueo y también soportan indexación.

def bfs(gameState):
    #return 1,2,3
    exploredNodes = []
    frontierNodes = deque()

    tree = Tree(gameState)
    root = tree.get_root()

    frontierNodes.append(root)
    while len(frontierNodes) > 0:
        current = frontierNodes.popleft()

        #TODO: Verificar si el nodo actual es la solución (Imprimirlo si lo es)

        #TODO: A cuales puedo ir desde este state?
        #TODO: Comparar como quedan los states de los nodos siguientes para no volver a recorrerlos
        #TODO: Generar nodos para los states a los que puedo ir y agregarlos a frontierNodes

        exploredNodes.append(current)


    
def dfs(gameState):
    return 1,2,3
    
def greedy(gameState, heuristic):
    return 1,2,3
    
def astar(gameState, heuristic):
    return 1,2,3

    


