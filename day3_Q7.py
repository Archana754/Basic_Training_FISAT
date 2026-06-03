#highest repeating element-use dictionary for frequency questions

l=[1,3,1,3,1,2,1,4,2,2,2,2,2]
d={}
for i in l:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
ele1,ele2,max1,max2=0,0,0,0
for i in d:
    if d[i]>max1:
        max1=d[i]
        ele1=i
print(d)
print(ele1)
