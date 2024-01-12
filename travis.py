users=["Alice","Bob","Claire","Dan","Emma","Fred","Geogie","Harry"]

while True:
    print("Hi, My name id Travis")
    name=input("What is your name? ").strip().capitalize()
    if name in users:
        print("Hello! {} name recognised".format(name))
        remove=input("Would you like to be removed from the System (y/n)? : ").lower()
        if remove=="y":
            print(users)
            users.remove(name)
            print(users)
    else:
        print("Hmmm I don't think I have met you yet{}".format(name))
        add_me=input("would you like to be added to the system (y/n)? ").strip().lower()
        if add_me=="y":
            print(users)
            users.append(name)
            print(users)
            
