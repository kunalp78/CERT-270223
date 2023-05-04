import operations as op
while 1:
    print("Menu: ")
    print("1) Write a diary")
    print("2) Read the Diary")
    print("3) Exit!!")
    i = input("Enter you choice between [1-3]: ")
    if i == "3":
        print("Exiting!!")
        break
    elif i == "1":
        op.write_diary("diary.json")
    elif i == "2":
        date = input("Enter the date in foll fromat: Tue-May-D-YYYY: ")
        op.read_diary("diary.json", date)
    else:
        print("Hey you entered incorrect response!!")