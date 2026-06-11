#Height of a binary tree
#https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree/problem?isFullScreen=true


def height(root):
    if root is None:
        return -1
    return 1+max(height(root.left),height(root.right))
