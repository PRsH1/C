"""
주제: 조건문 연습
작성일: 17. 09. 20.
작성자: 201632023 이지훈
"""

"""
사용자로부터 정수를 입력받는다.
90점 이상이면 A, 80점 이상이면 B, 70점 이상이면 C, 60점 이상이면 D, 60점 미만이면 F를 학점으로 출력한다.
"""

score = int(input("점수 입력 : "))

if(score >= 90):
    print("학점 : A")
elif (score >= 80):
    print("학점 : B")
elif (score >= 70):
    print("학점 : C")
elif (score >= 60):
    print("학점 : D")
else:
    print("학점 : F")