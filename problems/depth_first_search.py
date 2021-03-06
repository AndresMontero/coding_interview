class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        # time O(n + e) nodes + edges
        # Space O(n)
        # Write your code here.
        array.append(self.name)

        if len(self.children) > 0:
            for i in range(len(self.children)):
                self.children[i].depthFirstSearch(array)

        return array

if __name__ == '__main__':
    graph = Node("A")
    graph.addChild("B").addChild("C").addChild("D")
    graph.children[0].addChild("E").addChild("F")
    graph.children[2].addChild("G").addChild("H")
    graph.children[0].children[1].addChild("I").addChild("J")
    graph.children[2].children[0].addChild("K")

    depth_first_search = graph.depthFirstSearch([])
    print(depth_first_search)