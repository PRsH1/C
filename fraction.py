"""
주제:특수 연산자를 이용해 다양한 연산값 구하기
작성자:이승현
작성일:2017.11.05
."""
class fraction:
    def __init__(self,numer,denom):
        """
        :param numer: 분자
        :param denom: 분모
        """
        self.a=numer
        self.b=denom

    def __add__(self, other):#더하기의 특수연산자
        """
        :param other: 다른 분수
        :return:
        """
        numer1=(self.a*other.b)+(self.b*other.a)
        denom1=(self.b*other.b)
        return fraction.__str__(numer1,denom1)


    def __sub__(self, other):#뺄샘의 특수연산자
        """
        :param other: 다른 분수
        :return:
        """
        numer2=(self.a*other.b)-(self.b*other.a)
        denom2=(self.b*other.b)
        return fraction.__str__(numer2,denom2)
    def __str__(a,b):#문자열을 반환하는 특수연산자
        """

        :param b:
        :return: 문자열 반환
        """
        return  str(a) + "/" + str(b)



    def __lt__(self, other):#미만의 특수연산자
        """

        :param other: 다른 분수
        :return: 결과값 반환
        """
        if  (self.a/self.b) < (other.a/other.b):#조건 만족 시
            return True
        else:
            return False
    def __gt__(self,other):#초과의 특수연산자
        """
        :param other: 다른 분수
        :return: 결과값 반환
        """
        if (self.a / self.b) > (other.a / other.b):#조건 만족 시
            return True
        else:
            return False#결과값 반환
    def __eq__(self, other):#같다의 특수연산자
        """
        :param other: 다른 분수
        :return: 결과값 반환
        """
        if (self.a / self.b) == (other.a / other.b):#조건 만족 시
            return True
        else:
            return False
    def __ne__(self,other):#틀리다의 특수연산자
        """
        :param other: 다른 분수
        :return: 결과값 반환
        """
        if (self.a / self.b) != (other.a / other.b):#조건 만족 시
            return True
        else:
            return False
c1=fraction(2,4)
c2=fraction(4,7)
print(c1+c2)
print(c1-c2)
print(c1<c2)
print(c1>c2)
print(c1==c2)
print(c1!=c2)