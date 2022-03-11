"""
사용자로부터 5개의 숫자를 입력받아, 이를 리스트에 저장한후 합과 평균을 구하여 출력
"""
s=[]
for x in range(0,5):
    a = int(input("수 입력"))
    s.append(a)
sum=0
for x in range(0,5):
    sum+=s[x]
print("합 : %d, 평균 : %d" %(sum,sum/5))