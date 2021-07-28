# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 16:21:24 2021

@author: kjb98
"""

import os
os.getcwd()



import requests
import json

# 이미지가 있는 image_url을 통해 file_name 파일로 저장하는 함수
def save_image(image_url, file_name):
    img_response = requests.get(image_url)
    #요청에 성공했다면,
    if img_response.status_code == 200:
        #파일저장
        with open(file_name, "wb") as fp:
            fp.write(img_response.content)
            

# 이미지 검색 
url = "https://dapi.kakao.com/v2/search/image"
headers = {
    "Authorization" : "KakaoAK MyRestApiKey"
}
data = {
    "query" : "펭수"
}

# 이미지 검색 요청
response = requests.post(url, headers=headers, data=data)
# 요청에 실패했다면,
if response.status_code != 200:
    print("error! because ",  response.json())
else: # 성공했다면,
    count = 0
    for image_info in response.json()['documents']:
        print(f"[{count}th] image_url =", image_info['image_url'])
        # 저장될 이미지 파일명 설정
        count = count + 1
        file_name = "test_%d.jpg" %(count)
        #이미지 저장
        save_image(image_info['image_url'], file_name)
        