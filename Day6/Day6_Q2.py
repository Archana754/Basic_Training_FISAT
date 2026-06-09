#Find the min. no of steps to reduce N to 1 by two operations
#Oper 1:If even , divide it by 2
#Oper 2:If odd ,n+1 or n-1

def func(n):
    if n==1:
        return 0
    else:
        if(n%2==0):
            return 1+func(n//2)
        else:
            return 1+min(func(n-1),func(n+1))

n=int(input())
print(func(n))