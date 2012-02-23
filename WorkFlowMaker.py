import re
import sys
import os

for dirname, dirnames, filenames in os.walk('/Users/yvans/Home/Dropbox/travail/BRCA12/'):
    for subdirname in dirnames:
        print os.path.join(dirname, subdirname)
    for filename in filenames:
        print os.path.join(dirname, filename)

sys.exit("fini")
file = open("/Users/yvans/Home/Dropbox/travail/BRCA12/WORKFLOWS/WorkFlowGeneral2.sh")
target1="\"whreshould I be\""
target2="\"whreshould I be2\""

while 1:
    line = file.readline()
    if not line:
        break
    if (re.search("export READS1", line)):
        print line.strip()+target1
    elif (re.search("export READS2", line)):
        print line.strip()+target2
    else:
        print line.rstrip()