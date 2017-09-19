import subprocess
myoutput = open("output.txt","w")
myinput = open("test5.txt",encoding="ascii",errors="surrogateescape")
p1 = subprocess.check_call(['python',"proj10.py"],stdin=myinput,stdout=myoutput)
#myoutput.flush()
myinput.close()
myoutput.close()