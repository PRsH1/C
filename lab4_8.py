"""
주제:
작성일:
작성자:
"""
#사용자로부터 수를 받아서 그 수의 약수를 구하시오

n=int(input("수하나를 입력하시오:"))
l=[]
for i in range(1,n+1):
    if n%i==0:
        print(i)
        l.append(i)
print(l)
