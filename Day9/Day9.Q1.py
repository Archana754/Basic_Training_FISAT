# Tree Inorder

class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
class BST:

    def __init__(self):
        self.root=None
    def insert(self,node,data):
        if node is None:
            return Node(data)
        if data<node.data:
            node.left=self.insert(node.left,data)
        elif data>node.data:
            node.right=self.insert(node.right,data)
        return node

    def inorder(self,root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.data)
        self.inorder(root.right)


tree =BST()
tree.root=tree.insert(tree.root,5)
tree.root=tree.insert(tree.root,6)
tree.root=tree.insert(tree.root,7)
tree.root=tree.insert(tree.root,8)

tree.inorder(tree.root)


