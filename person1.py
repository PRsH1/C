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
    def __eq__(self,p):
        if(self.num==p.num):
            return True
        else:
            return False
