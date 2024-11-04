# 배민에서 음식을 고를려고 하는데 선택하기 힘들어서 메뉴를 추천하는 기능
# 예상 메뉴 > 치킨, 피자, 분식, 중식, 양식, 한식 등
# 무작위( 랜덤 )

import random
print(random.random())

menu = '치킨','피자','분식','중식'
print(random.choice(menu))

import requests
from bs4 import BeautifulSoup

# 웹에 접속
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"}
r = requests.get("https://www.melon.com/",headers=header)
print(r) #접속이 잘 됐는지 확인

# html 정보 가지고 오기
soup = BeautifulSoup(r.text, 'html.parser')
# print(soup) #가져온 html 데이터 출력

# #conts > div.chart > div > ul > li.on.nth1 > div > ul > li:nth-child(1) > div.rank_cntt > div.rank_info > p > a
title = soup.select_one('#conts > div.chart > div > ul > li.on.nth1 > div > ul > li:nth-child(1) > div.rank_cntt > div.rank_info > p > a')
print(title.text)