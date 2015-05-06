#1
import pysal
import pandas

path = pysal.examples.get_path('calempdensity.csv')
calemp = pandas.read_csv(path)

print('The extra column gets modified to give it a unique key!')

#2 
counties = pandas.read_csv('counties.txt')

##optional, not using comprehensions

##Note: we iterate though the tuples of state fips and fips in each row.
##then, we right-justify the county code by three. Think of what this means

results = []
for x,y in zip(counties['stfips'], counties['fips']):
    results.append(int(str(x) + str(y).rjust(3, '0'))) 
counties['fullfips'] = pandas.Series(results)

## using comprehensions

r2 = [int(str(x) + str(y).rjust(3,'0')) for x,y in zip(counties['stfips'], counties['fips'])]
counties['ff2'] = pandas.Series(r2)

#3

newframe = pandas.merge(calemp, counties, left_on='Geographic Area.1', right_on='fullfips')

#4

newframe['rv'].hist()

newframe['Number of employees'].hist()

#5 

newframe.plot('rv', 'Number of employees', kind='scatter')
