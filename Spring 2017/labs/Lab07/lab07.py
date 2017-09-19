def openfile():
	fileloc=input("Select a datafile: ")
	try:
		fp = open(fileloc)
		return fp
	except FileNotFoundError:
		print("File not found.")
		fp=openfile()
		return fp	
fp = openfile()
students=[]
for line in fp:
	student=(line[:20].rstrip(),line[20:].split()[0],line[20:].split()[1],(int(line[20:].split()[0])+int(line[20:].split()[1]))/2)
	students.append(student)
students.sort()
ex1=[]
ex2=[]
for person in students:
	print ("{:20}{:4}{:4}{}".format(person[0],person[1],person[2],person[3]))
for person in students:
	ex1.append(int(person[1]))
	ex2.append(int(person[2]))
print("Exam 1 Average:",(sum(ex1)/len(ex1)))
print("Exam 2 Average:",(sum(ex2)/len(ex2)))
