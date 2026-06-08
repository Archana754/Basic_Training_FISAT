# if correct password ,return true else false

str=input("Enter password")

i,j=0,0
flag=1
has_upper=False
has_digit=False
has_lower=False
has_space=False
has_special=False
for i in str:
    if i.isupper():
        has_upper=True
    elif i.islower():
        has_lower=True
    elif i.isdigit():
        has_digit=True
    elif i==" ":
        has_space=True
    else:
        has_special=True
if(len(str)>=8 and has_upper==True and has_digit==True and has_space==False and has_special==True):
    print("Valid Password")
else:
    print("Invalid Password")



