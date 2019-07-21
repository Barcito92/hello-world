guest =[]
name =" "

while name !="NO":
    data=input('Insert the names for the list (Type NO to stop adding): ').upper()
    guest.append(data)
    if data == "NO":
        name="NO"
        guest.remove('NO')
        print("the list sorted is:")
        guest.sort()
        for guest in guest:
            print(guest)
