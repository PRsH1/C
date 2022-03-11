import os
dict=input("작업할 디렉터리 입력:")
os.chdir(dict)

f=open("fruits.txt","r+")

fruits=f.tell()
fruitsdata=f.readline()
print(fruits)
print(fruitsdata[0:1])
print(f.tell())
print(f.readline())
print(f.tell())
print(f.readline())
print(f.tell())
print(f.readline())
print(f.tell())
print(f.readline())
print(f.tell())
print(f.readline())
print(f.tell())


