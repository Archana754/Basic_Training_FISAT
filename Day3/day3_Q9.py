#reverse a list without using reverse function

l=list(map(int,input().split()))

for i in range(0,len(l),1):
    for j in range(len(l)-1,-1,-1):
        temp=l[i]
        l[i]=l[j]
        l[j]=temp
print(l)