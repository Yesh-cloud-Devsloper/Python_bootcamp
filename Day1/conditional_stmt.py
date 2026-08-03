# 1.login system 
# ---------------
# correct username- admin
# correct password - pass123
# conditions:
#        ->if username is correct 
#           check password
#           if correct -- login successful
#           else-->worng password 
#           -->else Invalid password

username = input("enter your username: ")
password = input("enter your password: ")
if username == "admin":
    if password == "pass123":
        print("login successful")
    else:
        print("wrong password")
else:
    print("Invalid username")


