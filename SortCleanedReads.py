from sys import argv
#import sys
#try:
#    os.path.exists(argv[1])
#except:
#    print "could not find file"
    
from Bio import SeqIO

def CreateList(f,R_list,j):
    
    #d = open(str(j),"w+")
    for record in SeqIO.parse(handle, "fastq") :
        #print dir(record)
            #print "1 ",record.id
            #print "2 ",record.seq
            #print "3 ",record.letter_annotations.keys()
            #print "4 ",record.letter_annotations['phred_quality']
            #print record.format("fastq-illumina") ## qualities are wrong
        #d.write(record.format("fastq"))
        R_list.append(record.id)
    
    return R_list

def FilterAll(f,diff_R_sym):
    """ filter the original fastq file with the list of reads
    
    """
    d = open("CommonR1_2","w+")
    for record in SeqIO.parse(handle, "fastq") :
        if record.id not in diff_R_sym:
            d.write(record.format("fastq"))

files = argv[1:]
#R1_dict = []
#R2_dict = {}
R1 = []
R2 = []
R_list =[ R1, R2]
j = 0
for f in files:
    handle = open(f, "rU")
    CreateList(handle,R_list[j],j)
    j += 1
    handle.close()
#print len(R1)
#print len(R2)
#print "DIFF LEN " , len(R1)-len(R2)
### Reads present in R1 but NOT in R2
diff_R1vsR2 = list(set(R1).difference(set(R2)))
#print "diff_R1vsR2" , diff_R1vsR2
#print "##############"
### Reads present in R2 but NOT in R1 
diff_R2vsR1 = list(set(R2).difference(set(R1)))
#print "diff_R2vsR1", diff_R2vsR1
#print len(diff_R1vsR2)
#print len(diff_R2vsR1)
#print diff_R
#print len(diff_R)
diff_R_sym=list(set(R1).symmetric_difference(set(R2)))
#print diff_R_sym
#print len(diff_R_sym)

for f in files:
    handle =open(f,"rU")
    FilterAll(handle,diff_R_sym)
    handle.close()

handle = open(argv[1],"rU")
d = open("OnlyInR1.fastq","w+")
for record in SeqIO.parse(handle, "fastq") :
    if record.id in diff_R1vsR2:
        d.write(record.format("fastq"))
handle.close()

handle = open(argv[2],"rU")
d = open("OnlyInR2.fastq","w+")
for record in SeqIO.parse(handle, "fastq") :
    if record.id in diff_R2vsR1:
        d.write(record.format("fastq"))
handle.close()