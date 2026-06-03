#second largest element


l=list(map(int,input().split()))
largest=0
large=0
for i in l:
    if i>largest:
        large=largest
        largest=i
    elif i>large and i!=largest:
        large=i
print(large)

# l=list(map(int,input().split()))
# largest=l[0]
# for i in l:
# if i>largest:                      #this code only applicable when large occurs before
# largest=i                          largest
# large=0
# for i in l:
#     if i>large and i!=largest:
#         large=i
# print(large)
