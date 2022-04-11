#name generator
import random
import sys

if __name__ == "__main__":
    try:
        numberGenerate = int(sys.argv[1])
    except IndexError:
        numberGenerate = 1
        print("Number not speficied, only 1 will be generated")
else: numberGenerate = 1

print("-----Generated Names-----")


try:
    with open("names.txt","r") as nameFile:
        with open("surnames.txt", "r") as surnFile:

            names = nameFile.readlines()
            surnames = surnFile.readlines()        
            for x in range(numberGenerate):

                name = random.choice(names)
                surname = random.choice(surnames)
                line = (name.rstrip('\n') + " " + surname.rstrip('\n'))
                print(line)

        surnFile.close()
    nameFile.close()

    print("-----Finished------")

except FileNotFoundError:
    print("File not found")


