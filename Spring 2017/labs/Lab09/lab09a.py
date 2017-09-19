
import string
from operator import itemgetter


def add_word( word_map, word ):
    '''Addes a word to the given dictionary if the word exist in the diction the value ticker is up one'''
    # Adds word to the word_map dictionary and sets it found value to zero

    if word not in word_map:
        word_map[ word ] = 0

    # Adds one an already existing value in the dictionary of word_map
    word_map[ word ] += 1


def build_map( in_file, word_map ):
    '''This builds the word map'''
    for line in in_file:

        # splits the line in the file and adds it to the word list
        word_list = line.split()

        for word in word_list:
            # strips any punctuation from the string such as !.?,
            word = word.strip().strip(string.punctuation)
            add_word( word_map, word.lower() )
        

def display_map( word_map ):
    '''Prints out all the words in the given dictionary'''
    word_list = list()
    del word_map['']
    # goes through every word in word_map and then appends the word and the count to the word_list
    for word, count in word_map.items():
        word_list.append( (word, count) )

    # sorts list by frequency of word
    freq_list = sorted( sorted(word_list),reverse=True, key=itemgetter(1) )

    print( "\n{:15s}{:5s}".format( "Word", "Count" ) )
    print( "-"*20 )
    for item in freq_list:
        print( "{:15s}{:>5d}".format( item[0], item[1] ) )


def open_file():
    '''Opens a file'''
    try:
        fileloc=input("Select a datafile: ")
        in_file=open(fileloc)
    except IOError:
        print( "\n*** unable to open file ***\n" )
        in_file = None

    return in_file


word_map = dict()
in_file = open_file()

if in_file != None:

    build_map( in_file, word_map )
    display_map( word_map )
    in_file.close()


