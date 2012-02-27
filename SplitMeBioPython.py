#
## ToDo should create a directory where the splitted data should go

from sys import argv
from Bio import SeqIO
import math

for a in argv:
    print a

source = open(argv[1],"rU")
i=0
for record in SeqIO.parse(source, "fastq"):
    i += 1

print "I ", i
x = math.ceil(i/100.0)
print "X " , x
#x=1763637.0

#write subset

i = 0
j = 1
target = argv[1]+"_"+str(j)
d = open(target,"w+")
source = open(argv[1],"rU")

for record in SeqIO.parse(source, "fastq") :
    if i <= x:
        i += 1
        #d.write(str(i))
        d.write(record.format("fastq"))
    else:
        d.write(record.format("fastq"))
        d.write("\n")
        i = 0
        j += 1
        target = argv[1]+"_"+str(j)
        d =open(target,"w+")