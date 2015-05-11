import pysal as ps
fp = pysal.open(pysal.examples.get_path('calempdensity.csv'))
header = fp.header
data = fp.read()

d = {}

for record in data:
    d.update({record[0]:{}})
    for idx, field in enumerate(header):
        d[record[0]].update({field:record[idx]})
