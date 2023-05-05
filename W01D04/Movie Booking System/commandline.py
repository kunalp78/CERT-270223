import operations as op
import random
import string

while True:
    print("Main menu: ")
    print("1) User Login")
    print("2) Admin Login")
    print("3) Register")
    print("4) Exit")
    val = input("Enter your choice between numbers 1-4: ")
    if val == "4":
        print("See you next time!!")
        break
    elif val == "1":
        email=input("Enter your Email address: ")
        paswd=input("Enter your password: ")
        loginstatus = True # login(user_json, email, password)
        if loginstatus == False:
            print("Invalid Credentials!!")
        else:
            print("Logged in as User!!")
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
                tkt_id = input("Enter the ticket ID: ")
                no_of_booking=input("Enter the number of tickets you want to book: ")
                preferred_seats=input("Enter the seats followed by spaces: ").split()
                op.book_ticket("movie.json", "user.json", email, tkt_id, no_of_booking, *preferred_seats)
                print("Ticket Booked!!")
            elif val=="2":
                # all the movies
                print("Movies listed")
                print("Movie ID| Movie Name| Total Seating| Total seating available| Price| Duration")
                op.show_all_the_movies("movie.json")
            else:
                print("Enter the correct input!!")
    elif val=="2":
        print("Logged in as Admin!! ")
        while 1:
            print("Menu:")
            print("1) Add the Movie")
            print("2) Exit")
            i = input("Enter your choice: ")
            if i == "1":
                movie_name=input("Enter the Movie name: ")
                movie_duration=input("Enter the movie duration: ")
                price=input("Enter the movie Price: ")
                movie_id="".join(random.choices(string.ascii_uppercase+string.digits, k=5))
                op.add_movie("movie.json", movie_id, movie_name, movie_duration, price)
            elif i=="2":
                print("Thanks for your contribution!!")
                break
            else:
                print("Pls enter correct response between [1-2]")
        # add a movie
    elif val=="3":
        #Registeration process
        name=input("Enter the name.")
        paswd=input("Enter the password.")
        email=input("Enter your email!! ")
        phn=input("Enter the phone number!!")
        user_id="".join(random.choices(string.ascii_uppercase+string.digits, k=4))
        op.register("user.json", user_id, name, paswd, email, phn)
        print("Registration completed!!")
    else:
        print("Enter the correct choice between [1-4]")
        