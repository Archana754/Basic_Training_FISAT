# right rotation k times

l=list(map(int, input().split()))
k=int(input("Enter the no. of times: "))
n=len(l)
k=k%n
def rotate(i,j):
    while i<j :
        l[i],l[j]=l[j],l[i]
        i+=1
        j-=1

rotate(0,n-1)
rotate(0,k-1)
rotate(k,n-1)
print(l)
