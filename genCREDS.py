import random
import json


try:
	numberOfMails = int(input("Number of emails to generate: "))

	letterName = ((input("------------\nUse only a letter for names? ex: \n'A.smith' instead of 'Anna.smith'\nY or N: ")).upper() == "Y")

	mails = ["fakemail", "nonexist", "purefake"]

	gencreds = []

	try:
		with open("names.txt","r") as nameFile:
			with open("surnames.txt", "r") as surnFile:
				with open("fakePasswords.txt", "r") as passFile:
				
					allNames = nameFile.readlines()
					allSurnames = surnFile.readlines()
					allPasswords = passFile.readlines()

					for i in range(numberOfMails):
						name = random.choice(allNames).rstrip('\n')
						surname = random.choice(allSurnames).rstrip('\n')
						fullMail = "{0}.{1}@{2}.com".format(name[0].lower(),surname,random.choice(mails))
						password = random.choice(allPasswords).rstrip('\n')
						gencreds.append({"name": name, "surname": surname, "email": fullMail, "password": password})
						print(name + ":" + surname + ":" + fullMail + ":" + password)

				passFile.close()
			surnFile.close()
		nameFile.close()

		print("------------\nFinished")
		
	except FileNotFoundError:
		print("File not found")
except ValueError:
	print("Only numbers are allowed")


# Export creds as Json
with open("generatedCREDS.json", "w") as result:
	json.dump(gencreds, result, indent = 6)