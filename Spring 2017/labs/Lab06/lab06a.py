def openfile():
	fileloc=("data.txt")
	try:
		fp = open(fileloc)
		return fp
	except FileNotFoundError:
		print("File not found.")
		fp=openfile()
		return fp	
fp = openfile()
#fp.next()
avgheight=0
maxheight=0
minheight=1000000
avgweight=0
maxweight=0
minweight=1000000
avgbmi=0
maxbmi=0
minbmi=1000000
people=0
for line in fp:
	try:
		name=line[:12]
		#print(name)
		height=line[12:24]
		#print(height)
		weight=line[24:36]

		#print(weight)
		BMI=float(weight)/float(height)**2

		if float(height)>float(maxheight) or maxheight==None:
			maxheight=float(height)

		elif float(height)<float(minheight) or minheight==None:
			minheight=height

		if float(weight)>float(maxweight) or maxweight==None:
			maxweight=float(weight)

		elif float(weight)<float(minweight) or minweight==None:
			minweight=weight

		if BMI>maxbmi or maxbmi==None:
			maxbmi=BMI

		elif BMI<minbmi or minbmi==None:
			minbmi=BMI
		avgheight+=float(height)
		avgweight+=float(weight)
		avgbmi+=BMI

		print(name+height+weight+"%.2f" % round(BMI,2))
		people+=1
	except Exception as e:
		print(name+height+weight+"BMI")
print('')
print("Average".ljust(12)+str(round((avgheight/people),2)).ljust(12)+str("%.2f"%round((avgweight/people),2)).ljust(12)+str(round((avgbmi/people),2)).ljust(12))
print("Max".ljust(12)+str(maxheight).ljust(12)+str(maxweight).ljust(12)+str(round((maxbmi),2)).ljust(12))
print("Max".ljust(12)+str(minheight).ljust(12)+str(minweight).ljust(12)+str(round((minbmi),2)).ljust(12))