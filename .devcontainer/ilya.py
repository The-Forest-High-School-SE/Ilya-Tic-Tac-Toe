table = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
player1 = "X"
player2 = "O"

name1 = input("Player 1 Name: ")
name2 = input('Player 2 Name: ')

def print_grid():
    grid = "| "
    gridnum = 0
    for i in range(7):
        grid = grid + str(table[gridnum]) + " | "
        gridnum = gridnum + 1
        if gridnum == 2 or gridnum == 5:
            grid = grid + str(table[gridnum]) + " | "
            print(grid)
            grid = "| "
            print("_____________")
            gridnum = gridnum + 1
    print(grid)

def check_win():
    return False

print_grid()

turn = 0
# Need a while loop in here which would call check_win() and check for the number
# of turns
for e in range(len(table)):
    # You're not changing the turn here.
    # See if you can also think of a better way of telling if the 
    # turn is odd or even

    # There's a problem with how you're adding the 'X' - see if you can
    # work that out.
    if turn == 0 or turn == 2 or turn == 4 or turn == 6 or turn == 8:
        print(f'{name1}\'s turn!')
        markplace = int(input('Which cell would you like to place your mark in? (Choose 1-9) '))
        table[markplace] = [player1]
        print_grid()

    elif turn == 1 or turn == 3 or turn == 5 or turn == 7:
        print(f'{name2}\'s turn!')
        markplace = int(input('Which cell would you like to place your mark in? (Choose 1-9)'))
        table[markplace] = [player2]
        print_grid()

    else:
        print('End game!')
   
    

    

