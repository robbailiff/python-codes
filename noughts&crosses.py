"""
This is a noughts and crosses (tic-tac-toe) game I made to try and reinforce few of the concepts I've learnt so far. 
This version I have made to take player input. 
I have also created a Sololearn Version which replaces player input with a random generator.
I have tested it many times and I think I've managed to weed out most of the bugs.
"""

"""
=========
Functions
=========
"""

# Function to print the 3 x 3 board
def print_board():
    print("""

         |     |
      {}  |  {}  |  {}
    -----|-----|------
      {}  |  {}  |  {}
    -----|-----|------
      {}  |  {}  |  {}
         |     |

    """.format(*board_list))


# Function to check to see if anyone has won
def win_condition(marker):

    if board_list[0] == board_list[1] == board_list[2] == marker:
        return 0

    elif board_list[3] == board_list[4] == board_list[5] == marker:
        return 0

    elif board_list[6] == board_list[7] == board_list[8] == marker:
        return 0

    elif board_list[0] == board_list[3] == board_list[6] == marker:
        return 0

    elif board_list[1] == board_list[4] == board_list[7] == marker:
        return 0

    elif board_list[2] == board_list[5] == board_list[8] == marker:
        return 0

    elif board_list[0] == board_list[4] == board_list[8] == marker:
        return 0

    elif board_list[2] == board_list[4] == board_list[6] == marker:
        return 0

    else:
        pass

# Function to check to see if the board is full
def board_check():
    num_list = [1,2,3,4,5,6,7,8,9]
    full = int(1)

    # Loop to iterate through num_list
    for i in board_list:
        if i in num_list:
            full = 1
            if full == 1:
                break
        else:
            full = 0

    # Returns a value based on if any numbers are left in board_list
    if full == 1:
        return 1
    else:
        return 0


"""
================
Start of program
================
"""

board_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

p1_marker = "X"
p2_marker = "O"
p1_win = int(1)
p2_win = int(1)
board_full = int(1)

print("""
Noughts and Crosses
=================== """)

print_board()


while p1_win != 0 and p2_win != 0 and board_full != 0:


    while p1_win != 0 and p2_win != 0 and board_full != 0:

        print("Player 1, it's your turn.")
        p1_input = int(input("Enter a position on the board: "))
        if p1_input not in board_list:
            print("Position already taken.")

        else:
            p1_idx = (p1_input - 1)
            board_list[p1_idx] = "X"

            print_board()

            p1_win = win_condition(p1_marker)
            board_full = board_check()
            #print(f"Board Full is equal to {board_full}")
            break



    while p1_win != 0 and p2_win != 0 and board_full != 0:

        print("Player 2, it's your turn.")
        p2_input = int(input("Enter a position on the board: "))
        if p2_input not in board_list:
            print("Position already taken.")

        else:
            p2_idx = (p2_input - 1)
            board_list[p2_idx] = "O"

            print_board()

            p2_win = win_condition(p2_marker)
            board_full = board_check()
            break


if p1_win == 0:
    print("Player 1 wins!")

elif p2_win == 0:
    print("Player 2 wins!")

elif board_full == 0:
    print("Board is full.")
    print("It's a draw!")
