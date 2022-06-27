#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

for line in sys.stdin:

    letter,date,value = line.split()
    
    sys.stdout.write("{}\t{}\t{}\n".format(value,date,letter))