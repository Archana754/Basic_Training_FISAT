#Level order traversal
#https://www.hackerrank.com/challenges/tree-level-order-traversal/problem?isFullScreen=true

def levelOrder(root):
    #Write your code here
    q=[]
    q.append(root)
    while q:
        ele=q.pop(0)
        print(ele,end=" ")
        if ele.left:
            q.append(ele.left)
        if ele.right:
            q.append(ele.right)