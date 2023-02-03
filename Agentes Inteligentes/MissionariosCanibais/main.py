import functions
from anytree import Node, RenderTree


root = functions.createTree()
explored = []
goal = "m3c3m0c0E"

functions.printTree(root)
functions.breadthFirstSearch(root, goal)
