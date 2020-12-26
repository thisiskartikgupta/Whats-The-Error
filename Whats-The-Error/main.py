
from requests import get
from subprocess import Popen, PIPE


'''
-1. Take input of file and assess its extension and respond appropriately.
2. Run the subprocess and fetch the error message.
3. Take the error fetched and pass it on to the StackExchange API.
4. Retrieve result and show them appropriately.
5. Develop GUI package in Tkinter.
6. Develop similar support for Java, Kotlin, JS, TS, C, CPP, Go, Rust, Scala, PHP, Julia, Bash etc.
7. Create Docker Container / pip package. 
. AutoCheck file system for files.
'''

print("______________________________________")
print(" Welcome to Whats-The-Error Client ...")
print("______________________________________")

checkFileName = input().lower()

temp = checkFileName.split(".")
extensionName = temp[len(temp) - 1]

languages = ["py"]

if extensionName in languages:
    print("We support this file format !!")

else:
    print("<ERROR : FormatError>> Our client never saw such file format. Make sure it has an extension")

print("______________________________________")

ProgramExecutionProcess = Popen(["python","checkFileName"], stdout=PIPE, stderr=PIPE)
stdout, stderr = ProgramExecutionProcess.communicate()


# baseURL = "https://api.stackexchange.com"
# searchURL = "/2.2/search"
#
# query = {"order": "desc", "sort": "activity", "tagged": "Python", "intitle": "TypeError", "site": "stackoverflow"}
#
# getDataRequest = requests.get(f"{baseURL}{searchURL}", params=query)
# JSONResponse = getDataRequest.json()
#
# for item in JSONResponse["items"]:
#     if item["is_answered"] == True:
#         print(item["link"])
#

'''
if getDataRequest.status_code != 200:
    print(f" <ERROR 01> : {getDataRequest.status_code} received (Expected 200)")
'''


