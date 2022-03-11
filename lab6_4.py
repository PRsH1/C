import re
r=re.compile("tes?t")#?바로앞의 글자는 없어도 되지만 뒤 글자는 반드시 있어야 함,?앞의 글자가 0개또는 1개일 경우에만 매칭이 된다
r1=re.compile("akbcs?o")
d1=re.compile("akbcs*o")#바로앞의 문자가 존재 x 이거나 개수에 상관없이 존재
d=re.compile("tes*t")
e=re.compile("tes+t")#바로앞의 문자가 한번 이상 존재
print(r.search("test"))#매칭
print(r.search("tet"))#te가 있으므로 s를 제외 (1개)까지는 괜찮으므로 매칭
print(r.search("tesst"))#s가 2개 들어가 있으므로 논타입
print(r.search("tst"))#t(e)s 즉 e가 제외되었으므로 패턴이 맞지 않음=논타입 반환,반드시 순서대로 써야 함
print(r.search("tes"))#뒤에 반드시 와야 할 문자 t가 없으므로 논타입
print(r1.search("akbco"))#s가 제외되어도 패턴 자체는 (akbc)맞으므로 s 1개는 제외되어도 결과값 반환 가능
print(r1.search("akbso"))#패턴이 맞지 않으므로 논타입
print(d.search("test"))
print(d.search("tet"))
print(d.search("tesst"))#?과 달리 개수에 상관없이 결과값 반환,패턴은 (test형식)맞음
print(d.search("tst"))#패턴이 맞지 않으므로 논타입
print(d.search("tes"))#뒤에 반드시 와야 할 t가 없으므로 반환 불가
print(d1.search("akbcsssssso"))#패턴 ok 글자수 상관없으므로 결과값 반환 가능
print(d1.search("akbcccso"))#패턴이 맞지 않으므로(akbcs까지는 보존해야함)논타입 반환
print(d1.search("akbco"))
print(e.search("test"))
print(e.search("tet"))#s가 누락되었으므로 논타입,한번이상존재해야함
print(e.search("tesst"))#반환
print(e.search("teeest"))#패턴 x 반환 x