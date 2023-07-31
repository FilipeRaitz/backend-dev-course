#exercise on creating a basic login system
print("Sign Up:")
username = input("Enter username: ")
while True:
    password = input("Enter password: ")
    if len(password) < 8:
        print("Your password must be at least 8 characters long.")
    else:
        print("Your account was created successfully")
        break
print("\n\n")
print("Log In:")
while True:
    username2 = input("Enter your username: ")
    password2 = input("Enter your password: ")
    if username2 != username or password2 != password:
        print("Wrong credentials. Try again!")
    else:
        print("Login successful!")
        break
        
