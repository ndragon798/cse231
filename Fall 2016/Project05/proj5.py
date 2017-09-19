import pylab

def open_file():
	fileloc = input("Enter file name: ")
	try:
		fp = open(fileloc,"r")
		return fp
	except FileNotFoundError:
		print("File not found.")
		fp=open_file()
	return fp

def read_file():
	L=[]
	fp=open_file()
	fp.seek(0)
	for line in fp:
		L.append(line)
		L[-1]=L[-1][26:]
		L[-1]=L[-1].split()
		if L[-1]=="" or L[-1]==None:
			print("None")
	return L

def annual_average(L):
	Ly=[]
	Lm=[]
	Lf=[]
	LyReturn=[]
	LfReturn=[]
	for lines in L:
		Ly.append(float(lines[0]))
		Lm.append(lines[1])
		Lf.append(float(lines[2]))
	while len(Ly)>0:
		LyTmp=Ly[:12]
		LyReturn.append(float(sum(LyTmp))/float(len(LyTmp)))
		Ly=Ly[12:]
	while len(Lf)>0:
		LfTmp=Lf[:12]
		LfReturn.append(float(sum(LfTmp))/float(len(LfTmp)))
		Lf=Lf[12:]
	#print(LyReturn,LfReturn)
	return LyReturn, LfReturn

def month_average(L,M):
	Ly=[]
	Lm=[]
	Lf=[]
	LyReturn=[]
	LfReturn=[]
	for lines in L:
		Ly.append(float(lines[0]))
		Lm.append(lines[1])
		Lf.append(float(lines[2]))
	while len(Ly)>0:
			LyTmp=Ly[:12]
			LyReturn.append(float(sum(LyTmp))/float(len(LyTmp)))
			Ly=Ly[12:]
	while len(Lf)>0:
			LfTmp=Lf[:12]
			LfReturn.append(LfTmp[(int(M)-1)])
			Lf=Lf[12:]
	return LyReturn, LfReturn

def draw_plot( x, y, plt_title, x_label, y_label):
	''' Draw x vs. y (lists should have the same length)
	Sets the title of plot and the labels of x and y axis '''

	pylab.title(plt_title)
	pylab.xlabel(x_label)
	pylab.ylabel(y_label)

	pylab.plot( x, y )
	pylab.show()

def get_month():
	try:
		M = input("Enter a month (1-12): ")
		try:
			if int(M)>12 or int(M)<1:
				print("Number out of range please use number between 1 and 12")
				get_month()
			else:
				return M
		except Exception:
			print("Not a number")
			M=get_month()
			return M
	except Exception:
		print ("Not a number")
		get_month()

L=read_file()
#print(L)
#annual_average(L)
#print(L)
Ly,Lf=annual_average(L)
Lfround=[]
for lines in Lf:
	Lfround.append(round(lines,2))

draw_plot(Ly,Lfround,"Average Yearly Flow","Year","Flow")
h1=0
print("Annual Average Flow")
print("Year     Flow")
for lines in Lfround:
	print (int(Ly[h1]),"	" ,lines)
	h1+=1

M=get_month()
M=int(M)

year_avg,mon_avg=month_average(L,M)
monthlst=["January","February","March","April","May","June","July","August","September","October","November","December"]
title="Average Monthly flow for " + str(monthlst[int(M)-1])

draw_plot(year_avg,mon_avg,title,"Year","Monthly Flow")
h2=0
print(title)
print("Year      Flow")
for lines in year_avg:
	print(int(lines),"     ",float(mon_avg[h2]))
	h2+=1