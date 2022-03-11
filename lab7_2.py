import os
print(os.getcwd())
try:
    dict=os.chdir(input())
except FileNotFoundError:
    print("입력한 디렉토리는 존재하지 않습니다")
x=os.listdir(dict)
for s in x:
    print(s)
