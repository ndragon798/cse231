def combinedicts(dict1, dict2):
    combdict = dict()
    for key, value in dict1.items():
        if key not in combdict:
            combdict[key] = 0
        combdict[key] += value
    for key, value in dict2.items():
        if key not in combdict:
            combdict[key] = 0
        combdict[key] += value
    return combdict


def printdict(combdict):
    print('{:10}{}'.format('Name', 'Scores'))
    sorteda = sorted(combdict.items())
    for items in sorteda:
        print('{:10}{}'.format(items[0], items[1]))
data1 = open('data1.txt')
data2 = open('data2.txt')
dict1 = dict()
dict2 = dict()
for line in data1:
    if line.split()[0] not in dict1:
        dict1[line.split()[0]] = 0
    try:
        dict1[line.split()[0]] += int(line.split()[1])
    except:
        1+1
try:
    del dict1['Name']
except:
    1+1
for line in data2:
    if line.split()[0] not in dict2:
        dict2[line.split()[0]] = 0
    try:
        dict2[line.split()[0]] += int(line.split()[1])
    except:
        1+1
try:
    del dict2['Name']
except:
    1+1
combdict = combinedicts(dict1, dict2)
printdict(combdict)
