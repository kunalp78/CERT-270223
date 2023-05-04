import operations as op
import random
import string

while True:
    print("Main menu: ")
    print("1) Login")
    print("2) Register")
    print("3) Exit")
    val = input("Enter your choice between numbers 1-3: ")
    if val == "3":
        print("See you next time!!")
        break
    elif val == "1":
        email=input("Enter your Email address: ")
        paswd=input("Enter your password: ")
        loginstatus = True # login(user_json, email, password)
        if loginstatus == False:
            print("Invalid Credentials!!")
        else:
            print("Logged in!!")
        while loginstatus:
            print("User Menu")
            print("1) Book Ticket")
            print("2) Show all the movies")
            print("3) Log out")
            val=input("Enter the choices between 1-3")
            if val=="3":
                print("Logging out!!")
                break
            elif val=="1":
                # book ticket
                print("Ticket Booked!!")
            elif val=="2":
                # all the movies
                print("Movies listed")
            else:
                print("Enter the correct input!!")
    elif val=="2":
        #Registeration process
        name=input("Enter the name.")
        paswd=input("Enter the password.")
        email=input("Enter your email!! ")
        phn=input("Enter the phone number!!")
        user_id="".join(random.choices(string.ascii_uppercase+string.digits, k=4))
        op.register("user.json", user_id, name, paswd, email, phn)
        print("Registration completed!!")
    else:
        print("Enter the correct choice between [1-3]")
        