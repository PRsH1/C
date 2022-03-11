"""
주제:클래스
작성자:이승현
작성일:2017.11.06
1.intset클래스는 정수들 집합 정수를 관리하는 리스트 selfvals를 에트리뷰트로 가짐

"""
class intset:#클래스 정의 키워드
    def __init__(self):#초기화(생성자)특수매서드,self(객체 자신)매개 변수 받음
        self.valse=[]#리스트 초기화

    def insert(self,number):#number매개변수 받아
        if str(number) not in self.valse:
            return self.valse.append(number)#self.valse데이터 타입은 리스트이므로 append사용 가능
    def involve(self,num2):#매개변수 받아서(self는 데이터 타입(self는  intset num2는 int)
        if num2 in self.valse:
            return True
        else:
            return False
    def remove(self,num3):#num3매개변수 받음
        if num3 in self.valse:
            return self.valse.remove(num3)
        else:
            print("잘못된 수입니다")
    def __str__(self):#문자열 함수
        self.valse.sort()#리스트 타입이므로 sort함수 가능
        return str(self.valse)#리스트 타입이므로 str로 캐스팅하여 반환
s=intset()#클래스 호출 1번째
while(1):
    num=int(input())
    if num==0:
        break
    else:
        s.insert(num)#insert함수로 호출
        num=5
s.insert(3)
s.insert(7)
print(s)
print(s.involve(8))
print(s.involve(3))
s.remove(3)#remove함수 호출
s.remove(4)
print(s)






