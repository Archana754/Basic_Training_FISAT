
s=input()
cnt=1
k=0
res=""
for i in range(1,len(s)):
    if s[k]==s[i]:
        cnt+=1
    else:
        res+=s[i-1]+str(cnt)
        k=i
        cnt=1
res+=s[-1]+str(cnt)
print(res)



