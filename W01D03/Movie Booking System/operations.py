import json
from json import JSONDecodeError

def register(user_json, user_id, name, password, email, phone):
    """
    register function returns True if the registration was successful
                      returns False if the registration was unsucessful

    Args:
        user_json (string): the json file passed to the register function
        user_id (string): a random id generated for each user
        name (string): the identity of individual
        password (string): password
        email (string): it should be unique for each user
        phone (string)
    """
    d = {
        "user_id": user_id,
        "name": name,
        "password": password,
        "email": email,
        "phone": phone,
        "booked history": []
    }
    f=open(user_json, "r+")
    try:
        content=json.load(f) 
        if d not in content:
            content.append(d)
            f.seek(0)
            f.truncate()
            json.dump(content, f)
            f.close()
            return True
    except JSONDecodeError:
        l=[]
        l.append(d)
        json.dump(l, f)
        f.close()
        return True
    f.close()
    print("Registration completed")
    return False

def login(user_json, email, password):
    """
    Returns True if login is successful
    Returns False if login is unsuccessful

    Args:
        user_json (str): the json file passed to the register function
        email (str): email of the user
        password (str): password of the user
    """
    f=open(user_json, "r+")
    try:
        content=json.load(f)
    except JSONDecodeError:
        f.close()
        return False
    f.close()
    d=0
    for i in range(len(content)):
        if content[i]["email"]==email and content[i]["password"]==password:
            d=1
            break
    if d==1:
        return True
    return False

def add_movie(movie_json, movie_id, movie_name, duration, price):
    """
    Return True if the movie was added
    Return False if Movie was not added

    Args:
        movie_json (str): the json file passed to the add movie function
        movie_id (str): id of each movie
        movie_name (str): the name of the movie
        duration (str): total duration of the movie
        price (int): price of the movie
    """
    d = {
        "Movie ID": movie_id,
        "Movie Name":movie_name,
        "Total Seating": 25,
        "Price": price,
        "Duration": duration,
        "Booked Seats": []
    }
    f=open(movie_json, "r+")
    try:
        content=json.load(f)
        if d not in content:
            content.append(d)
            f.seek(0)
            f.truncate()
            json.dump(content, f)
            f.close()
            return True
        else:
            print("Movie Already exists!!")
            f.close()
            return False
    except JSONDecodeError:
        content=[]
        content.append(d)
        json.dump(content, f)
        f.close()
        return True

def book_ticket(movie_json, user_json, email, tkt_id, no_of_booking, *preferred_seats):
    """
    It Returns True if the ticket was Booked
    It returns False if Ticket was not booked

    Args:
        movie_json (str): _description_
        user_json (str): _description_
        email (str): _description_
        tkt_id (str): _description_
        no_of_booking (tuple): _description_
    """
    # open the movie.json
    f=open(movie_json, "r+")
    content=json.load(f)
    count=0
    for i in range(len(content)):
        if content[i]["Movie ID"]==tkt_id:
            movie=content[i]
            seat_booked=len(content[i]["Booked Seats"])
            number_of_seat_av=content[i]["Total Seating"]-seat_booked
            count+=1
            break
    if count==0:
        return False
    
    # open the user json
    f1=open(user_json, "r+")
    content1=json.load(f1)
    count=0
    for i in range(len(content1)):
        if content1[i]["email"]==email:
            user=content1[i]
            count+=1
            break
    if count==0:
        return False
    
    # Seating Arrangement
    #   A  B  C  D  E
    # 1 A1 B1 C1 D1 E1 
    # 2 A2 B2 C2 D2 E2 
    # 3 A3 B3 C3 D3 E3 
    # 4 A4 B4 C4 D4 E4 
    # 5 A5 B5 C5 D5 E5 
    
    # Recollecting the available seats
    seats=[]
    for row in range(1,6):
        for col in range(ord("A"), ord("E")+1):
            if chr(col)+str(row) not in movie["Booked Seats"]:
                seats.append(chr(col)+str(row))
    
    # Booking Process
    if number_of_seat_av >= no_of_booking:
        for i in preferred_seats:
            if i not in seats:
                return False

        if preferred_seats:
            movie["Booked Seats"].extend(preferred_seats)
            user["booked history"].append(tkt_id)
        else:
            movie["Booked Seats"].extend(seats[:no_of_booking])
            user["booked history"].append(tkt_id)
    else:
        return False
    
    # save new data to user json
    for i in range(len(content1)):
        if content1[i]["email"]==email:
            content1[i]["booked history"]=user["booked history"]
            f1.seek(0)
            f1.truncate()
            json.dump(content1,f1)
            f1.close()
    
    # save new data to movie json
    for i in range(len(content)):
        if content[i]["Movie ID"]==tkt_id:
            content[i]["Booked Seats"]=movie["Booked Seats"]
            f.seek(0)
            f.truncate()
            json.dump(content, f)
            f.close()
    return True
            
    