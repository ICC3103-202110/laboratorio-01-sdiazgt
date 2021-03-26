import random
# Creat_list creats the board that will be use in the game
def Creat_list(cards):
    number = cards
    visual =[] #visual will contain only the "#" symbol
    for i in range(2):
        visual.append([])
        for j in range(number):
            visual[i].append("#")
    
    mix = [] #mix will add all the numbers to a list and mix them
    for i in range(number+1):
        if i > 0:
            mix.append(i)
            mix.append(i)
    random.shuffle(mix)
    
    # Real will have the same shape as visual but with the numbers of mix
    Real = []
    for i in range(2):
        Real.append([])
        for j in range(number):
            Real[i].append(mix[0])
            mix.pop(0)
    print(Real)
    print("↑↑↑↑↑Only use for Testing and Checking↑↑↑↑↑\n") #This print can be erase, but it can help cheking if
    return [visual,Real]                         #the location are working properly.

# board_print is use to print the board when is asked
def board_print(in_use_board):
    board= in_use_board
    for i in range(len(board)):
        print(" ",i, end="") 
        
    print(" ")
    print("")
    x=0
    for a in zip(*board):   #Zip() prints the list in a vertical way
        print(x,end="  ")
        print(" ".join(map(str, a)))
        x += 1
    return

# turn_around receives the selected location and "flips" a card
def turn_around(list_i,position):
    real = list_i[1]   
    cencored = list_i[0]
    x = int(position.split(sep=',')[0])
    y = int(position.split(sep=',')[1])
    if cencored[x][y] == " ": # if you select a "blank" location
        reint = input("Select a new Location ")
        list_i1 = list_i
        turn_around(list_i1,reint)
    cencored[x][y] = real[x][y]
    board_print(cencored)
    return cencored

# Verification verifies the flip numbers are the same
#and gives the signal to give a point
def verification(board,n1,n2):
    tab = board
    points = 0
    x1 = int(n1.split(sep=',')[0])
    y1 = int(n1.split(sep=',')[1])
    x2 = int(n2.split(sep=',')[0])
    y2 = int(n2.split(sep=',')[1])
    if int(tab[x1][y1]) == int(tab[x2][y2]):
        print("\nYou found a pair")
        tab[x1][y1] = " "
        tab[x2][y2] = " "
        points = 1
        return [tab, points]
    else:
        print("\nThey are not the same")
        tab[x1][y1] = "#"
        tab[x2][y2] = "#"
        points = 0
        return [tab,points]




active = 0
player1 = 0
player2 = 0
xx = ""
yy = ""
x1 = ""
x2 = ""
y1 = ""
y2 = ""
add = []
turn = 0
total = 0
cards = int(input("How many cards do you want?: "))
creat = Creat_list(cards)
while active == 0:
    if total == cards:
        print("The game is over")
        if player1 > player2:
            print("Player 1 won with %s points"% (player1))
        elif player1 < player2:
            print("Player 2 won with %s points"% (player1))
        elif player1 == player2:
            print("DRAW")
        break
    elif turn == 0:
        board_print(creat[0])
        print("\nPlayer 1 is your turn! ")
        xx = str(input("Select a coordinate using the format x,y (Ej. 0,0 is the first card):"))
        creat[0] = turn_around(creat,xx)
        yy = str(input("Select a Second coordinate using the format x,y (Ej. 0,0 is the first card):"))
        creat[0] = turn_around(creat,yy)
        if xx == yy:
            x1 = int(xx.split(sep=',')[0])
            y1 = int(xx.split(sep=',')[1])
            x2 = int(yy.split(sep=',')[0])
            y2 = int(yy.split(sep=',')[1])
            creat[0][x1][y1] = "#"
            creat[0][x2][y2] = "#"
            print("\nYou can't select the same position")
            continue
        add = verification(creat[0],xx,yy)
        creat[0] = add[0]
        if int(add[1]) == 1:
            player1 += 1
            total += 1
            turn = 0
            print("Player 1 you won a point")
            print("You have %s points in total" % (player1))
        elif int(add[1]) == 0:
            turn = 1
    elif total == cards:
        continue
    elif turn == 1:
        board_print(creat[0])
        print("\nPlayer 2 is your turn! ")
        xx = str(input("Select a coordinate using the format x,y (Ej. 0,0 is the first card):"))
        creat[0] = turn_around(creat,xx)
        yy = str(input("Select a Second coordinate using the format x,y (Ej. 0,0 is the first card):"))
        creat[0] = turn_around(creat,yy)
        add = verification(creat[0],xx,yy)
        creat[0] = add[0]
        if int(add[1]) == 1:
            player2 += 1
            total += 1
            turn = 1
            print("Player 2 you won a point")
            print("You have %s points in total" % (player2))
        elif int(add[1]) == 0:
            turn = 0


    