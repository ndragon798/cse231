import pylab

# Here are some constants that are optional to use -- feel free to modify them, if you wish
REGION_LIST = ['Far_West',
 'Great_Lakes',
 'Mideast',
 'New_England',
 'Plains',
 'Rocky_Mountain',
 'Southeast',
 'Southwest',
 'all']
VALUES_LIST = ['Pop', 'GDP', 'PI', 'Sub', 'CE', 'TPI', 'GDPp', 'PIp']
VALUES_NAMES = ['Population(m)','GDP(b)','Income(b)','Subsidies(m)','Compensation(b)','Taxes(b)','GDP per capita','Income per capita']
PROMPT1 = "Specify a region from this list -- Far_West,Great_Lakes,Mideast,New_England,Plains,Rocky_Mountain,Southeast,Southwest,all: "
PROMPT2 = "Specify x and y values, space separated from Pop, GDP, PI, Sub, CE, TPI, GDPp, PIp: "

def plot_regression(x,y):
    '''Draws a regression line for values in lists x and y.
       x and y must be the same length.'''
    xarr = pylab.array(x) #numpy array
    yarr = pylab.array(y) #numpy arry
    m,b = pylab.polyfit(xarr,yarr, deg = 1) #creates line, only takes numpy arrays
    #as parameters
    pylab.plot(xarr,m*xarr + b, '-') #plotting the regression line
    


def plot(data):   # you need to replace pass with parameters
    '''Plot the values in the parameters.'''
    
    # prompt for which values to plot; these will be the x and y
    plotitem=input(PROMPT2)
    plotitems=plotitem.split()
    plotiteminlist=False
    while plotiteminlist==False:
        for plota in VALUES_LIST:
            if plotitems[0]==plota:
                plotiteminlist=True
                break
        if plotiteminlist==False:
            plotitem=input(PROMPT2)
            plotitems=plotitem.split()
    plotiteminlist=False
    while plotiteminlist==False:
        for plota in VALUES_LIST:
            if plotitems[1]==plota:
                plotiteminlist=True
                break
        if plotiteminlist==False:
            plotitem=input(PROMPT2)
            plotitems=plotitem.split()
    dictkeylist=data.keys()
    dictkeylistA=[]

    for dictkeys in dictkeylist:
        dictkeylistA.append(dictkeys)
    #print(dictkeylist)
    xnum=None
    ynum=None

    for value in range(len(VALUES_LIST)):
        #print(VALUES_LIST[value])
        if VALUES_LIST[value]==plotitems[0]:
            xnum=value
        if VALUES_LIST[value]==plotitems[1]:
            ynum=value
    x=[]
    y=[]
    # build x, the list of x values
    # build y, the list of y values
    xnum+=1
    ynum+=1
    for states in dictkeylist:
        x.append(float(data[states][xnum]))
        y.append(float(data[states][ynum]))
    # hint: list comprehension is a slick way to build x and y
    #print(x,y)
    # In the following you need to replace 'pass' with your own arguments
    pylab.title(VALUES_NAMES[xnum-1]+"vs. "+VALUES_NAMES[ynum-1])   # plot title

    pylab.xlabel(VALUES_NAMES[xnum-1])   #label x axis
    pylab.ylabel(VALUES_NAMES[ynum-1])   #label y axis
    
    pylab.scatter(x,y)
    for i, txt in enumerate(dictkeylist): 
        pylab.annotate(txt, (x[i],y[i]))
    
    plot_regression(x,y)
    
    # USE ONLY ONE OF THESE TWO
    pylab.show()                # displays the plot      
    #pylab.savefig("plot.png")   # saves the plot to file plot.png

def open_file():
    ''' Returns a file pointer '''
    fileloc=input("Filename: ")
    #fileloc='State_Data.csv'
    try:
        fp = open(fileloc)
        return fp
    except FileNotFoundError:
        print("File not found.")
        fp=open_file()
        return fp   

def csv_to_dict(fp):
    region=input(PROMPT1)
    regioninlist=False
    while regioninlist==False:
        for regions in REGION_LIST:
            #print(region,regions)
            if region.lower()==regions.lower():
                regioninlist=True
                break
        if regioninlist==False:
            region=input(PROMPT1)
    fp.readline()
    data=dict()
    for row in fp:
        items=row.split(',')
        if region.lower()==items[1].lower() or region.lower()=='all':
            data[items[0]]=[items[1],items[2],items[3],items[4],items[5],items[6],items[7],float(items[3])/float(items[2]),float(items[4])/float(items[2])]

    #print(data)

    return data,region.lower()
def main():
    data,region=csv_to_dict(open_file())
    if region=='all':
        print("Data for",region)
    else:
        print("Data for the",region)
    dictkeylist=data.keys()
    dictkeylistA=[]
    higdp=None
    higdpstate=None
    lowgdp=None
    lowgdpstate=None
    hiincome=None
    hiincomestate=None
    lowincome=None
    lowincomestate=None
    for dictkeys in dictkeylist:
        dictkeylistA.append(dictkeys)
    for states in dictkeylistA:
        pop=float(data[states][1])
        gdp=float(data[states][2])
        income=float(data[states][3])

        gdpp=gdp/pop
        incomep=income/pop
        if higdp==None or gdpp>higdp:
            higdp=gdpp
            higdpstate=states
        elif lowgdp==None or gdpp<lowgdp:
            lowgdp=gdpp 
            lowgdpstate=states
        if hiincome==None or incomep>hiincome :
            hiincome=incomep
            hiincomestate=states
        elif lowincome==None or incomep<lowincome:
            lowincome=incomep
            lowincomestate=states
    higdp*=1000
    lowgdp*=1000
    lowincome*=1000
    hiincome*=1000
    print(higdpstate,"has the highest GDP per capita at",'${:,.2f}'.format(higdp))
    print(lowgdpstate,"has the lowest GDP per capita at",'${:,.2f}'.format(lowgdp))
    print("")
    print(hiincomestate,"has the highest income per capita at",'${:,.2f}'.format(hiincome))
    print(lowincomestate,"has the lowest income per capita at",'${:,.2f}'.format(lowincome))
    print("")
    print("Data for all states in the",region,":")
    print('{:<15}'.format('State'), '{:>8}'.format('Population(m)'), '{:>8}'.format('GDP(b)'),\
          '{:>8}'.format('Income(b)'), '{:>8}'.format('Subsidies(m)'), '{:>8}'.format('Compensation(b)'),\
          '{:>8}'.format('Taxes(b)'), '{:>8}'.format('GDP per capita'), '{:>8}'.format('Income per capita'))
    for states in sorted(data):
        print('{:<20}'.format(states),\
        '%8.2f'%(float(data[states][1])),\
        '%8.2f'%(float(data[states][2])),\
        '%9.2f'%(float(data[states][3])),\
        '%12.2f'%(float(data[states][4])),\
        '%15.2f'%(float(data[states][5])),\
        '%8.2f'%(float(data[states][6])),\
        '%14.2f'%(float(data[states][7])*1000),\
        '%17.2f'%(float(data[states][8])*1000))
    plot1=input("Would you like to plot the data? Yes/No: ")
    if plot1.upper()=='YES':
        plot(data)

main()