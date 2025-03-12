print("""
*********************************************
USER LOGIN
*********************************************
""")

user_name = "Diyar Aydın"
user_password = "welcome to mardin"

right_to_try = 3
i = 0

while i < right_to_try:
    userName = input("User Name: ")
    userPassword = input("User Password: ")

    if(user_name == userName):
        if(user_password == userPassword):
            print("Logged in")
            break
        else:
            print("Username is correct, password is incorrect")
            i += 1
            if (i == 2):
                print("Your last right ")

    else:
        print("Username is incorrect")
        i += 1
        if (i == 2):
            print("Your last right ")
