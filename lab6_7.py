"""
주제:익셉트(예외처리)
작성자:이승현
작성일:2017.11.22.
"""
n=0
def divide(x,y):#디바이드 함수 정의 매개변수 x,y로 받음
    try:
        result=x//y#리절트에 몫 저장
        return print("몫:",result)#결과 반환

    except ZeroDivisionError:#만약 제로디비전에러 발생 시
        return print("0으로 나눌 수 없습니다")#오류메세지 출력

while(1):
    if n==1:
        break
    divide(int(input("첫번째 수:")),(int(input("두번째 수:"))))#함수 호출(입력받는 것도 출력문에 포함한다)
