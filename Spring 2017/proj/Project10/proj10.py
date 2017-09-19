import cards  # This is necessary for the project


BANNER = """
    __        _____ _   _ _   _ _____ ____  _ _ _ 
    \ \      / /_ _| \ | | \ | | ____|  _ \| | | |
     \ \ /\ / / | ||  \| |  \| |  _| | |_) | | | |
      \ V  V /  | || |\  | |\  | |___|  _ <|_|_|_|
       \_/\_/  |___|_| \_|_| \_|_____|_| \_(_|_|_)

"""


RULES = """
     ____        _             _        ____
    | __ )  __ _| | _____ _ __( )___   / ___| __ _ _ __ ___   ___
    |  _ \ / _` | |/ / _ \ '__|// __| | |  _ / _` | '_ ` _ \ / _ \\
    | |_) | (_| |   <  __/ |    \__ \ | |_| | (_| | | | | | |  __/
    |____/ \__,_|_|\_\___|_|    |___/  \____|\__,_|_| |_| |_|\___|

    Cells:       Cells are numbered 1 through 4. They can hold a
                 single card each.

    Foundations: Foundations are numbered 1 through 4. They are
                 built up by rank from Ace to King for each suit.
                 All cards must be in the foundations to win.

    Tableaus:    Tableaus are numbered 1 through 8. They are dealt
                 to at the start of the game from left to right
                 until all cards are dealt. Cards can be moved one
                 at a time from tableaus to cells, foundations, or
                 other tableaus. Tableaus are built down by rank
                 and cards must be of the same suit.

"""


MENU = """

    Game commands:
    
    TC x y    Move card from tableau x to cell y
    TF x y    Move card from tableau x to foundation y
    TT x y    Move card from tableau x to tableau y
    CF x y    Move card from cell x to foundation y
    CT x y    Move card from cell x to tableau y
    R         Restart the game with a re-shuffle
    H         Display this menu of commands
    Q         Quit the game
    
"""


def valid_fnd_move(src_card, dest_card):
    """
    Checks to see if the fnd move is valid by checking the suit and rank
    """
    if dest_card == None:
        if src_card.rank() == 1:
            pass
        else:
            #Raises the errors so that the action doesn't complete
            raise RuntimeError("Error: Source card not an ace")
    else:
        if src_card.suit() == dest_card.suit():
            if src_card.rank() == dest_card.rank()+1:
                pass
            else:
                #Raises the errors so that the action doesn't complete
                raise RuntimeError("Error: Rank Mismatch")
        else:
            #Raises the errors so that the action doesn't complete
            raise RuntimeError("Error: Suit Mismatch")


def valid_tab_move(src_card, dest_card):
    """
    Checks to see if the tab move is valid takes in
    the card to be moved and the card it will be moved onto
    """

    if dest_card == None:
        pass
    else:
        if src_card.suit() == dest_card.suit():
            if src_card.rank()+1 == dest_card.rank():
                pass
            else:
                #Raises the errors so that the action doesn't complete
                raise RuntimeError("Error: Rank Mismatch")
        else:
            #Raises the errors so that the action doesn't complete
            raise RuntimeError("Error: Suit Mismatch")


def tableau_to_cell(tab, cell):
    """
    Moves a card from a tab to the cell
    """
    #To have my formatting work properly made sure that all of the lists where 100 in length

    if tab[-1] == '':
        # print('test')
        tab.pop()
        tableau_to_cell(tab, cell)
    else:
        # print(tab)
        # print(cell[-1])
        if cell[-1] == None:
            cell.append(tab.pop())
            while len(tab) < 100:
                tab.append('')
        else:
            while len(tab) < 100:
                tab.append('')
            #Raises the errors so that the action doesn't complete    
            raise RuntimeError("Error: Cell is not empty")


def tableau_to_foundation(tab, fnd):
    """
    Moves card from tab to a fnd
    """
    #List length
    if tab[-1] == '':
        tab.pop()
        tableau_to_foundation(tab, fnd)
    else:
        try:
            valid_fnd_move(tab[-1], fnd[-1])
            fnd.append(tab.pop())
            while len(tab) < 100:
                tab.append('')
        except:
            while len(tab) < 100:
                tab.append('')
            raise RuntimeError("Error : invalid command")


def tableau_to_tableau(tab1, tab2):
    """
    Move card from tab to tab
    """
    #maintain list len
    if tab1[-1] == '':
        print('test')
        tab1.pop()
        tableau_to_tableau(tab1, tab2)
    elif tab2[-1] == '':
        print('test2')
        tab2.pop()
        tableau_to_tableau(tab1, tab2)
    else:
        valid_tab_move(tab1[-1], tab2[-1])
        tab2.append(tab1.pop())
        while len(tab1) < 100:
            tab1.append('')
        while len(tab2) < 100:
            tab2.append('')


def cell_to_foundation(cell, fnd):
    """
    Moves a card from a cell to a fnd
    """
    if cell[-1] != None:
        valid_fnd_move(cell[-1], fnd[-1])
        fnd.append(cell.pop())
    else:
        raise RuntimeError("Error: Cell is Empty")


def cell_to_tableau(cell, tab):
    """
    moves a card from a cell to give tab
    """
    #maintain list len for formatting
    if tab[-1] == '':
        tab.pop()
        cell_to_tableau(cell, tab)
    else:
        if cell[-1] != None:
            valid_tab_move(cell[-1], tab[-1])
            tab.append(cell.pop())
        else:
            while len(tab) < 100:
                tab.append('')
            raise RuntimeError("Error: Cell is Empty")


