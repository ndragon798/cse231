import subprocess
n = input("Enter a single-digit test number: ")
myoutput = open("output"+n+".txt","w")
myinput = open("test"+n+".txt",encoding="ascii",errors="surrogateescape")
p1 = subprocess.check_call(['python',"proj09.py"],stdin=myinput,stdout=myoutput)
#myoutput.flush()
myinput.close()
myoutput.close()
