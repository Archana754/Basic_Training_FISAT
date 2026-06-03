l=list(map(int,input().split()))


#for jumping 1 position to left
# first=l[0]
# for i in range(0,len(l)-1,1):
#     l[i]=l[i + 1]
# ind=len(l)-1
# l[ind]=first
# print(l)
#
# #for jumping two position
#
# sec=l[0]
# for i in range(0,len(l)-1,1):
#     l[i]=l[i + 1]
# l[ind]=sec
# print(l)
#

# OR for jumping two position to left

n=len(l)
temp1=l[0]
temp2=l[n-1]

for i in range(0,len(l)-1,1):
    l[i]=l[i +1]
ind=len(l)-1
l[ind]=temp1
print(l)