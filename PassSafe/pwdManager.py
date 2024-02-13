import time
import csv

def encrypt():
    pass

def decrypt():
    pass

def add_user():
    UserName = input("What would you like the user to be called? ")
    mast_pwd = input('Enter your Master Password(Do not reveal this to anyone): ')
    time.sleep(0.5)
    details =[[UserName,mast_pwd]]
    with open('Safe.csv','a+',newline='') as f:
        swriter = csv.writer(f)
        swriter.writerow(details)
    # print("Great! Kindly restart the program to view or add passwords by choosing the 'return[r]' option. ")
    # quit()
    

def view_all():
    with open('Safe.csv','r') as f:
        contents = csv.reader(f)
        for row in contents:
            if row[0] == Safe_user:
                print(row)


def view_specific():
    Account = input("Enter the name of the account you want to view: ")
    with open('Safe.csv','r') as f:
        content = csv.reader(f)
        for row in content:
            if row [0] == Safe_user:
                for element in row:
                    if element[0] == Account:
                        print(element[1])


def add():
    with open('Safe.csv', 'a+') as file:
        reader = csv.reader(file)
        for row in reader:
            if row == 'User':
                row.append('Account')
        for row in reader:
            if row[0] == Safe_user:
                mst_pwd =input("Enter you're master password: ")
                if row[1] == mst_pwd:
                    new_acc = input("Enter the new account's Username: ")
                    new_pwd = input("Enter the new account's Password: ")
                    details = ([new_acc,new_pwd])
                    row.append(details)
                else:
                    i = 0
                    while True:
                        i += 1
                        print('You have entered the wrong master password, you have one more attempt.')
                        mst_pwd = mst_pwd =input("Enter you're master password: ")
                        if i == 2:
                            print("You have enetered the master password incorrect too many times. The program is now shutting down.")
                            for i in range(3,0,-1):
                                print(i)
                                time.sleep(0.5)
                            print('...')
                            quit()

                        
#__main__

    
print("Welcome to PassSafe, your personal password manager.")

while True:
    registered_user = input('Are you a returning user or here to make a new safe. (return[r],new[n])').lower()
    if registered_user == 'n' or registered_user == 'new':
        add_user()
    elif registered_user == 'return' or registered_user == 'r':
        Safe_user = input('Enter Pass Safe User Name:')
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
            view_all()


