#select consecutive k books with costs in list which give max sum of costs
# -brute force

cost=list(map(int,input().split()))
k=int(input("Enter no.of books"))
m=0

for i in range(len(cost)-k):
    sum=0
    for j in range(i,i+k):
        sum=sum+cost[i]
    m=max(m,sum)
print(m)





