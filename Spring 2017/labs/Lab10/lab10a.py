
import string

def build_word_set( input_file ):
    
    word_set = set()
    
    for line in input_file:

        # splits the line into a list of words
        word_lst = line.strip().split()

        # removes punctuation and makes them all lower
        word_lst = [w.lower().strip(string.punctuation) for w in word_lst]
        
        for word in word_lst:
            
            if word != "":

                # adds the word if it isn't blank to the word_set
                word_set.add( word )
                
    return word_set


def compare_files( file1, file2 ):

    # Build two sets:
    #   all of the unique words in file1
    #   all of the unique words in file2
    word_set1=build_word_set(file1)
    word_set2=build_word_set(file2)
    #print(word_set1,word_set2)
    #print(len(word_set1)+len(word_set2))
    word_setboth=word_set1.intersection(word_set2)
    word_setsym=word_set1.symmetric_difference(word_set2)
    print("Total Number of Unique Words",len(word_setboth)+len(word_setsym))
    # Display the total number of unique words between the
    # two files.  If a word appears in both files, it should
    # only be counted once.
    print("Number Of Unique Words Which Appear in both files",len(word_setboth))
    # Display the number of unique words which appear in both
    # files.  A word should only be counted if it is present in
    # both files.

  
     
######################################################################

f1 = open( "document1.txt" )
f2 = open( "document2.txt" )

compare_files( f1, f2 )

f1.close()
f2.close()

