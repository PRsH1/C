import os
dict=input("작업할 디렉터리 입력:")
os.chdir(dict)
f=open("fruits.txt","a")
list=[]
for i in range(0,3):
    p=input("과일을 입력하세요:")
    list.append(p)

    f.write(list[i] + "\n")

f.close()

