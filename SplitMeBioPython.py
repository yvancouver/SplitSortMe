from sys import argv
#try:
#    os.path.exists(argv[1])
#except:
#    print "could not find file"
    
from Bio import SeqIO
handle = open(argv[1], "rU")
i=1
for record in SeqIO.parse(handle, "fastq") :
    if i < 101:
        #print dir(record)
        #print "1 ",record.id
        #print "2 ",record.seq
        #print "3 ",record.letter_annotations.keys()
        #print "4 ",record.letter_annotations['phred_quality']
        #print record.format("fastq-illumina") ## qualities are wrong
        print record.format("fastq").rstrip()
        i +=1
    else:
        exit("Voila C'EST FINI")
handle.close()