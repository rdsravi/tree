class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def remove_child(self, child_node):
        if child_node in self.children:
            self.children.remove(child_node)

root = TreeNode("A")

# Adding children to the root node
child1 = TreeNode("B")
child2 = TreeNode("C")
root.add_child(child1)
root.add_child(child2)

# Adding children to child1 node
child3 = TreeNode("D")
child4 = TreeNode("E")
child1.add_child(child3)
child1.add_child(child4)

# Adding children to child2 node
child5 = TreeNode("F")
child2.add_child(child5)
