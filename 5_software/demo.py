database = open("first-names.txt")
all_names = database.read().split('\n')

def checkIfName(username):
    for name in all_names:
        if username == name:
            print("Welcome, " + username + "!")
            return
    print("Error occured!")

username = input("what is your first name? ")

checkIfName(username)

database.close()
