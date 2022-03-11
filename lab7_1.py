"""
주제:라이브러리
작성자:이승현
작성일:2017.11.27.
"""

import urllib.request

req=urllib.request
d=req.urlopen("http://sw.skhu.ac.kr/")
s=d.read()
print(s)