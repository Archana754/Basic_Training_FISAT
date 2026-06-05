#select consecutive k books with costs in list which give max sum of costs
# -optimal

cost=list(map(int,input().split()))
k=int(input("Enter no.of books"))
n=len(cost)
s=sum(cost[:k])
m=s
for i in range(1,n-k+1):
    s=s-cost[i-1]+cost[i+k-1]
    m=max(m,s)
print(m)
