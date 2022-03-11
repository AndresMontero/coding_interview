# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        # Write your code here.
        # Time O(nodes + edges)
        # Space O(nodes)
        queue = []

        queue.insert(0, self)
        while len(queue) >= 1:
            current = queue.pop()
            array.append(current.name)
            for children in current.children:
                queue.insert(0, children)

        return array

    def depth_first_search(self, array):
        # Write your code here.
        # Time O(nodes + edges)
        # Space O(nodes)
        stack = []

        stack.append(self)
        while len(stack) >= 1:
            current = stack.pop()
            array.append(current.name)
            for children in current.children:
                stack.append(children)

        return array


if __name__ == '__main__':
    graph = Node("A")
    graph.addChild("B").addChild("C").addChild("D")
    graph.children[0].addChild("E").addChild("F")
    graph.children[2].addChild("G").addChild("H")
    graph.children[0].children[1].addChild("I").addChild("J")
    graph.children[2].children[0].addChild("K")
    print(graph.breadthFirstSearch([]))
    print(graph.depth_first_search([]))
