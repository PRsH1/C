"""
사용자가 입력한 영문자를 아래와 같이 출력
"""
a=str(input("문자 입력:"))
b=" "
for x in range(0,len(a)):
    print(b*x+a[x:len(a)])
