"""
주제: naver의 검색 open api 예제를 새로운 접속 방법으로 수정
작성일: 2017. 9. 14.
작성자: 홍은지
"""

import os
import sys
import urllib.request

#naver openapi를 사용하기 위한 새로운 설정 방법. client_id와 clinet_secret를
#부여받아 request할 때 전달

client_id = "jIdXqLS7Gr8qnOWpguE1"
client_secret = "sr9inMMWI7"

sort = '&sort=sim'
start = '&start=100'
display = '&display=10'

#검색할 단어를 직접 입력받음
encText = urllib.parse.quote_plus(str(input("검색어를 입력하세요: ")))

#blog를 검색하도록 설정. 결과를 xml로 받도록 설정.
url = "https://openapi.naver.com/v1/search/blog.xml?query=" \
      + encText + sort + start +display # xml 결과

#blog를 검색하는 코드
#url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과

#request 설정
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)

#결과를 저장할 파일 생성
file = open("C:\\Python34\\naver_blogs.txt","w",encoding='utf-8')

#BeautifulSoup 모듈 사용을 위한 설정
from bs4 import BeautifulSoup

#request를 open하여 읽어 들이기
f = urllib.request.urlopen(request)
resultXML = f.read( )

#resultXML을 파싱하기
xmlsoup = BeautifulSoup(resultXML,'html.parser')
#item 항목을 찾아서, items에 저장
items = xmlsoup.find_all('item')

#items에 있는 내용을 파일에 저장
for item in items :
     file.write('-----------------------------------------\n')
     file.write('뉴스제목 : ' + item.title.get_text(strip=True) + '\n')
     file.write('요약내용 : ' + item.description.get_text(strip=True) + '\n')
     file.write('\n')
#파일 닫기
file.close( )