class Node(object):
    """Represents a node in a tree"""
    def __init__(self, gameState, children = None, parent = None, depth = 0):
        self.parent = parent
        self.children = []
        self.depth = depth
        self.gameState = gameState
        if children is not None:
            for child in children:
                self.add_child(child)
            
    def is_root(self):
        return self.parent is None
    
    def is_leaf(self):
        return len(self.children) == 0
    
    def depth(self):
        return self.depth
    
    def game_state(self):
        return self.gameState
    
    def add_child(self, node):
        assert isinstance(node, Node)
        node.parent = self
        self.children.append(node)
    
    def remove_child(self, node):
        assert isinstance(node, Node)
        node.parent = None
        self.children.remove(node)
    

class Tree(object):
    """Represents a tree"""
    def __init__(self, root):
        self.root = root
    
    def get_root(self):
        return self.root
    
