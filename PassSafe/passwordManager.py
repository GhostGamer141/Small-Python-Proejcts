import time

def encrypt():
    pass

def decrypt():
    pass

def add_user():
    UserName = input("What would you like the user to be called? ")
    mast_pwd = input('Enter your Master Password(Do not reveal this to anyone): ')
    time.sleep(0.5)
    Pwords['username'] = {}
    Pwords['username'][UserName] = {}
    Pwords['username'][UserName]['master password']= mast_pwd
    print(f"Perfect a user with the name {UserName} has been created.")
    print("Kindly restart the program to start saving passwords.")
    quit()

def view_all():
    with open("D:\\VS CODE\\Exercises\\Safe.txt",'r') as file:
        contents = file.readline()
        if master_pwd == Pwords[UserName]['master password']:
            print(Pwords[UserName])  

def view_specific():
    with open("D:\\VS CODE\\Exercises\\Safe.txt",'r') as file:
        return Pwords[UserName] 

def add():
    pass





#__main__
Pwords = {}
Pwords['user']
print("Welcome to PassSafe, your personal password manager.")
with open('D:\\VS CODE\\Exercises\\Safe.txt', 'a+') as file:
    file.writelines(Pwords)

while True:
    registered_user = input('Are you a returning user or here to make a new safe. (return[r],new[n])').lower()
    if registered_user == 'n' or registered_user == 'new':
        add_user()
    elif registered_user == 'return' or registered_user == 'r':
        break
    else:
        print("Enter a valid option.")
        continue

if registered_user == 'return' or registered_user == 'r':
    while True:
        choice = input("Would you like to add a new password, or would you like to view a current password.['add','view']").lower()
        if choice not in ['add','view']:
            print('Enter a valid option.')
        else:
            break
        if choice == 'add':
            add()
        elif choice == 'view':
            while True:
                Vmode = input("Would you like to view a specific account or view all passwords, ['specific','all']").lower()
                if Vmode not in ['specific', 'all']:
                    print('Enter a valid option.')
                else:
                    break
                if Vmode == 'specific':
                    view_specific()
                else:
                    view_all



master_pwd = input("Whats the master password? ")
UserName = input("Enter the user name to the account")
mode = input("Would you like to view your all your passwords or add a new one:")


