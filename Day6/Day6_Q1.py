#Recursion
# 1) 5 4 3 2 1 ,n=5 ==>Tail recursion

# def func(n):
#     if n==0:
#         return 0
#     else:
#         print(n,end=" ")
#         func(n-1)
# func(5)
#-----------------------------

# 2) 1 2 3 4 5 , n=5 ==>Head recursion
# def func(n):
#     if n==0:
#         return 0
#     else:
#         func(n-1)
#         print(n, end=" ")
# func(5)
# #------------------------------------

# 1 2 3 4 5 200 ,n=5

# def func(n):
#     if n==0:
#         return 200
#     else:
#         t=func(n-1)
#         print(n,end=" ")
#         return t
# print(func(5))
#--------------------------------

# 3) 10 8 6 4 2 ,n=10

# def func(n):
#     if n==0:
#         return 0
#     else:
#         print(n,end=" ")
#         func(n-2)
# func(10)
#--------------------------------

# 4) 2 4 6 8 10 ,n=10

# def func(n):
#     if n==0:
#         return 0
#     else:
#         func(n-2)
#         print(n,end=" ")
# func(10)
#-------------------------------

# 5) 5 4 3 2 1 2 3 4 5 , n=5
# def func(n):
#     if n==0 :
#         return 0
#     else:
#         print(n,end=" ")
#         func(n-1)
#         if n>1:
#             print(n,end=" ")
# func(5)
#------------------------------------

# 1 2 3 4 5 4 3 2 1 ,n=5

def func(n,m=0):
    if n==m:
        return 0
    else:
        print(m+1,end=" ")
        func(n,m+1)
        if m!=0:
            print(m,end=" ")
func(5)








