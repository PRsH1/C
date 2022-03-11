import os
dict=input("디렉터리 입력:")
os.chdir(dict)

f=open("fruits.txt","w")
t=input("입력할 문장을 입력하세요:")
t2=input("두번째 과일을 입력하세요:")
t3=input("세번쨰 과일을 입력하세요:")
f.write(t+"\n"+t2+"\n"+t3+"\n")
f.close()