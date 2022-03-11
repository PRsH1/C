import os
dict=input("작업할 디렉터리 입력:")
os.chdir(dict)
f=open("fruits.txt","r")
fruits=f.readlines()
for num in fruits:
    print(num)
