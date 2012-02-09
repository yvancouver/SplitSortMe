from sys import argv
from Bio import SeqIO
import math

for a in argv:
    print a

source = open(argv[1],"rU")
i=0
for record in SeqIO.parse(d, "fastq"):
    i += 1

print "I ", i
x = math.ceil(i/10.0)
print "X " , x

#write subset

target = []
#not finisehd
d = open(target,"w+")
for record in SeqIO.parse(source, "fastq") :
    d.write(record.format("fastq"))