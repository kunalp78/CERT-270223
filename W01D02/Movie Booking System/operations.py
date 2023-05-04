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
    return False