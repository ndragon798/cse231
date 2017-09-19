def openfile():
	fileloc=("dictionary.txt")
	try:
		fp = open(fileloc)
		return fp
	except FileNotFoundError:
		print("File not found.")
		fp=openfile()
		return fp
fp=openfile()
for word in fp:
	if word.replace('a','',1).find('a') == -1:
		a=word.find('a')
		if word.replace('e','',1).find('e') == -1:
			e=word.find('e')
			if word.replace('i','',1).find('i') == -1:
				i=word.find('i')
				if word.replace('o','',1).find('o') == -1:
					o=word.find('o')
					if word.replace('u','',1).find('u') == -1:
						u=word.find('u')
						if a != -1 and e !=-1 and i !=-1 and o !=-1 and u !=-1:
							if a < e and e<i and i<o and o<u:
								print (word)