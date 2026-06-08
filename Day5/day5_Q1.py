#Find the longest subarray whose sum is <= k
#Dynamic Sliding Window

list=list(map(int,input().split()))
k=int(input())
r,l=0,0
m=0
s=0
while r<len(list):
    s+=list[r]
    while s>k:
        s-=list[l]
        l+=1
    length=r-l+1
    m=max(m,length)
    r+=1
print(m)