films {
    "Finding Doy":[3,5],
    "Bourne":[18,5],
    "Tarzan":[15,5],
    "Ghost Busters";[12,5]
    }
while True:
    choice = input("What film you want to watch? ").strip().title()

    if choice in films:
        age = int(input("What is your age? ").strip())
        
        if age >= films[choice][0]:
            
            if films[choice][1] > 0:
            print("Enjoy your film.")
            films[choice][1] = films[choice][1] - 1
            else:
                print("sorry we are sold out.")
        else:
            print("Sorry you ate too young to watch this film.")

    else:
        print("sorry we don't have that film.")

        
