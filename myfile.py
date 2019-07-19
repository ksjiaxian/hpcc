import random

rlist = []
for i in range(10):
    rlist.append(random.gauss(0,1))

outfile = open('mylist.txt', 'w')
outfile.write(str(rlist))