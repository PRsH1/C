"""
주제:피보나치 수열 recursion이용하여 구하기
작성자:이승현
작성일:2017.10.27.
"""

def fibo(n):

    if n<2:
        return n
    else:

        return (fibo(n-1)+fibo(n-2))


for i in range(0,11):
        print(fibo(i))