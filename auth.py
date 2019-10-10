import bcrypt 
from getpass import getpass

all_users = []

def create_user():
    username = input('Username: ')
    pass1 = getpass()
    pass2 = getpass()

    found = False

    for i in all_users:
        if i['username'] == username:
            found = True
            break
    
    if found:
        print('User already exits. ')
    else:
        if pass1 == pass2:
            password = pass1.encode('utf-8')
            hpass = bcrypt.hashpw(password, bcrypt.gensalt())

            all_users.append({'username':username, 'password':hpass})
        else: 
            print('Passwords did not match. ')
    
    print(all_users)

def authenticate():
    username = input('Username: ')
    password = getpass()

    found = False

    for c,i in enumerate(all_users):
        if i['username'] == username:
            found = True
            location = c 
            break
        
    if found: 
        npass = password.encode('utf-8')
        if bcrypt.checkpw(npass, all_users[location]['password']):
            print('You have logged on.')
        else:
            print('Passwords don\'t match.')
    else:
        print('User not found.')
