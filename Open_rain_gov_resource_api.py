import requests
from requests.models import Response

def get_open_rain(no):
    url =" 	https://tinyurl.com/j9t6jxds?stationNo="+no
    headers = {
        "loginId" : "open_rain",
        "daraKey" : "85452CID"
    }
    response = requests.get(url,headers=headers)
    results = response.json()['data'] 
    for i in range(len(results)):
        if results[i]["stationNo"] == no:
            print(str(results[i]["stationName"])+":"+str(results[i]["rain"])) 
try:
    no = input()
    get_open_rain(no)
except KeyError:
    print("error")