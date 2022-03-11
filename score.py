"""
주제:readlines와 split을 이용하여 텍스트파일에 쓰여진 데이터 읽고 연산해보기
작성일:2017.12.09
작성자:이승현
"""


import os#디렉터리를 입력해야 하기 때문에 os모듈을 import시킨다
try:#트라이
    dict=input("작업하고 싶은 디렉터리를 입력하세요:")#디렉터리 입력 안내문 출력,디렉터리 입력받음
    os.chdir(dict)#작업할 디렉터리로 이동
    f=open("score.txt","r")#score.txt를 open
except FileNotFoundError:#파일이 없으면(FileNotFoundError 발생 시)
    print("파일이 존재하지 않습니다")#오류 메세지 출력
score=f.readlines()#스코어 텍스트 파일에 있는 텍스트를 읽는다
result1=0#학생 당 평균 점수를 저장할 변수 result1 0으로 초기화
sum=0#총 점수의 평균을 저장할 변수 sum 0으로 초기화
kor=0#국어 점수의 평균을 저장할 변수 kor 0으로 초기화
math=0#수학 점수의 평균을 저장할 변수 math 0으로 초기화
eng=0#영어 점수의 평균을 저장할 변수 eng 0으로 초기화
str2=""#score리스트형을 문자형으로 바꾼 뒤 저장할 변수 str2
list1=[]#각 학생의 점수를 리스트로 관리하기 위한 리스트 변수 지정

print(score)
for x in range(0,len(score)):#반복문
    str1=str(score[x])#스플릿을 하기 위해 str1에 리스트형 변수 score을 문자열화 시킨 것을 저장

    str2=str1.split(":")#str에 있는 문자들을 split하여 : 제거
    name=str2[0]#학생들의 이름을 저장할 변수 name
    for i in range(1,4):#반복문
        d = str2[i]#각 요소를 d에 저장
        sum += int(d)#d에 저장된 문자형 숫자들을 형변환하여 sum에 더한다
        result1 += int(d)#마찬가지로 result1에 더한다
        if i==1:#만약 요소 1이면 국어점수이므로
            kor+=int(d)#국어점수를 더한다
        elif i==2:#요소 2면 영어점수이므로
            eng+=int(d)#영어점수를 더한다

        elif i==3:#요소 3이면 수학점수이므로
            math+=int(d)#수학점수를 더한다
            result2=result1#result1의 숫자를 result2로 전이
            list1.append(round(result2/3,1))#학생 평균점수 변수를 리스트로 보냄,소수점 첫째자리까지 출력하기 위해 round함수 사용
            result1=0#0으로 초기화



print("==== 전체 평균 ===\n",round(sum/30,1))#전체 평균 출력,소수점 첫째자리 출력 위해 round 사용
print("==== 각 학생 평균 ===")#각 학생 평균
for u in range(0,len(score)):#반복문
    str3=str(score[u])#위와 동일
    str4=str3.split(":")#위와 동일
    print(str4[0]+":",list1[u])#학생들 이름과 리스트에 저장된 숫자들 출력
print("==== 과목 평균 ====")#과목 평균 출력
print("국어 평균:", kor/10)
print("영어 평균:",eng/10)
print("수학 평균:",math/10)

