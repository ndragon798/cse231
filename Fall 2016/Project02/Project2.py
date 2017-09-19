def prj2(x):
	total = 0
	eq = ""
	while len(x)>0:
		if len(x)>1:
			eq = eq + x[(len(x)-1)] + "+"
		else:
			eq = eq + x[(len(x)-1)] + "="
		total=total +int(x[(len(x)-1)])
		x=x[0:(len(x)-1)]
	eq = eq + str(total)
	if int(total)>=10:
		print(eq)
		prj2(str(total))
	else:
		print(eq)		

def start():		
	x = input("Please input an integer: ")
	try:
		prj2(x)
	except ValueError:
		print("Error Non-Int Entered\n Try Again")
		start()

start()