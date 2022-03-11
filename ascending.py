num=input()

a=0
ac=0
b=0
dc=0
for i in num:
    d=int(i)
    if d>a:
        a=d
        ac+=1
        dc-=1
    elif a>d:
        b=d
        dc+=1
        ac-=1

if ac>dc:
    print("ascending")
elif dc>ac:
    print("decending")



