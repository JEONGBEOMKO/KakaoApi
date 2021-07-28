# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 13:51:39 2021

@author: kjb98
"""

import json
import requests
import datetime
import os

# 카카오 토큰을 저장할 파일명
KAKAO_TOKEN_FILENAME = "res/kakao_message/kakao_token.json"
KAKAO_APP_KEY = "MyRestApiKey"
# 저장하는 함수

url = "https://kauth.kakao.com/oauth/token"

data = {
    "grant_type" : "authorization_code",
    "client_id" : "MyRestApiKey",
    "redirect_uri" : "https://localhost.com",
    "code"         : "MyTokenCode"
    
}
response = requests.post(url, data=data)
 
tokens = response.json()
print(tokens)

def save_tokens(filename, tokens):
    with open(filename, "w") as fp:
        json.dump(tokens, fp)
        
        return tokens

# 토큰 저장
save_tokens(KAKAO_TOKEN_FILENAME, tokens)

# 토큰 업데이트 -> 토큰 저장 필수!
#KAKAO_APP_KEY = "MyRestApiKey"
#tokens = update_tokens(KAKAO_APP_KEY, KAKAO_TOKEN_FILENAME)
#save_tokens(KAKAO_TOKEN_FILENAME, tokens)
