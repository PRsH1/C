num=(input("숫자를 입력하세요:"))
num=num.split()
str=""
re=0
for x in range(0,len(num)):
    str+=num[x]
while(1):
    try:
        if re==0:
            str2=int(str)
        else:
            for x in range(0, len(num)):
                str += num[x]
            str2=int(str)

        break
    except ValueError:
        num=input("숫자가 아닙니다 다시 입력해주세요:")
        num=num.split()
        str=""
        re+=1
list=[]
for i  in str:
    list.append(i)
list2=sorted(set(list))
list3=sorted(set(list))
list2.sort()
list3.reverse()
if len(list)==1:
    print("single")
else:
    if list==list2:
        print("ascending")
    elif list==list3:
        print("decending")

    else:
        print("Mixed")



