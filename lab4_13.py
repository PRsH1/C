"""
주제:알파벳 순서로 출력
작성일:2017.09.27
작성자:이현복
"""
a = str(input("단어 입력 : ")) # 단어를 입력받고 a에 저장
print(a) # a 출력
s=[] # s 리스트 정의
for x in range(0,len(a)): # 반복문
    s.append(a[x]) # s 리스트에 추가
s.sort() # s 알파벳 순으로 정렬
print(s) # s 출력
print(len(a)) # 길이 출력