import requests
from requests.models import Response

#取得tokens
def get_access_token():
    #API網址    
    url = "https://account.kkbox.com/oauth2/token" 
    #標頭
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "account.kkbox.com"
    }   
    #參數
    data = {
        "grant_type": "client_credentials",
        "client_id": "86db6c39c8f04bcf81cf63fd44de1cc7",
        "client_secret": "f3a18d3f881feb0636c962f75cda6c66"
    }
    access_token = requests.post(url, headers=headers, data=data)
    #print(access_token.json())
    return access_token.json()["access_token"]

def get_charts():
    #取得存取憑證
    access_token = get_access_token()
    #榜單網址
    url = "https://api.kkbox.com/v1.1/charts"
    #標頭
    headers = {
        "accept": "application/json",
        "authorization": "Bearer " + access_token  #帶著存取憑證
    }
    #參數
    params = {
        "territory": "TW"  #台灣領域  
    }
    response = requests.get(url, headers=headers, params=params)
    result = response.json()["data"]
    #print(response.json())
    
    for item in result:
        print(item["id"], item["title"])

def get_chart_list():
    access_token = get_access_token()

    url = "https://api.kkbox.com/v1.1/charts/-mjlqxfwgu9_zm9YOr/tracks"
    headers = {
        "accept": "application/json",
        "authorization": "Bearer " + access_token
    }
    params = {
        "territory":"TW"
    }
    response =requests.get(url,headers=headers,params=params)
    print("****"+str(response.status_code))
    results = response.json()["data"]
    for play in results[0:10]:
        print(play["name"])

get_chart_list()