import re
str=re.compile("a,e,i,o,u")#단어로 취급되므로
print(str.search("This is a test"))#none타입이 뜬다
print(re.search("[aeiou]","This is a test"))#이래야지 결과값 출력됨,aeiou중 i값이 This에 있으므로 2번쨰 요소 3번쨰 글자(span(2,3))으로 반환 가능)
print(re.search("a,e,i,o,u","This is a test"))
