import cards        # this is required

YAY_BANNER = """
__   __             __        ___                       _ _ _ 
\ \ / /_ _ _   _    \ \      / (_)_ __  _ __   ___ _ __| | | |
 \ V / _` | | | |    \ \ /\ / /| | '_ \| '_ \ / _ \ '__| | | |
  | | (_| | |_| |_    \ V  V / | | | | | | | |  __/ |  |_|_|_|
  |_|\__,_|\__, ( )    \_/\_/  |_|_| |_|_| |_|\___|_|  (_|_|_)
           |___/|/                                            

"""

RULES = """
    *------------------------------------------------------*
    *-------------* Thumb and Pouch Solitaire *------------*
    *------------------------------------------------------*
    Foundation: Columns are numbered 1, 2, ..., 4; built 
                up by rank and by suit from Ace to King. 
                You can't move any card from foundation, 
                you can just put in.

    Tableau:    Columns are numbered 1, 2, 3, ..., 7; built 
                down by rank only, but cards can't be laid on 
                one another if they are from the same suit. 
                You can move one or more faced-up cards from 
                one tableau to another. An empty spot can be 
                filled with any card(s) from any tableau or 
                the top card from the waste.
     
     To win, all cards must be in the Foundation.
"""

MENU = """
Game commands:
    TF x y     Move card from Tableau column x to Foundation y.
    TT x y n   Move pile of length n >= 1 from Tableau column x 
                to Tableau column y.
    WF x       Move the top card from the waste to Foundation x                
    WT x       Move the top card from the waste to Tableau column x        
    SW         Draw one card from Stock to Waste
    R          Restart the game with a re-shuffle.
    H          Display this menu of choices
    Q          Quit the game
"""

def valid_fnd_move(src_card, dest_card):
    """
        add your function header here.
    """
    pass  # stub; delete and replace it with your code
        
def valid_tab_move(src_card, dest_card):
    """
        add your function header here.
    """    
    pass  # stub; delete and replace it with your code
            
def tableau_to_foundation(tab, fnd):
    """
        add your function header here.
    """    
    pass  # stub; delete and replace it with your code
            

def tableau_to_tableau(tab1, tab2, n):
    """
        add your function header here.
    """    
    pass  # stub; delete and replace it with your code

def waste_to_foundation(waste, fnd, stock):
    """
        add your function header here.
    """    
    pass  # stub; delete and replace it with your code

def waste_to_tableau(waste, tab, stock):
    """
        add your function header here.
    """    
    pass  # stub; delete and replace it with your code
                    
def stock_to_waste(stock, waste):
    """
        add your function header here.
    """    
    pass  # stub; delete and replace it with your code
                            
def is_winner(foundation):
    """
        add your function header here.
    """    
    pass  # stub; delete and replace it with your code

def setup_game():
    """
        The game setup function, it has 4 foundation piles, 7 tableau piles, 
        1 stock and 1 waste pile. All of them are currently empty. This 
        function populates the tableau and the stock pile from a standard 
        card deck. 

        7 Tableau: There will be one card in the first pile, two cards in the 
        second, three in the third, and so on. The top card in each pile is 
        dealt face up, all others are face down. Total 28 cards.

        Stock: All the cards left on the deck (52 - 28 = 24 cards) will go 
        into the stock pile. 

        Waste: Initially, the top card from the stock will be moved into the 
        waste for play. Therefore, the waste will have 1 card and the stock 
        will be left with 23 cards at the initial set-up.

        This function will return a tuple: (foundation, tableau, stock, waste)
    """
    # you must use this deck for the entire game.
    # the stock works best as a 'deck' so initialize it as a 'deck'
    stock = cards.Deck()
    # the game piles are here, you must use these.
    foundation = [[], [], [], []]           # list of 4 lists
    tableau = [[], [], [], [], [], [], []]  # list of 7 lists
    waste = []                              # one list
    # your setup code goes here
    #pass  # stub; delete and replace it with your code
    tableau.append(stock.deal())    
    return foundation, tableau, stock, waste

def display_game(foundation, tableau, stock, waste):
    """
        add your function header here.
    """    
    pass  # stub; delete and replace it with your code


print(RULES)
fnd, tab, stock, waste = setup_game()
display_game(fnd, tab, stock, waste)
print(MENU)
command = input("prompt :> ")
while command.strip().lower() != 'q':
    try:
        
        pass  # stub; delete and replace it with your code
        
    except RuntimeError as error_message:  # any RuntimeError you raise lands here
        print("{:s}\nTry again.".format(str(error_message)))       
    display_game(fnd, tab, stock, waste)                
    command = input("prompt :> ")


