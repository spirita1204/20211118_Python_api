from datetime import datetime
import json
import urllib.parse
import hashlib #sha256 e

HashKey='5294y06JbISpM5x9'
HashIV='v77hoKGq4kWxNNIS'
send_message = {
    'MerchantTradeNo': '2021/11/18 17:14:06',
    'MerchantTradeDate': '2021/11/18 17:14:06',
    'PaymentType': 'aio',
    'TotalAmount': '3000',
    'TradeDesc': '訂單測試',
    'ItemName': '42',
    'ReturnURL': 'https://ef2f-2001-b011-4009-19f9-ac9b-4d89-5176-89d3.ngrok.io/payment/end_return/',#'https://www.ecpay.com.tw/return_url.php' 顧客填完付款資料後的跳轉頁面
    'ChoosePayment': 'ALL',
    'ClientBackURL': 'https://ef2f-2001-b011-4009-19f9-ac9b-4d89-5176-89d3.ngrok.io/payment/end_page/',
    'ItemURL': 'https://www.ecpay.com.tw/item_url.php',
    'Remark': '交易備註',
    'OrderResultURL': 'https://ef2f-2001-b011-4009-19f9-ac9b-4d89-5176-89d3.ngrok.io/payment/end_page/',
    'PaymentInfoURL': 'https://www.ecpay.com.tw/payment_info_url.php',
    'NeedExtraPaidInfo': 'Y',
    'InvoiceMark': 'N',
    'EncryptType': 1,
    'ExpireDate': 7,
    'StoreExpireDate': 15,
    'BindingCard': 0,
    'Redeem': 'N',
    'UnionPay': 0,
}
send_message7 = {
    'MerchantTradeNo': '2021/11/18 17:14:06',
    'StoreID': '',
    'MerchantTradeDate': '2021/11/18 17:14:06',
    'PaymentType': 'aio',
    'TotalAmount': '3000',                                               #商品金額
    'TradeDesc': '訂單測試',                                            #商品描敘       
    'ItemName': '42',
    'ReturnURL': 'https://ef2f-2001-b011-4009-19f9-ac9b-4d89-5176-89d3.ngrok.io/payment/end_return/',#'https://www.ecpay.com.tw/return_url.php' 顧客填完付款資料後的跳轉頁面
    'ChoosePayment': 'ALL',
    'ClientBackURL': 'https://ef2f-2001-b011-4009-19f9-ac9b-4d89-5176-89d3.ngrok.io/payment/end_page/',
    'ItemURL': 'https://www.ecpay.com.tw/item_url.php',
    'Remark': '交易備註',
    'ChooseSubPayment': '',
    'OrderResultURL': 'https://ef2f-2001-b011-4009-19f9-ac9b-4d89-5176-89d3.ngrok.io/payment/end_page/',
    'NeedExtraPaidInfo': 'Y',
    'DeviceSource': '',
    'IgnorePayment': '',
    'PlatformID': '',
    'InvoiceMark': 'N',
    'CustomField1': '',
    'CustomField2': '',
    'CustomField3': '',
    'CustomField4': '',
    'EncryptType': 1,
    'ExpireDate': 7,
    'PaymentInfoURL': 'https://www.ecpay.com.tw/payment_info_url.php',
    'ClientRedirectURL': '',
    'StoreExpireDate': 15,
    'Desc_1': '',
    'Desc_2': '',
    'Desc_3': '',
    'Desc_4': '',
    'ClientRedirectURL': '',
    'BindingCard': 0,
    'MerchantMemberID': '',
    'Redeem': 'N',
    'UnionPay': 0,
    'Language':'ENG',
    }
send_message1= {
    'TradeDesc':'促銷方案',
    'PaymentType':'aio',
    'MerchantTradeDate': '2013/03/12 15:30:23',
    'MerchantTradeNo':'ecpay20130312153023',
    'MerchantID':'2000132',
    'ReturnURL':'https://www.ecpay.com.tw/receive.php',
    'ItemName':'Apple iphone 7 手機殼',
    'TotalAmount':'1000',
    'ChoosePayment':'ALL',
    'EncryptType':1,
    'daads':'',
}
#print(type(send_message["Redeem"]))
# 透過 Dictionary comprehension 一行就可以濾掉
def removekey(d, key):
    r = dict(d)
    del r[key]
    return r
