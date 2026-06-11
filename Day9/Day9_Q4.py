#preorder tree
#https://www.hackerrank.com/challenges/tree-preorder-traversal/problem?isFullScreen=true


def preOrder(root):
    #Write your code here
    if root is None:
        return
    print(root.info,end=" ")
    preOrder(root.left)
    preOrder(root.right)