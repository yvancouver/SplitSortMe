#Yvan Strahm  2011 yvan.strahm@gmail.com

#import os
#import sys
from sys import argv

#index lines in ori
i = 1
#index subdirectory
j = 1

#open file
ori = open(argv[1], "r" )
#open output file
d = open( str(j),"w+")

for line in ori:
    d.write(line)
    i +=1
    if i > 10000000:
        d.close()
        j += 1
        d = open( str(j),"w+")
        i = 1

'''
#from https://biostar.stackexchange.com/questions/671/extracting-a-subset-of-sequences-from-a-fastq-file-biopython-speed

handle = open(output_fn, "w")
for title, seq, qual in FastqGeneralIterator(open(input_fastq_fn)) :
        if title not in corrected_names:
                handle.write("@%s\n%s\n+\n%s\n" % (title, seq, qual))
handle.close()



This is the hard way
try:
    os.path.exists(argv[1])
except:
    print "could not find file"
    
from Bio import SeqIO
handle = open(argv[1], "rU")
i=1
for record in SeqIO.parse(handle, "fastq-illumina") :
    if i < 2:
        #print dir(record)
        print record.id
        print record.seq
        print record.letter_annotations.keys()
        print record.letter_annotations['phred_quality']
        print record.format("fastq-illumina")
        i +=1
    else:
        exit("FINI")
handle.close()

import HTSeq
i=1
for s in HTSeq.FastqReader( "/Users/yvans//Home/PlayData/s_6_1_sequence.txt" ):
    if i < 11:
        print s.name
        print s.qualstr
        i +=1
    else:
        exit("FINI")
'''    