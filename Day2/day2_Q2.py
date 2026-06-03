#print the elements in the lis which has occurred odd number of times

l=input().split()
res=[]
for i in l:
    if i not in res and l.count(i)%2!=0 :
        res.append(i)
print(res)