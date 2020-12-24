import requests

baseURL = "https://api.stackexchange.com"
searchURL = "/2.2/search"

query = {"order": "desc", "sort": "activity", "tagged": "Python", "intitle": "TypeError", "site": "stackoverflow"}

getDataRequest = requests.get(f"{baseURL}{searchURL}", params=query)
JSONResponse = getDataRequest.json()

for item in JSONResponse["items"]:
    if item["is_answered"] == True:
        print(item["link"])


'''
if getDataRequest.status_code != 200:
    print(f" <ERROR 01> : {getDataRequest.status_code} received (Expected 200)")
'''


