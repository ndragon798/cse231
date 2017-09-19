def openfile():
	#fileloc = input("Enter file name: ")
	fileloc=("GDP.txt")
	try:
		fp = open(fileloc)
		return fp
	except FileNotFoundError:
		print("File not found.")
		fp=openfile()
		return fp

def find_min_percent(line):
	i=0
	line=line-1
	while i<int(line):
		linetxt=fpmin.readline()
		i=i+1
	linetxt=fpmin.readline()
	linetxt=linetxt[76:]
	minval=100000000000
	for x in range(0,47):
		#print(x)
		currval=linetxt[:12]
		currval=currval.rstrip()
		currval=currval.lstrip()
		if float(currval)<float(minval):
			minval=currval
			minval_index=(x*12)
			linetxt=linetxt[12:]
		else:
			linetxt=linetxt[12:]
	return(minval,minval_index)

def find_max_percent(line):
	i=0
	line=line-1
	while i<int(line):
		linetxt=fpmax.readline()
		i=i+1
	linetxt=fpmax.readline()
	linetxt=linetxt[76:]
	maxval=0
	for x in range(0,47):
		#print(x)
		currval=linetxt[:12]
		#print(currval,maxval)
		currval=currval.rstrip()
		currval=currval.lstrip()
		try:
			if float(currval)>float(maxval):
				maxval=currval
				maxval_index=(x*12)
				linetxt=linetxt[12:]
			else:
				linetxt=linetxt[12:]
		except ValueError:
			print("Current Val is: ",currval)
			print("Maxval is: ",maxval)
	return(maxval,maxval_index)

def find_gdp(line,index):
	fpgdp=openfile()
	i=0
	line=line-1
	while i<int(line):
		linetxt=fpgdp.readline()
		i=i+1
	linetxt=fpgdp.readline()
	linetxt=linetxt[index:index+12]
	linetxt=linetxt.lstrip()
	linetxt=linetxt.rstrip()
	return (linetxt)
def display(min_val, min_year, min_val_gdp, max_val, max_year, max_val_gdp):
	print("Gross Domestic Product")
	bill_or_millmin="billion"
	bill_or_millmax="billion"
	#print (min_val_gdp)
	#print(max_val_gdp)
	if float(min_val_gdp)>999.9:
		bill_or_millmin="trillion"
		min_val_gdp=float(min_val_gdp)/1000
		min_val_gdp='{:2,.2f}'.format(float(min_val_gdp))
	if float(max_val_gdp)>999.9:
		bill_or_millmax="trillion"
		max_val_gdp=float(max_val_gdp)/1000
		max_val_gdp='{:2,.2f}'.format(float(max_val_gdp))
	print("The minimum change in GDP was ",min_val," percent in",min_year, " when the GDP was ",min_val_gdp," ",bill_or_millmin," dollars.")
	print("The maximum change in GDP was ",max_val," percent in",max_year," when the GDP was ",max_val_gdp," ",bill_or_millmax," dollars.")
#Gross Domestic Product
#The minimum change in GDP was -2.8 percent in 2009 when the GDP was 14.42 trillion dollars.
#The maximum change in GDP was 7.3 percent in 1984 when the GDP was 4.04 trillion dollars.
fpmin=openfile()
fpmax=openfile()


minval,minval_index=find_min_percent(9)
maxval,maxval_index=find_max_percent(9)
gdp_min=find_gdp(44,552)
gdp_max=find_gdp(44,257)
#print (minval,minval_index)
#print(maxval,maxval_index)
#print(gdp_min,gdp_max)
display(minval,2009,gdp_min,maxval,1984,gdp_max)