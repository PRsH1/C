"""
밑변이 5개의 *로 구성된 직각 삼각형 출력
거꾸로 된 직각 삼각형 출력
"""
for x in range(1,6):
    print("*"*x)
a=5
while a>0:
    print("*"*a)
    a -= 1
for x in range(5,0,-1):
    print("*"*x)