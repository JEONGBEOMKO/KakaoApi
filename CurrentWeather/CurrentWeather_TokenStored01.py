# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 13:51:39 2021

@author: kjb98
"""

import requests

import json


apikey = " af88e26010932bab33aa15ec76b9bf2e"
city_list = ["Seoul, KR", "NewYork, US", "London, GB"]

api="http://api.openweathermap.org/data/2.5/weather?q=Seoul,NewYork,London &appid=WeatherAk"

#켈빈 온도를 섭씨 온도로 변환하는 함수
k2c = lambda k: k -273.15

#각 도시의 정보 추출
for name in city_list:

    #API URL 구성하기
    url = api.format(city=name, key=apikey)

    #API 요청을 보내 날씨 정보를 가져오기
    res = requests.get(url)

    #JSON형식의 데이터를 파이썬으로 변환
    data = json.loads(res.text)

    print("도시 = ", data["name"])
    print("날씨 = ", data["weather"][0]["description"])
    print("최저 기온", k2c(data["main"]["temp_min"]))
    print("최고 기온 = ", k2c(data["main"]["temp_max"]))