# needs to create a series of folder before
## for ((i=1;$i<=100;i=$(($i+1)))); do mkdir $i;mv Diag-HaloBRCA1A-test-1_ATCACG_L004_R1_001.pf.fastq$i $i ; mv Diag-HaloBRCA1A-test-1_ATCACG_L004_R2_001.pf.fastq$i $i ;done
## the workflow file should contain the index of the splitted fastq files. and have the correct permission 755
#
import re
import sys
import os

def writeWorkFlow(R1,R2,target,folder_write_workflow,index):
    file = open("/Users/yvans/Home/Dropbox/travail/BRCA12/WORKFLOWS/WorkFlowGeneral.sh")
    while 1:
        line = file.readline()
        #print dirname
        if not line:
            break
        if (re.search("export READS1", line)):
            d.write(line.strip()+R1+"\n")
        elif (re.search("export READS2", line)):
            d.write(line.strip()+R2+"\n")
        elif (re.search("export DIR", line)):
            d.write(line.strip()+folder_write_workflow+"\n")
        elif (re.search("export WORKINGDIR", line)):
            d.write(line.strip()+folder_write_workflow+"/Analysis/\n")
        elif (re.search("export RG", line)):
            d.write(line.strip()+"\"@RG\\tID:subset"+index+"\\tPL:ILLUMINA\\tSM:subset"+index+"\"\n")
        else:
            d.write(line)

i = 1  

for dirname, dirnames, filenames in os.walk('/Users/yvans/Home/Analysis/BRCA_analysis_01.12.2012/Sample_Diag-HaloBRCA1A-test-1/ReducedDataSet/', topdown=True):
    for dir in dirnames:
        (target1,target2) = os.listdir(os.path.join(dirname,dir))
        R1 = str(os.path.join(dirname,dir,target1))
        R2 = str(os.path.join(dirname,dir,target2))
        workflow = str(os.path.join(dirname,dir,"workflow"))
        folder_write_workflow = str(os.path.join(dirname,dir))
        d = open(workflow,"a+")
        os.chmod(str(os.path.join(dirname,dir,"workflow")),"0744")
        writeWorkFlow(R1,R2,d,folder_write_workflow,str(dir))
        