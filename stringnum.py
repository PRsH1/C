"""
문자열 S가 주어졌을 때, S의 서로 다른 부분 문자열의 개수를 구하는 프로그램을 작성하시오.

부분 문자열은 S에서 연속된 일부분을 말하며, 길이가 1보다 크거나 같아야 한다.

예를 들어, ababc의 부분 문자열은 (a, b, a, b, c), (ab, ba, ab, bc), (aba, bab, abc), (abab, babc), ababc가 있고, 서로 다른것의 개수는 12개이다.
ab(a,b,ab)+1
abc(a,b,c,ab,bc,abc)+3
abab(a,b,a,b,ab,ba,ab,aba,bab,abab)=10
bbccb=b,b,c,c,b,bb,bc,cc,cb,bbc,bcc,ccb,bbcc,bccb,bbccb=15개,12개
aacacc=(a,,c,),(aa,ac,ca,ac,cc,)(aac,aca,cac,acc),(aaca,acac,cacc),(aacac,acacc),aacacc=17개,21-4
abab=(,a,b,a,b),(ab,ba,ab),(aba,bab),(abab)=7개
aabb=(a,a,b,b)(,aa,ab,bb),(aab,abb),(aabb)=8
"""
s=input()
length=len(s)
str=[]
num=0
for i in range(0,length):
    for x in range (1,length+1):
        str.append(s[i:x])






print(len(set(str))-1)

