#https://www.hackerrank.com/challenges/is-binary-search-tree/problem?isFullScreen=true

def check_binary_search_tree_(root):
    res =[]
    def inorder(root):
        if root is None:
            return 0
        inorder(root.left)
        res.append(root.data)
        inorder(root.right)
    inorder(root)
    for i in range(len(res ) -1):
        if(res[i]>=res[i+1]):
            return False
        return True
