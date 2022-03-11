import re#정규식
str=re.compile("a")#컴파일("a")
print(str.search("apple"))#apple단어에서 서치하라
print(re.search("b","apple"))#컴파일"b",apple에서 서치하라