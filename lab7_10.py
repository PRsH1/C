import os
dict=input("작업할 디렉터리 입력:")
os.chdir(dict)

f=open("fruits.txt","r+")

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
print(f.readline())
f.seek(int(input()))
f.write(input())
fruits=f.readlines()
for food in fruits:
    print(food)