import re
import sys
import os

def writeWorkFlow(R1,R2,target,folder_write_workflow):
    file = open("/Users/yvans/Home/Dropbox/travail/BRCA12/WORKFLOWS/WorkFlowGeneral2.sh")
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
            d.write(line.strip()+"\"@RG\\tID:subset\\tPL:ILLUMINA\\tSM:subset\"\n")
        else:
            d.write(line)

i = 1  

for dirname, dirnames, filenames in os.walk('/Users/yvans/Home/Analysis/BRCA_analysis_01.12.2012/Sample_Diag-HaloBRCA1A-test-1/ReducedDataSet/', topdown=True):
    """for file in filenames:
        if i <5:
            #print "in DIR",dirname
            #print os.path.join(dirname,file)
            print "DIRNAME : ", dirnames
            target =str(os.path.join(dirname,file))
            print "TARGET : ",target
            workflow = str(os.path.join(dirname,"workflow"))
            print "WORKFLOW : ",workflow
            #d = open(workflow,"w+")
            if (re.search("_R1_",file)):
                R = "R1"
                #writeWorkFlow(target,R,d)
            if (re.search("_R2_",file)):
                R = "R2"
                #writeWorkFlow(target,R,d)
            i += 1
        else:
            sys.exit()
        """
    for dir in dirnames:
        #print "DIR : ", dir
        #print "ROOT : ", dirname
        #for fname in os.listdir(os.path.join(dirname,dir)):
            #print "FNAME : ",fname
            #target = str(os.path.join(dirname,dir,fname))
            #print "TARGET : ",target
            #print "LIST : ", type(os.listdir(os.path.join(dirname,dir)))
        (target1,target2) = os.listdir(os.path.join(dirname,dir))
        #print "target =", str(os.path.join(dirname,dir,fname))
        #R1 = target+str(os.listdir(os.path.join(dirname,dir))[0])+"\n"
        R1 = str(os.path.join(dirname,dir,target1))
        #print "R1 : ",os.listdir(os.path.join(dirname,dir))[0]
        print "R1 : ",R1
        #R2 = target+str(os.listdir(os.path.join(dirname,dir))[1])+"\n"
        R2 = str(os.path.join(dirname,dir,target2))
        print "R2 : ", os.listdir(os.path.join(dirname,dir))[1]
        #print "R2 : ", R2
        workflow = str(os.path.join(dirname,dir,"workflow"))
        folder_write_workflow = str(os.path.join(dirname,dir))
        print folder_write_workflow
        #print "WORKFLOW : ",workflow
        d = open(workflow,"a+")
        #d.write(R1)
        #d.write(R2)
        writeWorkFlow(R1,R2,d,folder_write_workflow)
        