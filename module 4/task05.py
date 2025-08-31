correct_username = "python"
correct_password = "rules"

Attempts = 0
while Attempts < 5:
    username = input("Username: ")
    password = input("Password: ")

    if username == correct_username and password == correct_password:
        print("Welcome")
        break
    else:
        print("username or password is incorrect, try again.")
        Attempts += 1

if Attempts == 5:
    print("Access denied")
