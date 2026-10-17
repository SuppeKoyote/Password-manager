import json


passwords = [{}]

with open("passwords.json", "r") as file:
	passwords = json.load(file)



def getPasswords() -> list:
	return passwords


def addPassword(passwordData : dict):
	passwords.append(passwordData)
	saveJson()

def deletePassword(index: int):
	del passwords[index]
	saveJson()


def saveJson():
	with open("passwords.json", "w") as file:
		json.dump(passwords, file)