from requests import get
from subprocess import Popen, PIPE
from webbrowser import open

print("______________________________________")
print(" Welcome to Whats-The-Error Client ...")
print("______________________________________")

checkFileName = input().lower()

temp = checkFileName.split(".")
extensionName = temp[len(temp) - 1]

languages = ["py"]
language = "Not Defined"

if extensionName not in languages:
    print("<ERROR : FormatError>> Our client never saw such file format. Make sure it has an extension !!")
    exit()

if extensionName == languages[0]:
    language = "Python"

print("______________________________________")

ProgramExecutionProcess = Popen(["python", checkFileName], stdout=PIPE, stderr=PIPE)

stdout, stderr = ProgramExecutionProcess.communicate()

errorText = stderr.decode("UTF-8")

errorClass = errorText[errorText[: errorText.rfind("Error")].rfind(" "): errorText.rfind("Error")].split()[1]
errorClass = errorClass + str("Error")

errorMessage = errorText[errorText.rfind(errorClass):]

print("Error Type        : " + errorClass)
print("Error Description : " + errorMessage)

baseURL = "https://api.stackexchange.com"
searchURL = "/2.2/search"

query = {"order": "desc", "sort": "activity", "tagged": language, "intitle": errorClass, "site": "stackoverflow"}

getDataRequest = get(f"{baseURL}{searchURL}", params=query)
JSONResponse = getDataRequest.json()

count = 0
for item in JSONResponse["items"]:
    if item["is_answered"] and count < 5:
        open(item["link"])
        count = count + 1
