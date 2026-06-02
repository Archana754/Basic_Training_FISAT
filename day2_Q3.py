#Segregate the given list as even elements first in descending order and then
# odd elements next in ascending order
#constraints : can use one sort and one res[]

l=input().split()
l.sort()
res=[]
for i in l:
    if i%2!=0:
        res.append(i)
    else:
        res.insert(0,i)
print(res)

