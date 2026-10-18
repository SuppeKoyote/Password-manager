import passwordbank
import secrets

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
charCount = 94


PasswordDatabank = passwordbank.getPasswords()

def mainMenu():
	print("Password Manager")
	print("-----------------\n")

	print("1. show list of passwords")
	print("2. Generate random password")
	print("3. Add password to list")
	print("4. Quit")

	while True:
		try:
			option = int(input("Enter option: "))

			if option not in (1,2,3,4):
				print("Error! Enter the numbers of these options")
			else:
				sceneChanger(option)
				break
		except ValueError:
			option = None
			print("Error! Enter a number")



def sceneChanger(scene : int):
	match scene:
		case 1: showlist()
		case 2: randomPassGen()
		case 3: addPassword()

def showlist():
	PasswordDatabank = passwordbank.getPasswords()

	index: int= 1
	for passwordData in PasswordDatabank:
		print(str(index) + ". " + passwordData["name"] + ": " + passwordData["password"])
		index += 1

	print("\nEnter 1 to delete a password or 2 to edit a password")
	print("Enter anything else to go to main Menu")

	choice = str(input("Enter choice: "))

	if (choice == "1"):
		deletPassword()
	elif (choice == "2"):
		editPassword()
	else:
		mainMenu()

def randomPassGen():

	password = ""

	while True:
		try:
			passwordLength = int(input("Enter length of password: "))
			if (passwordLength <= 0):
				print("Enter a number over 0")
			else:
				break

		except ValueError:
			print("Error! Enter number")


	for i in range(passwordLength):
		randomInt = secrets.randbelow(charCount)
		char = chars[randomInt]	
	
		password += char

	print(password)
	
def addPassword():

	newPasswordData = makePasswordData()
	PasswordDatabank.append = newPasswordData
	passwordbank.savePassword(PasswordDatabank)
	mainMenu()


def getPassDataFromList() -> int:
	while True:
		try:
			passIndex: int = int(input())

			if passIndex < 1 or passIndex > len(PasswordDatabank):
				print("Number is not in range")

			else:
				return passIndex

		except ValueError:
			print("Error! Enter a number")
			passIndex : int = -1

def deletPassword():
	print("Enter the password number you want to delete: ", end="")

	passIndex = getPassDataFromList()		


	print("Are you sure to delete " + PasswordDatabank[passIndex-1]["name"] + "?")
	confirmation = str(input("Enter y to confirm: "))
	if(confirmation == "y"):
		passwordbank.deletePassword(passIndex-1)
		print("Succesfully deleted")
		mainMenu()
	else:
		mainMenu()	

def editPassword():
	print("Enter the password number you want to edit: ", end="")

	passIndex = getPassDataFromList()

	newPasswordData = makePasswordData()

	print("Are you sure to change: " + PasswordDatabank[passIndex-1]["name"] +" " + PasswordDatabank[passIndex-1]["password"], end="" )
	print(" to: " + newPasswordData["name"] +" " + newPasswordData["password"])
	confirmation = str(input("Enter y to comfirm"))

	if confirmation == "y":
		PasswordDatabank[passIndex-1]["name"] = newPasswordData["name"]
		PasswordDatabank[passIndex-1]["password"] = newPasswordData["password"]
		passwordbank.savePassword(PasswordDatabank)



def makePasswordData() -> dict:
	passwordname = ""

	while passwordname == "":
		passwordname = input("Enter new Platform name: ").strip()

	newpassword = str(input("Enter new Password: "))

	newPasswordData = {"name" : passwordname, "password" : newpassword}
	return newPasswordData

mainMenu()