# OR for jumping k position--brute force

# l=list(map(int,input().split()))
# n=len(l)
# k=int(input("Enter the  no. of times"))
# while(k>0):
#     temp = l[0]
#     for i in range(0, len(l) - 1, 1):
#         l[i] = l[i + 1]
#     ind = len(l) - 1
#     l[ind] = temp
#     k-=1
# print(l)

# left rotation k times -optimal solution

# l=list(map(int, input().split()))
# k=int(input("Enter the no. of times: "))
# n=len(l)
# k=k%n
# l[0:k]=l[0:k][::-1]
# l[k:n]=l[k:n][::-1]
# l[:]=l[::-1]
#
# print(l)

#OR

l=list(map(int, input().split()))
k=int(input("Enter the no. of times: "))
n=len(l)
k=k%n
def rotate(i,j):
    while i<j :
        l[i],l[j]=l[j],l[i]
        i+=1
        j-=1

rotate(0,k-1)
rotate(k,n-1)
rotate(0,n-1)
print(l)
