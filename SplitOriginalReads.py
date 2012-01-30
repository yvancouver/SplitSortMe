""" please read http://docs.python.org/library/argparse.html#module-argparse"""

import sys,io
from time import gmtime, strftime,localtime
import argparse
import doctest
from sys import argv
import textwrap

helpstr = '''SplitOriginalReads is use to split a fastq file into smaller files
This was made in order to analyse the first HTS pilot experiment we had at Ulleval.

Author: Yvan Strahm (yvan.strahm@gmail.com)
License: GPL 3.0 (http://www.gnu.org/licenses/gpl-3.0.txt)'''
#parser = ArgumentParser(description="SplitOriginalReads is use to split a fastq file into smaller files.\nThis was made in order to analyse the first HTS pilot experiment we had at Ulleval",
#                        epilog="Author: Yvan Strahm (yvan.strahm@gmail.com) License: GPL 3.0 (http://www.gnu.org/licenses/gpl-3.0.txt)")
parser = argparse.ArgumentParser(prog='SplitOriginalReads',
                        formatter_class=argparse.RawDescriptionHelpFormatter,
                        description=textwrap.dedent('''\
                            SplitOriginalReads is use to split a fastq file into smaller files.
                            This was made in order to analyse the first HTS pilot experiment we had at Ulleval
                                Author: Yvan Strahm (yvan.strahm@gmail.com)
                                License: GPL 3.0 (http://www.gnu.org/licenses/gpl-3.0.txt
                            '''))

parser.add_argument('-f', metavar='F', type=str, dest='files', action='append',
                   help='list of files')

parser.add_argument('-n', type=int,
                   help='number of reads to be present into the splitted files')
print parser.parse_args()
args = parser.parse_args()
print args.files
print type(args.n)
i = 1
for f in args.files:
    while i <= args.n:
        print i,f
        i += 1
    else: i = 1
'''
(opts,args) = parser.parse_args()
print "opts" , opts
#print "args", args

if opts.files == None:
    errmsg = "You should provide a valid fastq file"
    errmsg += " Please see the help with -h or --help"
    parser.error(errmsg)
elif opts.number == None:
    errmsg = "You should provide a number of reads per subfile"
    errmsg += " Please see the help with -h or --help"
    parser.error(errmsg)

#check if files exist
files = opts.files.split(",")
print files
for f in files:
    try:
        io.open(opts.files,'r')
    except:
        errmsg = "You should provide a valid fastq file"
        errmsg += " Please see the help with -h or --help"
        parser.error(errmsg)
'''