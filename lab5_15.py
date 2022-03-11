"""
주제:계승
작성자:이승현
작성일:2017.11.08.
"""
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def getOlder(self):
        return self.age+1
    def __str__(self):
        return "이름:"+self.name+" "+"나이:"+str(self.age)
    def __eq__(self, other):#서로 다른 객체는 원래 False값이 나오는데(이름이 같아도) 이 함수를 씀으로써 재정의 함
        if self.name==other.name:
            return True
        else:
            return False
class sturdent(person):
    def __init__(self,name,age,grade,num):
        person.__init__(self,name,age)
        self.grade=grade
        self.num=num

    def upgrade(self, a=1):
        if a + self.grade > 4:
            print("학년이 초과되었습니다 다시 입력해주세요")
        else:
            print(self.grade + a)
    def print(self):
        return print("이름:"+self.name+"\n"+"나이:"+str(self.age)+"\n"+"학번:"+str(self.num)+"\n"+"이름:"+str(self.name)+"\n"+"학년:"+str(self.grade))
    def __eq__(self,other):
        if(self.num==other.num):
            return True
        else:
            return False

p=person("나야나",20)
p2=person("나야나",50)
p3=person("Donald J Trump",71)
print(p==p2)
print(p==p3)

s=sturdent("이승현",20,1,201732022)
s.print()

s1=sturdent("그래서",30,2,20193202)
print(s==s1)
#print(p==s)는 person 클래스에 num인수가 없으므로 작동 불능
#p와 s를 비교하고싶으면 P.__eq__(s)를 쓰자
print(p.__eq__(s))
p.getOlder()#겟오더 함수 호출
print(p)
s.getOlder()
print(s)
#p.upgrade()<== 작동 안함
s.upgrade()#작동함