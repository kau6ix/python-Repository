films={
    "Finding Dory":[3,5],
    "Bourne":[18,5],
    "Tarzan":[15,5],
    "Ghost Busters":[12,5]
    }
while True:
    choice=input("What movie you want to watch ? ").strip().title()
    if choice in films:
        age=int(input("How old are you ").strip())
        if age>=films[choice][0]:
            seats=films[choice][1]
            if seats>0:
                print("Enjoy the film")
                films[choice][1]=films[choice][1]-1
            else:
                print("Sorry :( we are sold out")
        else:
            print("You are too young")
    else:
        print("Sorry :( we do not have {}".format(choice))
