x = 1
y = 1

while x <= 3 and y <= 3:
    
    if x == 1 and y == 1:
        Movement = input(" You can go North: ")
        if Movement == "N" or Movement == "n":
            y += 1
        else:
            print("Not a valid direction!")
    elif x == 1 and y == 2:
        Movement = input("You can go (N)orth, (E)ast or (S)outh: ")
        if Movement == "N" or Movement == "n":
            y += 1
        elif Movement == "E" or Movement == "e":
            x += 1
        elif Movement == "S" or Movement == "s":
            y -= 1
        else:
            print("Not a valid direction!")
    
    elif x == 2 and y == 2:
        Movement = input("you can go (S)outh or (W)est: ")
        if Movement == "S" or Movement == "s":
            y -= 1
        elif Movement == "W" or Movement == "w":
            x -= 1
        else:
            print("Not a valid direction!")
    
    elif x == 2 and y == 1:
        Movement = input("you can go (N)orth: ")
        if Movement == "N" or Movement == "n":
            y += 1
        else:
            print("Not a valid direction!")

    elif x == 1 and y == 3:
        Movement = input("you can go EAST or SOUTH: ")
        if Movement == "E" or Movement == "e":
            x += 1
        elif Movement == "S" or Movement == "s":
            y -= 1
        else:
            print("Not a valid direction!")

    elif x == 2 and y == 3:
        Movement = input(" you can go west or east: ")
        if Movement == "W" or Movement == "w":
            x += 1
        elif Movement == "E" or Movement == "e":
            x -= 1
        else: 
            print("Not a valid direction!")
    
    elif x == 3 and y == 3:
        Movement = input("you can go south or west: ")
        if Movement == "S" or Movement == "s":
            y -= 1
        elif Movement == "W" or Movement == "w":
            x -= 1
        else:
            print("Not a valid direction!")
    
    elif x == 3 and y == 2:
        Movement = input("you can go North or South: ")
        if Movement == "S" or Movement == "s":
            y -= 1
        elif Movement == "N" or Movement == "n":
            y += 1
        else:
            print("Not a valid direction!")
    
    elif x == 3 and y == 1:
        print("You Won")