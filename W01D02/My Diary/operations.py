import json
from json import JSONDecodeError
import time
import re

def write_diary(diary_json):
    t=time.asctime().split()
    t.pop(3)
    print(t)
    key = "-".join(t)
    cli = input("[>]")
    f=open(diary_json, "r+")
    try:
        content=json.load(f)
    except JSONDecodeError:
        content=[]
    count = 0
    while 1:
        if re.search("^exit$", cli):
            print("Saving the data!!")
            f.seek(0)
            f.truncate()
            json.dump(content, f)
            f.close()
            break
        else:
            if len(content)==0:
                d = { key: []}
                d[key].append(cli)
                content.append(d)
            for i in range(len(content)):
                if key in content[i].keys():
                    count+=1
                    content[i][key].append(cli)
                    break
            if count == 0:
                d= {
                    key: []
                }
                d[key].append(cli)
                content.append(d)

        cli=input("[>]")

def read_diary(diary_json, date):
    f=open(diary_json, "r+")
    content=json.load(f)
    diary_list = []
    for i in range(len(content)):
        if date in content[i].keys():
            diary_list=content[i][date]
            f.close()
            break
    if diary_list:
        for i in diary_list:
            print(i)
    else:
        print("the date is invalid")