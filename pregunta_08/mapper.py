#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#

import sys

if __name__ == "__main__":
    for line in sys.stdin:
        key = line.split()[0]
        value = line.split()[2]
        sys.stdout.write("{}\t{}\n".format(key,value))
        