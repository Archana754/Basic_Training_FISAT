#Print the list after deleting the duplicating elements in it.

l=input().split()
res=[]
for i in l:
    if i not in res :
        res.append(i)
print(res)



