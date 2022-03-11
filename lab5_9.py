"""
주제:피보나치 수열 구하기
작성자:이승현
작성일:2017.10.23.
"""
def fibo(a):
    b=1
    c=0
    print(c)
    d=0
    for i in range(0,a-1):
        c=b
        b=d
        d=c+b


        print(d)
fibo(10)