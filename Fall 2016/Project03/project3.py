def start():
	res = input("Are you a resident?(Yes/No): ")
	level = input("Input level - Freshman, Sophmore, Junior, Senior, Graduate: ")
	cred = input("Input credits this semester: ")
	totalcost=3
	float(totalcost)
	if float(cred)>5:
		totalcost=totalcost+5
	if res.lower() == "yes":
		if 	level.lower() == "freshman" or level.lower()=="sophmore":
			totalcost=totalcost+(468.75*float(cred))+18
			
		elif level.lower() == "junior"	or level.lower()=="senior":
			college=input("College - Business, Engineering, Health, Sciences, None: ")
			totalcost=totalcost+(523.25*float(cred))+18
			if college.lower()=="business":
				if float(cred)>4:
					totalcost=totalcost+218
				else: 
					totalcost=totalcost+109
			elif college.lower()=="engineering" or college.lower()=="sciences":
				if float(cred)>4:
					totalcost=totalcost+645
				else: 
					totalcost=totalcost+387
			elif college.lower()=="health":
				if float(cred)>4:
					totalcost=totalcost+100
				else: 
					totalcost=totalcost+50
		elif level.lower()=="graduate":
			totalcost=totalcost+11+(float(cred)*698)	
			college=input("College - Business, Engineering, Health, Sciences, None: ")
			if college.lower()=="engineering":
				if float(cred)>4:
					totalcost=totalcost+645+75
				else:
					totalcost=totalcost+387+37.50
			else:
				if float(cred)>4:
					totalcost=totalcost+75
				else:
					totalcost=totalcost+37.50
		else:			
			print("Level Not Recognized")
	elif res.lower() == "no":
		if 	level.lower() == "freshman" or level.lower()=="sophmore":
			totalcost=totalcost+(1263.00*float(cred))+18
		elif level.lower() == "junior"	or level.lower()=="senior":
			college=input("College - Business, Engineering, Health, Sciences, None: ")
			totalcost=totalcost+(1302.75*float(cred))+18
			if college.lower()=="business":
				if float(cred)>4:
					totalcost=totalcost+218
				else: 
					totalcost=totalcost+109
			elif college.lower()=="engineering" or college.lower()=="sciences":
				if float(cred)>4:
					totalcost=totalcost+645
				else: 
					totalcost=totalcost+387
			elif college.lower()=="health":
				if float(cred)>4:
					totalcost=totalcost+100
				else: 
					totalcost=totalcost+50
		elif level.lower()=="graduate":	
			totalcost=totalcost+11+(float(cred)*1372.00)	
			college=input("College - Business, Engineering, Health, Sciences, None: ")
			if college.lower()=="engineering":
				if float(cred)>4:
					totalcost=totalcost+645+75
				else:
					totalcost=totalcost+387+37.50
			else:
				if float(cred)>4:
					totalcost=totalcost+75
				else:
					totalcost=totalcost+37.50
		else:
			print("Level Not Recognized")
	else:	
		print("Residency must be yes or no.")	
	print("Total bill: $", '{:2,.2f}'.format(totalcost))
	tryag = input("Do you want to calculate again (Yes/No): ")
	if tryag.lower() ==  "yes":
		try:
			start()
		except Exception as e:
			print(e)

try:
	start()
except Exception as e:
	print(e)
