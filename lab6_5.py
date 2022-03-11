"""
작성일:2017.11.20
작성자:이승현
주제:정규식
"""

import re
a=input("입력하시기 바랍니다:")
r=re.findall("[\d]+",a)#리스트로 리턴
for i in r:
    print(i)
b=input("스플릿입니다 입력해주세요:")
r2=re.split('[,]+',b)
for x in r2:
        print(x)
c=input("sub입니다 입력해주세요(/를 replace합니다):")
r3=re.sub("/","-",c)
print(r3)
result=(re.sub("[<>]",",","<2015><성지수><한국대학교>"))
print(result)
