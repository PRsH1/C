"""
사용자가 입력한 디렉토리 이동,사용자가 입력한 이름의 새 디렉토리 생성
사용자가 입력한 새 디렉토리 아래에 test디렉토리 생성
사용자가 입력한 새 디렉토리 포함하여 해당 디렉토리와 test디렉토리 삭제
삭제 후 사용자가 입력한 새 디렉토리의 부모 디렉토리(처음 디렉토리)의 파일목록 출력
과제제출시스템에 제출
만약 디렉토리가 경로에 존재 x시 예외처리 후 오류메세지 출력
"""
"""
주제:라이브러리
작성자:이승현
작성일:2017.11.28.
"""


import os
try:#예외처리 문장
    os.chdir(input())#작업할 디렉토리 입력받음
except FileNotFoundError:#만약 해당 디렉토리 없으면
    print("해당 디렉토리를 찾을 수 없습니다")#오류 출력
str=input()#새 디렉토리 이름 str에 저장
os.mkdir(str)#만들고
dict=os.getcwd()#현재 작업중인 디렉토리 검사
os.makedirs(dict+"\\"+str+"\\"+"test")#하위 디렉토리에 test생성
print(dict)#현재 디렉토리 출력
list=os.listdir(dict)#현재 작업중인 디렉토리의 파일과 폴더 리스트로 변환
print(list)#한번 출력해본다(사용자가 입력한 폴더가 잘 생성됬는지 확인하기 위함)
list3=os.listdir(dict+"\\"+str)#리스트 3에 사용자가 입력한 디렉토리의 하위 디렉토리와 파일들을 리스트 형태로 변환 후 저장
print(list3)#하위 디렉토리에 test가 잘 생성되었는지 확인
os.removedirs(dict+"\\"+str+"\\"+"test")#하위 디렉토리 test삭제,사용자가 입력한 디렉토리도 삭제한다
list2=os.listdir(dict)#list2에 해당 디렉토리 파일,폴더 리스트화한것 저장
for x in list2:#반복문 돌려서
    print(x)#출력



