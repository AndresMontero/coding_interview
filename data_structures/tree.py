class TreeNode:
    def __init__(self, name, designation):
        self.data = {name: designation}
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self, choice, level_limit=0):
        curr_level = self.get_level()
        if curr_level <= level_limit:
            spaces = ' ' * curr_level * 3
            prefix = spaces + "|__" if self.parent else ""

            if choice == 'name':
                print(prefix + [key for key in self.data.keys()][0])

            elif choice == 'designation':
                print(prefix + [key for key in self.data.values()][0] )

            else:
                print(prefix + [key for key in self.data.keys()][0] + '-' + [key for key in self.data.values()][0])


            if self.children:
                for child in self.children:
                    child.print_tree(choice, level_limit)

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

def build_product_tree():
    root = TreeNode("Nilipul", "CEO")

    technolgy = TreeNode("Chinmay","CTO")
    infra_head = TreeNode("Vishwa","Infrastructure Head")
    infra_head.add_child(TreeNode("Dhaval", "Cloud Manager"))
    infra_head.add_child(TreeNode("Abhijit", "App Manager"))
    technolgy.add_child(infra_head)
    technolgy.add_child(TreeNode("Aamir", "Application Head"))

    hr = TreeNode("Gels", "HR Head")
    hr.add_child(TreeNode("Peter", "Recruitment Manager"))
    hr.add_child(TreeNode("Wagas", "Policy Manager"))


    root.add_child(technolgy)
    root.add_child(hr)

    root.print_tree('name', 4)

if __name__ == '__main__':
    build_product_tree()