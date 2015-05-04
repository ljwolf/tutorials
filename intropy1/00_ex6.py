f_counties = open('counties.txt')

counties = [] #you'll learn list comprehensions soon
for x in f_counties.readlines():
    counties.append(x.strip('\n').split(','))

#1
cnames = []
for l in counties:
    cnames.append(l[3])

cset = set(cnames)

len(cset)

#2
a1 = time.time()
cdict = dict()
for county in cset:
    cdict.update({county:0})
for county in cnames:
    cdict[county] += 1
a2 = time.time()

#OR

b1= time.time()
cdict = dict()
for county in cnames:
    if county in cdict.keys():
        cdict[county] +=1
    else:
        cdict.update({county:1})
b2 = time.time()

#3 time.time()
a2 - a1 #faster
b1 - b2
