"""

"""

#import sys
#def input( prompt=None ):
#    if prompt != None:
#        print( prompt, end="" )
#    aaa_str = sys.stdin.readline()
#    aaa_str = aaa_str.rstrip( "\n" )
#    print( aaa_str )
#    return aaa_str
#

def open_file():
    ''' Returns a file pointer '''
    fileloc=input("Filename: ")
    try:
        fp = open(fileloc)
        return fp
    except FileNotFoundError:
        print("File not found.")
        fp=open_file()
        return fp   

def read_file(fp):  
    ''' Reads through the file and returns network'''
    # Read n and initizlize the network to have n empty lists -- 
    #    one empty list for each member of the network
    fp.seek(0)
    n = fp.readline()
    n = int(n)
    network = []
    for i in range(n):
        network.append([])
    for line in fp: #reads through and makes a list for every member
        #print(int(line.split()[0]))
        network[int(line.split()[0])].append(line.split()[1])
        network[int(line.split()[1])].append(line.split()[0])

    return network

def num_in_common_between_lists(list1, list2):
    ''' finds the number in common between lists'''
    incommon=0
    if len(list1)>=len(list2):
        for person1 in list1:
            for person2 in list2:
                if person1==person2:
                    incommon+=1
    else:#same thing just reversed
        for person2 in list2:
            for person1 in list1:
                if person1==person2:
                    incommon+=1
    return incommon 
def init_matrix(n):
    '''Create an nxn matrix, initialize with zeros, and return the matrix.'''
    matrix = []
    for row in range(n):  # for each of the n rows
        matrix.append([])  # create the row and initialize as empty
        for column in range(n):
            matrix[row].append(0)  # append a 0 for each of the n columns
    return matrix
    
def calc_similarity_scores(network):  
    ''' Calculates the similatity scores'''
    similarity_matrix=init_matrix(len(network))
    #print (similarity_matrix)
    #loops through the network twice to generate the number in common
    for i in range(len(network)):
        for j in range(len(network)):
            similarity_matrix[i][j]=num_in_common_between_lists(network[i],network[j])
    return similarity_matrix
     
def recommend(user_id,network,similarity_matrix):
    ''' recommends the next friend'''

    largest=0
    second=0
    for items in similarity_matrix[user_id]:
        if items>largest:
            if largest>0:
                second=largest
                print(second)
            largest=items

            #enumerates through the items to find the location of largest
    friend=[i for i,x in enumerate(similarity_matrix[user_id]) if x==largest]
    if len(friend)>1:
        for person in friend:
            if int(person) != int(user_id):
                return person
    return friend[0]

def main():
    print("Facebook friend recommendation.")
    fp=open_file()
    network=read_file(fp)#Builds the network
    similarity_matrix=calc_similarity_scores(network)#builds the similarity matrix
    fp.seek(0)
    top=fp.readline()
    user_id=input("Enter an integer in the range 0 to "+ str(int(top)-1)+": ")
    #Prompts for the user
    try:
        int(user_id)
    except:
        user_id=input("Enter an integer in the range 0 to "+ str(int(top)-1)+": ")
    while int(user_id) >int(int(top)-1) or int(user_id)<0:
        user_id=input("Enter an integer in the range 0 to "+ str(int(top)-1)+": ")
    print("The suggested friend for "+str(user_id)+ " is "+str(recommend(int(user_id),network,similarity_matrix)))
    cont=input("Do you want to continue(yes/no)? ")
    while cont.lower() != 'no':
        user_id=input("Enter an integer in the range 0 to "+ str(int(top)-1)+": ")
        try:
            int(user_id)
        except:
            user_id=input("Enter an integer in the range 0 to "+ str(int(top)-1)+": ")
        while int(user_id) >int(int(top)-1) or int(user_id)<0:
            user_id=input("Enter an integer in the range 0 to "+ str(int(top)-1)+": ")
        print("The suggested friend for "+str(user_id)+ " is "+str(recommend(int(user_id),network,similarity_matrix)))
        cont=input("Do you want to continue(yes/no)? ")
    #while cont=="yes":


if __name__ == "__main__":
    main()

