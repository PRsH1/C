"""
주제:인코딩 하지 않기
작성일:2017.11.29.
작성자:이승현
"""

import urllib.parse
def input_query():
    q=str(input("검색어를 입력하세요:"))
    return "&query="+q
print(input_query())
