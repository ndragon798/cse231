
import itertools

class Matrix(object):
    '''Matrix class that reads in a fp and generates a matrix based on adjacency'''
    
    def __init__(self):  # no modification is needed for this method, but you may modify it if you wish to
        '''Create and initialize your class attributes.'''
        self._matrix = []
        self._rooms = 0
        
    def read_file(self,fp):  #fp is a file pointer
        '''Build an adjacency matrix that you read from a file fp.'''

        for line in fp:
            line=line.split()
            if len(line)==1:
                self._rooms=int(line[0])
                #print(self._rooms)
                for i in range(0,self._rooms):
                    self._matrix.append(set())
                #print(self._matrix)
            else:#Appends each number in the line to their own set and to the other set
                self._matrix[int(line[0])-1].add(int(line[1]))
                self._matrix[int(line[1])-1].add(int(line[0]))

        #print(self._matrix)
    def __str__(self):
        '''Return the matrix as a string.'''
        s = ''

        for item in range(len(self._matrix)):
            s=s+str(item+1)+": "
            for a in self._matrix[item]:
                s=s+str(a)+' '
            s=s+'\n'
        return s  #__str__ always returns a string

    def __repr__(self):  # no modification need of this method
        '''Call __str__() to return a string for displaying in the shell'''
        return self.__str__()  
        
    def adjacent(self,index):
        '''Return the set of connecting rooms to room specified by index'''
        return self._matrix[index-1]

    def rooms(self):
        '''Return the number of rooms'''
        return self._rooms

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

def main():
    M=Matrix()
    M.read_file(open_file())

    Done=False
    num_ta=0
    '''
    While statement below loops through and tries to determine
    the number of tas needed and where to place them
    It does this but generating a list of all possible solutions using 1 ta and working up 
    then checking to see if it can get all rooms filled
    '''
    while Done!=True:
        num_ta+=1
        roomlst=set()
        for i in range(1,M.rooms()+1):
            roomlst.add(i)
        roomlst1=set()

        combos=list(itertools.combinations(list(roomlst),num_ta))
        for comb in combos:
            for item in comb:
                try:
                    roomlst1.update(M.adjacent(item))
                    roomlst1.add(item)
                except TypeError:
                    roomlst1.add(M.adjacent(item))
                    roomlst1.add(item)
            if roomlst1==roomlst:
                finalcomb=comb
                Done=True
            roomlst1=set()

        if roomlst1==roomlst:
            break
    print("TAs needed: ",len(finalcomb))
    print ('TAs assigned to rooms: ',", ".join([str(x) for x in finalcomb] ))#Print without ()
    print("\nAdjacency Matrix")
    print(M)

if __name__ == "__main__":
    main()