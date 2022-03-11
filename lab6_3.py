import re

print(re.search("^a","aThis is a test"))#search:string전체가 주어진 패턴과 동일한지 검사하여 매치될 경우 결과 반환,^(문자)주어진 철자로 시작하면 반환함
print(re.match("^a","aThis is a test"))#이 친구는 a가 처음부터 있으므로 결과 반환 가능
print(re.search("e$","This is a teste"))#span(요소 n번쨰 값,실제 글자 갯수 값),(이 구문의 경우 (14번째 요소,15번쨰 글자)가 반환되었음.(문자)$:주어진 철자로 끝나면 반환
print(re.match("e$","This is a teste"))#매치는 완전히 일치해야 결과값 반환,시작부터검사하므로(문자열의 처음이 정규식과 부합해야함)
print(re.match("e$","e"))
print(re.search("^a","This is a test"))#해당 값 없으므로 반환 없음
print(re.search("e$","This is a test"))#해당 값 없으므로 반환 값 없음
