def squares(inital,terms):
	total=0
	for i in range(inital,terms+inital):
		total=(i**2)+total
	return total
def cubes(inital,terms):
	total=0
	for i in range(inital,terms+inital):
		total=(i**3)+total
	return total
def power(inital,terms,exponent):
	total=0
	for i in range(inital,terms+inital):
		total=(i**exponent)+total
	return total
def takein():
	command = input("Please Enter a command: ")
	if command =="cubes":
		inital=int(input("Please enter inital number: "))
		terms=int(input("Please enter the number of terms in the series: "))
		cubed=cubes(inital,terms)
		print(cubed)
		takein()
	elif command =="squares":
		inital=int(input("Please enter inital number: "))
		terms=int(input("Please enter the number of terms in the series: "))
		squared=squares(inital,terms)
		print(squared)
		takein()
	elif command =="power":
		inital=int(input("Please enter inital number: "))
		terms=int(input("Please enter the number of terms in the series: "))
		exponent=int(input("Please enter the exponent: "))
		powered=power(inital,terms,exponent)
		print(powered)
		takein()
	elif command =="exit":
		1+1
	else:
		print("***Invalid choice***")
		command=takein()
takein()