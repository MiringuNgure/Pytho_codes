import sys

if len(sys.argv) != 3:
    print ("Error in the input and output files")
try:
    ifile = open (sys.argv[1], "r")
except IOError:
    exit("file" + sys.argv[1] + "could not be opened")
try:
    ofile = open (sys.argv[2], "w")
except IOError:
    exit("file" + sys.argv[2] + "could not be opened")

try:
    for line in ifile:
        ofile.write(line)
finally:
    
ifile.close()
ofile.close()