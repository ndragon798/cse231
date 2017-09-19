def open_file():
    ''' Returns a file pointer '''
    fileloc=input("Filename: ")
    while True:
        try:
            fp = open(fileloc)
            return fp
        except FileNotFoundError:
            print("File not found.")
            fileloc=input("Filename: ")

def read_data(fp):
    ''' Reads through the file and returns a dicitonary '''
    Data_dict=dict()
    linecount=0
    for line in fp:
        linecount+=1
        #Below replaces all the stuff
        line=line.replace(',','')
        line=line.replace('.','')
        line=line.replace('!','')
        line=line.replace('-','')
        line=line.replace("'",'')
        line=line.split()#splits into an list of words
        for word in line:
            if len(word)>=2:
                try:
                    Data_dict[word.lower()].add(linecount)#adds the number to a list
                except:
                    Data_dict[word.lower()]=set()#creats the set
                    Data_dict[word.lower()].add(linecount)
    return Data_dict

def find_cooccurance(D, inp_str):
    ''' Takes in a dictionary and a string '''
    numset=set()
    old_inp_str=inp_str
    old_inp_str=old_inp_str.replace(" ",", ")
    #replaces the old str spaces with commas and a space
    inp_str=inp_str.split()
    #splits it into list
    for item in inp_str:
        if item in D:
            if len(numset)>0:
                numset=numset.intersection(D[item])#if they intersect then add it to the set
            else:
                numset=D[item]#creates the set
    print("The co-occurance for:",old_inp_str)
    linestr=''
    for num in numset:
        linestr+=str(num)+", "
    print(linestr[:-2])
    return numset

def main():
    D=read_data(open_file())#open file then read the file
    usrinput=input("Enter space-seperated words: ")
    while usrinput.lower() != 'q':
        find_cooccurance(D,usrinput)
        usrinput=input("Enter space-seperated words: ")


if __name__ == "__main__":
    main()