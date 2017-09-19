#####################################
# Computer Project #3
#
#Prompts for a purchase price.
#Prompts for Dollars paid
#Calculates change
#Returns Change
#Go back to step 1
#####################################
try:#Try statement to catch any errors
	print("\nWelcome to change-making program.")
	in_str = input("Enter the purchase price (xx.xx) or `q' to quit: ")
	#Start up all the stocks
	quarter_stock=10
	dimes_stock=10
	nickels_stock=10
	penny_stock=10
	while str(in_str).lower() != 'q':
		#Start up all counters for the change
		quarters=0
		dimes=0
		pennies=0
		nickels=0
		#Gen fullstock
		full_stock=(quarter_stock*25)+(dimes_stock*10)+(nickels_stock*5)+(penny_stock*1)
		in_str=float(in_str)
		#Checks to make sure the price was greater that 0
		if in_str>0:
			#Gets amt paid
			paid= int(input("Input dollars paid (int): "))
			#Makes sure paid is greater than the cost
			if paid > in_str:
				change=int((paid - in_str)*100)
			else:
				print("Error: insufficient payment.")
				paid= int(input("Input dollars paid (int): "))
				change=int((paid-in_str)*100)
			#Do all the logical work of figuring out stock and amt of nickels.
			#If fullstock is more than change then it should work correctly
			if change<full_stock:
				while change > 25 and quarter_stock>0:	
					change=change -25
					quarters=quarters+1
					quarter_stock=quarter_stock-1
				while change > 10 and dimes_stock>0:
					change=change-10
					dimes=dimes+1
					dimes_stock=dimes_stock-1
				while change > 5 and nickels_stock>0:
					change=change-5
					nickels=nickels+1
					nickels_stock=nickels_stock-1
				while change >= 0.001 and penny_stock>0:
					change=change-1
					pennies=pennies+1
					penny_stock=penny_stock-1
				#Print all the stuff generated above
				print("Collect payment below:")
				if quarters>0:
					print("Quarters:", quarters)
				if dimes>0:
					print("Dimes:", dimes)
				if nickels>0:
					print("Nickels:",nickels)
				if pennies>0:
					print("Pennies:", pennies)
				print("Stock:"+str(quarter_stock)+" Quarters, "+str(dimes_stock)+" Dimes, "+str(nickels_stock)+" Nickels, "+str(penny_stock)+" Pennies")
				in_str = input("Enter the purchase price (xx.xx) or `q' to quit: ")
			else:
				#Print for not enough stock error
				print("Error: Not enough stock")
				break
			
		else:
			print("Error: purchase price must be non-negative.")
			in_str = input("Enter the purchase price (xx.xx) or `q' to quit: ")
except Exception as e:
	1+1#Catch just catches all the errors silently so not to disturbe anything.
# Questions
# Q1: 4
# Q2: 1
# Q3: 2
# Q4: 7
# Q5: 1