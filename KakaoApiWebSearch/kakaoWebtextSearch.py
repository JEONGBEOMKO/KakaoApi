# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 17:28:46 2021

@author: kjb98
"""

import requests
import json

url = "https://dapi.kakao.com/v2/search/web"

queryString = {'query' : '이효리'}
header = {'Authorization': 'KakaoAK MyRestApiKey'}

response = requests.get(url, headers=header, params=queryString)
tokens = response.json()

print(response)
print(tokens)



