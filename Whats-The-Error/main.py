from requests import get
from subprocess import Popen, PIPE
from webbrowser import open

print("______________________________________")
print(" Welcome to Whats-The-Error Client ...")
print("______________________________________")

print("Enter file name ..")
checkFileName = input().lower()

temp = checkFileName.split(".")
extensionName = temp[len(temp) - 1]

languages = ["py", "c", "cpp"]
languageCode = -1
errorFindMethodCode = -1
language = "Not Defined"

if extensionName not in languages:
    print("<ERROR : FormatError>> Our client never saw such file format. Make sure it has an extension !!")
    exit()

if extensionName == languages[0]:
    languageCode = 0
    language = "Python"
    errorFindMethodCode = 0

elif extensionName == languages[1]:
    languageCode = 1
    language = "C"
    errorFindMethodCode = 1

elif extensionName == languages[2]:
    languageCode = 2
    language = "C++"
    errorFindMethodCode = 1

print("______________________________________")

execCommand = ["python " + checkFileName,
               "gcc " + checkFileName + " -o" + checkFileName[:checkFileName.rfind(".")] + ".exe",
               "g++ " + checkFileName + " -o" + checkFileName[:checkFileName.rfind(".")] + ".exe"]

ProgramExecutionProcess = Popen(execCommand[languageCode].split(), stdout=PIPE, stderr=PIPE)

stdout, stderr = ProgramExecutionProcess.communicate()

errorText = stderr.decode("UTF-8")

if len(errorText) == 0:
    print("No Errors Found")
    exit(0)

if errorFindMethodCode == 0:
    errorClass = errorText[errorText[: errorText.rfind("Error")].rfind(" "): errorText.rfind("Error")].split()[1]
    errorClass = errorClass + str("Error")
    errorMessage = errorText[errorText.rfind(errorClass):]

    print("Error Type        : " + errorClass)
    print("Error Description : " + errorMessage)

elif errorFindMethodCode == 1:
    # Under development
    print(errorText)
    exit()

baseURL = "https://api.stackexchange.com"
searchURL = "/2.2/search"

query = {"order": "desc", "sort": "activity", "tagged": language, "intitle": errorClass, "site": "stackoverflow"}

print("Fetching data ..")

getDataRequest = get(f"{baseURL}{searchURL}", params=query)
JSONResponse = getDataRequest.json()

print("Opening web links ...")

count = 0
for item in JSONResponse["items"]:
    if item["is_answered"] and count < 5:
        open(item["link"])
        count = count + 1
