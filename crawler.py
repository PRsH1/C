import urllib.request#urllib.request라이브러리 import
from bs4 import BeautifulSoup

target_url = 'http://52.68.130.249:8040/textboard/'#목표 url

# 게시글의 제목과 목록을 가져오는 함수
def fetch_post_list():
    URL = target_url#주소를 URL에 저장
    res = urllib.request.urlopen(URL)
    html = res.read()

    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table', class_='kingkongboard-table')

    title_list = table.find_all('td', class_='kingkongboard-list-title')

    links = []#링크를 저장할 리스트 변수 links정의

    links = [td.find('a').get_text() for td in title_list]#title_list를 반복문을 돌려"a"를 찾아서 하이퍼링크 씌운다음 링크에 append를 함
    #이 코드는
    """
    for td in title_list:
        links.append(td.find('a').get_text()['href'])
        body_tag.append(bs.find('body'))
"""

    return links#링크를 반환한다

result = fetch_post_list( )#함수 fetch_post_list()호출
print(result)#결과문 출력

