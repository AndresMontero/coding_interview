# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None

    def addDescendants(self, *descendants):
        for descendant in descendants:
            descendant.ancestor = self

def new_trees():
    ancestralTrees = {}
    for letter in list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        ancestralTrees[letter] = AncestralTree(letter)
    return ancestralTrees


def depth_first_search(topAncestor, descendantOne):
    stack = [descendantOne]
    array = []
    while stack:
        current = stack.pop()
        array.append(current)
        if current.ancestor is not None:
            stack.append(current.ancestor)

    return array


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    # Write your code here.
    # Time O(depth_a + depth_b)
    # Space O(depth_a + depth_b)
    path_a = []
    path_b = []

    path_a = depth_first_search(topAncestor, descendantOne)
    path_b = depth_first_search(topAncestor, descendantTwo)

    print(path_a)
    print(path_b)

    if len(path_a) >= len(path_b):
        for node in path_b:
            if node in path_a:
                print(node.name)
                return node
    else:
        for node in path_a:
            if node in path_b:
                print(node.name)
                return node


def find_depth(topAncestor, descendantOne):
    current = descendantOne
    depth = 0
    while current.ancestor:
        current = current.ancestor
        depth += 1
    return depth


def getYoungestCommonAncestor_2(topAncestor, descendantOne, descendantTwo):
    # Write your code here.
    # Time O(d) where d is the depth of tree
    # Space O(1) c
    depth_a = find_depth(topAncestor, descendantOne)
    depth_b = find_depth(topAncestor, descendantTwo)

    if depth_a > depth_b:
        diff = depth_a - depth_b
        steps = 0
        while steps < diff:
            descendantOne = descendantOne.ancestor
            steps += 1
    else:
        diff = depth_b - depth_a
        steps = 0
        while steps < diff:
            descendantTwo = descendantTwo.ancestor
            steps += 1

    while descendantOne != descendantTwo:
        descendantOne = descendantOne.ancestor
        descendantTwo = descendantTwo.ancestor

    return descendantOne


if __name__ == '__main__':
    trees = new_trees()
    trees["A"].addDescendants(trees["B"], trees["C"])
    trees["B"].addDescendants(trees["D"], trees["E"])
    trees["D"].addDescendants(trees["H"], trees["I"])
    trees["C"].addDescendants(trees["F"], trees["G"])

    print(getYoungestCommonAncestor(trees["A"], trees["E"], trees["I"]))
    print(getYoungestCommonAncestor_2(trees["A"], trees["E"], trees["I"]))