def is_winner(foundations):
    """
    If the len of the fnds is 14 because of the none value in the beginning then winner.
    """
    if len(foundations[0])==14 and foundations[0][-1].rank()==13 and len(foundations[1])==14 and foundations[1][-1].rank()==13 and len(foundations[2])==14 and foundations[2][-1].rank()==13 and len(foundations[3])==14 and foundations[3][-1].rank()==13:
        return True
    else: return False


def setup_game():
    """
    The game setup function. It has 4 cells, 4 foundations, and 8 tableaus. All
    of these are currently empty. This function populates the tableaus from a
    standard card deck. 

    Tableaus: All cards are dealt out from left to right (meaning from tableau
    1 to 8). Thus we will end up with 7 cards in tableaus 1 through 4, and 6
    cards in tableaus 5 through 8 (52/8 = 6 with remainder 4).

    This function will return a tuple: (cells, foundations, tableaus)
    """

    # You must use this deck for the entire game.
    # We are using our cards.py file, so use the Deck class from it.
    stock = cards.Deck()
    # The game piles are here, you must use these.
    cells = [[], [], [], []]  # list of 4 lists
    foundations = [[], [], [], []]  # list of 4 lists
    tableaus = [[], [], [], [], [], [], [], []]  # list of 8 lists
    # print(stock)
    """ YOUR SETUP CODE GOES HERE """
    # Replace this pass statement with your own code
    for a in range(0, 7):
        for table in range(len(tableaus)):
            card = stock.deal()
            if card == None:
                card = ''
            tableaus[table].append(card)

    for a in range(0, 4):
        foundations[a].append(None)
        cells[a].append(None)
    #Make all tab list 100 to maintain a nice formatting
    while(len(tableaus[0])) < 100:
        tableaus[0].append('')
    while(len(tableaus[1])) < 100:
        tableaus[1].append('')
    while(len(tableaus[2])) < 100:
        tableaus[2].append('')
    while(len(tableaus[3])) < 100:
        tableaus[3].append('')
    while(len(tableaus[4])) < 100:
        tableaus[4].append('')
    while(len(tableaus[5])) < 100:
        tableaus[5].append('')
    while(len(tableaus[6])) < 100:
        tableaus[6].append('')
    while(len(tableaus[7])) < 100:
        tableaus[7].append('')
    return cells, foundations, tableaus


def display_game(cells, foundations, tableaus):
    """
    Takes in cells fnds and tabs to display the game board
    """
    # Labels for cells and foundations
    print("    =======Cells========  ====Foundations=====")
    print("     --1----2----3----4--  --1----2----3----4--")
    print("       ", end="")
    for c in cells:
        if c[-1] != None:
            print('{}'.format(str(c[-1])), end='   ')
        else:
            print('  ', end='   ')
    for f in foundations:
        if f[-1] != None:
            print('{}'.format(str(f[-1])), end='    ')
        else:
            print('   ', end='   ')
    # to print a card using formatting, convert it to string:
    # print("{}".format(str(card)))

    print()
    # Labels for tableaus
    print("    =================Tableaus=================")
    print("    ---1----2----3----4----5----6----7----8---")
    #formatting for the tableaus
    try:
        for row in range(0, 100):#if statement below makes sure there is something to be printed
            if tableaus[0][row] != '' or tableaus[1][row] != '' or tableaus[2][row] != '' or tableaus[3][row] != '' or tableaus[4][row] != '' or tableaus[5][row] != '' or tableaus[6][row] != '' or tableaus[7][row] != '':
                print("       {:4s}".format(str(tableaus[0][row])), end=' ')
                print("{:4s}".format(str(tableaus[1][row])), end=' ')
                print("{:4s}".format(str(tableaus[2][row])), end=' ')
                print("{:4s}".format(str(tableaus[3][row])), end=' ')
                print("{:4s}".format(str(tableaus[4][row])), end=' ')
                print("{:4s}".format(str(tableaus[5][row])), end=' ')
                print("{:4s}".format(str(tableaus[6][row])), end=' ')
                print("{:4s}".format(str(tableaus[7][row])), end=' ')
                print()
    except Exception as e:
        pass
        # print(e)
# HERE IS THE MAIN BODY OF OUR CODE
print(RULES)
cells, fnds, tabs = setup_game()
display_game(cells, fnds, tabs)
print(MENU)
command = input("prompt :> ").strip().lower()
while command != 'q':
    try:#splits the command up so that we can get usable peices
        command = command.split()
        # print(command)
        # if command[0] == 'printtab':
        #     print(tabs)
        # if command[0] == 'printcell':
        #     print(cells)
        # if command[0] == 'printfnds':
        #     print(fnds)
        if command[0] == 'tf':
            tableau_to_foundation(
                tabs[int(command[1])-1], fnds[int(command[2])-1])
        if command[0] == 'tt':
            tableau_to_tableau(tabs[int(command[1])-1],
                               tabs[int(command[2])-1])
        if command[0] == 'tc':
            tableau_to_cell(tabs[int(command[1])-1], cells[int(command[2])-1])
        if command[0] == 'cf':
            cell_to_foundation(cells[int(command[1])-1],
                               fnds[int(command[2])-1])
        if command[0] == 'ct':
            cell_to_tableau(cells[int(command[1])-1], tabs[int(command[2])-1])
        if command[0]=='h':
            print(MENU)
        if command[0]=='r':
            cells,fnds,tabs=setup_game()
    # Any RuntimeError you raise lands here
    except RuntimeError as error_message:
        print("{:s}\nTry again.".format(str(error_message)))
    except IndexError as error_message:
        print("Try again.")

    display_game(cells, fnds, tabs)
    if is_winner()==True:
        print(BANNER)
        command='q'
    else:  
        command = input("prompt :> ").strip().lower()
