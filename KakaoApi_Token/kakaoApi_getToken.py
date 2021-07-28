# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 15:28:46 2021

@author: kjb98
"""

import requests
import json

url = "https://kauth.kakao.com/oauth/token"
# 카카오 토큰을 저장할 파일명
KAKAO_TOKEN_FILENAME = "res/kakao_message/kakao_token.json"

data = {
    "grant_type" : "authorization_code",
    "client_id" : "MyRestApiKey",
    "redirect_uri" : "https://localhost.com",
    "code"         : "MyTokenKey"
    
}
response = requests.post(url, data=data)
 
tokens = response.json()
print(tokens)
"""
def save_tokens(filename, tokens): 
    with open(filename, "w") as fp:
        tokens = json.dump( tokens, fp)
        
    return tokens

save_tokens("kakao.json", {"error": "invalid_grant", "error_description": "authorization code not found for code=hrrGzQvLUj9Cgno9N75g3hCZpUNHhtaRA9sCV4sJA65WMnNCpPAQEWtlJLfnJ9Y-rGUo1worDNMAAAF65q2OOA", "error_code": "KOE320")

"""