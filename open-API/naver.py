import urllib.request

client_id = "FcQj8Lu4lqN6P6O8cKUw"
client_secret = "6b0HRiTIHX"
url = "https://openapi.naver.com/v1/datalab/search"
body = '''{
    "startDate": "2021-02-22",
    "endDate": "2022-02-22",
    "timeUnit": "date",
    "keywordGroups": [
        {
            "groupName": "NFT",
            "keywords": [
                "nft"
            ]
        }
    ]
}'''

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
request.add_header("Content-Type","application/json")
response = urllib.request.urlopen(request, data=body.encode("utf-8"))
rescode = response.getcode()

if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)