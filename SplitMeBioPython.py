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
x = math.ceil(i/1000.0)
print "X " , x
#x=1763637.0

#write subset

i = 0
j = 1
target = argv[1]+str(j)
d = open(target,"w+")
source = open(argv[1],"rU")

for record in SeqIO.parse(source, "fastq") :
    if i <= x:
         i += 1
         d.write(record.format("fastq"))
    else:
        d.write(record.format("fastq"))
        i = 0
        j += 1
        target = argv[1]+str(j)
        d =open(target,"w+")