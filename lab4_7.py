"""
주제: for반복문
작성일: 2017.09.25.
작성자:임석현
"""
l=[1,3,5]
for i in range(1,5,2):
    print(l)
s="성공회대학교"
for n in s:
    print(n)
#1에서 부터 100까지의 합을 구하시오
sum=0
for i in range(1,101):
    sum+=i
print("합",sum)
#1에서 100까지의 3의 배수의 합    for i in range(99.0,-3):
sum1=0
for i in range(99,0,-3):
    sum1+=i
print(sum1)
#1에서 100까지의 합을 while을 이욯하여 구하시오
sum2=0
i=1
while i<=100:
    sum2+=i
    i+=1
print(sum2)
sum2=0
i=1
while i<=100:
    i += 1
    if (i%3!=0):
        continue
    sum2+=i

print("합",sum2)