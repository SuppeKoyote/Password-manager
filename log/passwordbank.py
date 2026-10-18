import json
from pathlib import Path


passwords = [{}]


parent = Path(__file__).parent
jsonFile = parent / "passwords.json"


with open(jsonFile, "r") as file:
	passwords = json.load(file)



def getPasswords() -> list:
	return passwords


def savePassword(passwordData : list):
	passwords = passwordData
	saveJson()

def deletePassword(index: int):
	del passwords[index]
	saveJson()


def saveJson():
	with open(jsonFile, "w") as file:
		json.dump(passwords, file)