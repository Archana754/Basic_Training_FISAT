
n,m,a,b=map(int,input().split())

if a*m<b:
    print(a*n)
else:
    print(((n//m)*b)+min(b,(n%m)*a))