for key in send_message:
    if send_message[key] == '':
        send_message = removekey(send_message,key)
print (send_message)
for key,val in send_message.items():
    if type(send_message[key]) == int :
        send_message[key] = str(send_message[key])
    send_message[key] = send_message[key].replace(" ","+")

#print(send_message)

send_message_filter = {
    k: send_message[k] for k in send_message if type(send_message[k]) != dict
}

#print(send_message_filter)
#print("#########")

# 將 key 進行排序，將此順序存到另外一個 list 中
sorted_key =  sorted ( send_message_filter.keys() )

# 一樣透過 Dictionary comprehension 得到一個排序好的新 dict
send_message_orderby_key = {k: send_message_filter[k] for k in sorted_key}
print(send_message_orderby_key)
# 將 dict 轉成 json (字串)
app_json = json.dumps(send_message_orderby_key,ensure_ascii=False)
print("#######JSON######")
# 印出來看看
print(app_json)
# {"Amount": 50000, "BackendURL": "http://10.11.22.113:8803/QPay.ApiClient/AutoPush/PushSuccess", "CurrencyID": "TWD", "OrderNo": "A201804270001", "PayType": "A", "PrdtName": "ThisDummyOrderNo", "ReturnURL": "http://10.11.22.113:8803/QPay.ApiClient/Store/Return", "ShopNo": "BA0026_001"}

# 透過內建的文字取代函數，就可以拿到最終的成果囉! 
app_json = app_json.replace(": ", "=").replace(",","&").replace('"', "").replace("{", "" ).replace(" ","").replace("}", "")
print("#####JSON_REPLACE#######")
print(app_json) 

print("######Hash_json######")
hash_app_json = "HashKey=5294y06JbISpM5x9&"+app_json+"&HashIV=v77hoKGq4kWxNNIS"
print(hash_app_json)
print("######Url_encode######")
url_encode = urllib.parse.quote(hash_app_json.encode('utf8'))
url_encode = url_encode.lower()
url_encode = url_encode.replace("%2b","+")
url_encode = url_encode.replace(":","%3a")
url_encode = url_encode.replace("/","%2f")
print(url_encode)
print("################")
sha256 = hashlib.sha256(url_encode.encode('utf-8')).hexdigest()
sha256 = sha256.upper()
print(sha256)
print("#####finish######")
#print(url_encode ==
#"hashkey%3d5294y06jbispm5x9%26choosepayment%3dall%26encrypttype%3d1%26itemname%3dapple+iphone+7+%e6%89%8b%e6%a9%9f%e6%ae%bc%26merchantid%3d2000132%26merchanttradedate%3d2013%2f03%2f12+15%3a30%3a23%26merchanttradeno%3decpay20130312153023%26paymenttype%3daio%26returnurl%3dhttps%3a%2f%2fwww.ecpay.com.tw%2freceive.php%26totalamount%3d1000%26tradedesc%3d%e4%bf%83%e9%8a%b7%e6%96%b9%e6%a1%88%26hashiv%3dv77hokgq4kwxnnis")
#"hashkey%3d5294y06jbispm5x9%26choosepayment%3dall%26encrypttype%3d1%26itemname%3dapple+iphone+7+%e6%89%8b%e6%a9%9f%e6%ae%bc%26merchantid%3d2000132%26merchanttradedate%3d2013%2f03%2f12+15%3a30%3a23%26merchanttradeno%3decpay20130312153023%26paymenttype%3daio%26returnurl%3dhttps%3a%2f%2fwww.ecpay.com.tw%2freceive.php%26totalamount%3d1000%26tradedesc%3d%e4%bf%83%e9%8a%b7%e6%96%b9%e6%a1%88%26hashiv%3dv77hokgq4kwxnnis"
#CFA9BDE377361FBDD8F160274930E815D1A8A2E3E80CE7D404C45FC9A0A1E407
#CFA9BDE377361FBDD8F160274930E815D1A8A2E3E80CE7D404C45FC9A0A1E407
