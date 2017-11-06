#/usr/bin/python3

"""
    # TicTacToe!
    
    TicTacToe! is a tictactoe game with 'fake' graphics.
    
    # HOW TO PLAY
    The program will draw a board for you. The first player (the game always start with player X) will be asked which slot he or she wants to fill.
    Each slot has a unique code:
    
    ----------------
    | t1 | t2 | t3 |
    ----------------
    | t4 | t5 | t6 |
    ----------------
    | t7 | t8 | t9 |
    ----------------
    
    
    So if you want to fill the slot in the upper right corner, you type 't3'. For the slot in the middle, you type 't5' etc.
    
    Have fun playing this game with your friends and feel free to improve this script!
"""

__status__ = 'Stable'
__version__ = '1.1'
__author__ = 'Bas Kasemir'

def drawboard(tiles,player):
    """
        Function that draws a board and fills the slots. It also creates a list of empty slots.
        
        Args:
            player: the current player (X or O)
            tiles: dictionary which is holding the tiles and their values
        
        Returns:
            Nothing, but calls the askinput() function and passes the player, the empty slots and the tiles
    """
    rowdivider = "-------------"
    possible = []
    print(rowdivider)
    for key in tiles:
        if key is "t3" or key is "t6" or key is "t9":
            print("| {} |\n{}".format(tiles[key],rowdivider))
        else:
            print("| {} ".format(tiles[key]), end="")
        if tiles[key] is " ":
            possible.append(key)
    
    askinput(player, possible, tiles)

def askinput(player, possible, tiles):
    """
        Function that ask the player which slot he wants to fill and checks if the given slot is empty. if it's empty it will fill the slot by filling the dictionary.
        
        Args:
            player: the current player (X or O)
            possible: a list of empty slots
            tiles: dictionary which is holding the tiles and their values
        
        Returns:
            Nothing, but calls a new function and passes the player and the tiles
        
        Exeptions:
            KeyError: If the input is not a empty slot, it will output an ERROR message with solution and asks again.
    """
    try:
        tileinput = str(input("Player {}, please type a location: {}\n".format(player, possible)))
        if tileinput not in possible:
            raise KeyError
        else:
            tiles[tileinput] = player
            checkwin(tiles, player)
    except KeyError:
        print("\n/!\ WARNING: You did not choose a empty slot, try again.")
        askinput(player, possible, tiles)

def checkwin(tiles, player):
    """
        Function that checks if the tiles in a winning row are all filled and if so, if they are the same. If it's all true the program will print which player wins this round. Otherwise it will call the drawboard() function to draw the board again.
        
        Args:
            tiles: dictionary which is holding the tiles and their values
            player: the current player (X or O)
        
        Returns:
            Nothing, but calls a new function and passes the player, the tiles to draw board. Or it will print which player wins the round.
    """
    if tiles["t1"] is not " " and tiles["t2"] is not " " and tiles["t3"] is not " ":
        if tiles["t1"] is tiles["t2"] is tiles["t3"]:
            print("\nPlayer {} wins! \n".format(player))
        else:
            if player is "X":
                player = "O"
            else:
                player = "X"
            drawboard(tiles, player)
    elif tiles["t4"] is not " " and tiles["t5"] is not " " and tiles["t6"] is not " ":
        if tiles["t4"] is tiles["t5"] is tiles["t6"]:
            print("\nPlayer {} wins! \n".format(player))
        else:
            if player is "X":
                player = "O"
            else:
                player = "X"
            drawboard(tiles, player)
    elif tiles["t7"] is not " " and tiles["t8"] is not " " and tiles["t9"] is not " ":
        if tiles["t7"] is tiles["t8"] is tiles["t9"]:
            print("\nPlayer {} wins! \n".format(player))
        else:
            if player is "X":
                player = "O"
            else:
                player = "X"
            drawboard(tiles, player)
    elif tiles["t1"] is not " " and tiles["t5"] is not " " and tiles["t9"] is not " ":
        if tiles["t1"] is tiles["t5"] is tiles["t9"]:
            print("\nPlayer {} wins! \n".format(player))
        else:
            if player is "X":
                player = "O"
            else:
                player = "X"
            drawboard(tiles, player)
    elif tiles["t3"] is not " " and tiles["t5"] is not " " and tiles["t7"] is not " ":
        if tiles["t3"] is tiles["t5"] is tiles["t7"]:
            print("\nPlayer {} wins! \n".format(player))
        else:
            if player is "X":
                player = "O"
            else:
                player = "X"
            drawboard(tiles, player)
    else:
        if player is "X":
            player = "O"
        else:
            player = "X"
        drawboard(tiles, player)

if __name__ == '__main__':
    player = "X"
    tiles = {"t1": " ", "t2": " ", "t3": " ", "t4": " ", "t5": " ", "t6": " ", "t7": " ", "t8": " ", "t9": " "}
    drawboard(tiles, player)
