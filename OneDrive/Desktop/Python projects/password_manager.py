from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
write_key()'''

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


master_pwd = input("What is the master password? ")
key = load_key() + master_pwd.encode()
fer = Fernet(key)

#defining our functions
def view():
    with open("passwords.txt", "r") as f:
       for line in f.readlines():
        data = line.rstrip()
        user, passw = data.split("|")
        print("User:", user, ",| Password:", fer.decrypt(passw.encode()).decode())

def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    with open("passwords.txt", "a") as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

        
#while loop, if statements
while True:
    mode = input("Would you like to add a new password or view existing ones (view/add), press q to quit? ")
    if mode == "q":
        break
#calling the view function here
    if mode == "view":
        view()
#calling the add() function here
    elif mode == "add":
        add()
        print("Done!")

    else:
        print("Invalid mode.")
        continue



