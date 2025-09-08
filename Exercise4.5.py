# Correct username and password
user_correct = "python"
pass_correct = "rules"

attempts = 0

while attempts < 5:
    user = input("Username: ")
    pw = input("Password: ")

    if user == user_correct and pw == pass_correct:
        print("Welcome!")
        break
    else:
        attempts += 1
        print("Wrong credentials. Tries left:", 5 - attempts)
else:
    print("Access denied.")
