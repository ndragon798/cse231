import zipfile
import string
import time
from itertools import product


def open_dict_file():
    """Opens dictionary file"""
    fileloc = input("Enter dictionary file name: ")
    try:
        #try and open the file
        fp = open(fileloc)
        return fp
    except FileNotFoundError:
        print("File not found.")
        #recursively try and open the file if it cant find it
        fp = open_dict_file()
        return fp


def open_zip_file():
    """Opens zip file"""
    filename = input("Enter zip file name: ")
    try:
        #try and open the zip file
        zip_file = zipfile.ZipFile(filename)
        return zip_file
    except Exception as e:
        print("File not found or not a zip file.")
        #recursibely try and open the file if it  cant find it
        zip_file = open_zip_file()
        return zip_file


def brute_force_attack(zip_file):
    """Uses a brute force attack on given zip file"""
    #loop through all iterations of the alphabet at length of 3
    for length in range(1,9):    
        for items in product('abcdefghijklmnopqrstuvwxyz', repeat=length):
            password = (''.join(items))
            #try and use password to extractall password
            try:
                zip_file.extractall(pwd=password.encode())
                print("Brute force password is "+password)
                return True
            except Exception as e:
                1+1
    return False


def dictionary_attack(zip_file, dict_file):
    """Uses a dictionary attack on a given zip file and dictionary file"""
    #loop through and test every line on the zip file
    for line in dict_file:
        password = line.strip()#strip the line
        try:
            zip_file.extractall(pwd=password.encode())
            print("Dictionary password is "+password)
            dict_file.close()
            return True#return true if cracked
            break
        except Exception as e:
            1+1
    return False


def main():
    print("Cracking zip files.")
    #warn the users
    print(
        "Warning cracking passwords is illegal due to Computer Fraud and Abuse Act (CFAA) and has a max prison term of 1 year.")
    userinput = input(
        "What type of cracking ('brute force','dictionary','both','q'): ")
    while userinput != 'q':#while loop for asking cracking type
        if userinput == 'brute force':
            print("Brute Force Cracking\n")
            zip_file = open_zip_file()
            start = time.process_time()#start time
            found = brute_force_attack(zip_file)#brute force
            end = time.process_time()#stop time
            if found == False:
                print("No password found.")
            print("Elapsed time (sec): " + str(round((end-start), 4)))#return elapsed time
            userinput = input(
                "What type of cracking ('brute force','dictionary','both','q'): ")
        elif userinput == 'dictionary':
            print("Dictionary Cracking\n")
            dict_file = open_dict_file()#open dict file
            zip_file = open_zip_file()#open zip
            start = time.process_time()#start time
            found = dictionary_attack(zip_file, dict_file)
            end = time.process_time()#stop time
            if found == False:
                print("No password found.")
            print("Elapsed time (sec): " + str(round((end-start), 4)))
            userinput = input(
                "What type of cracking ('brute force','dictionary','both','q'): ")
        elif userinput == 'both':#do both
            print("Both Brute Force and Dictionary Attack\n")
            dict_file = open_dict_file()
            zip_file = open_zip_file()
            start = time.process_time()
            found = dictionary_attack(zip_file, dict_file)
            end = time.process_time()
            if found == False:
                print("No password found.\n")
            print("Elapsed time (sec): " + str(round((end-start), 4)))
            if found == False:
                start = time.process_time()
                found = brute_force_attack(zip_file)
                end = time.process_time()
                if found == False:
                    print("No password found.\n")
                print("Elapsed time (sec): " + str(round((end-start), 4)))
            userinput = input(
                "What type of cracking ('brute force','dictionary','both','q'): ")
        else:#if the inputs isn't any good ones then ask again
            userinput = input(
                "What type of cracking ('brute force','dictionary','both','q'): ")


if __name__ == "__main__":
    main()
