# Merging two sorted list which is also sorted
#constraint : O(n)


l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
n1=len(l1)
n2=len(l2)
res=[]
i,j=0,0
while(i<n1 and j<n2):
    if(l1[i]<l2[j]):
        res.append(l1[i])
        i+=1
    else:
        res.append(l2[j])
        j+=1
while(i<n1):
    res.append(l1[i])
    i+=1
while(j<n2):
    res.append(l2[j])
    j+=1
print(res)