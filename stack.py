stack=[]
num=int(input())
for i in range(0,num):
    str=input()
    if str=="pop":
        if len(stack)==0:
            print("-1")
        else:
            print(stack[0])
            del stack[0]


    elif str=="size":
        print(len(stack))
    elif str=="empty":
        if len(stack)==0:
            print("1")
        else:
            print("0")
    elif str=="top":
        if len(stack)==0:
            print("-1")
        else:
            print(stack[0])
    elif str[0:4]=="push":
        stack.insert(0,str[5:])



