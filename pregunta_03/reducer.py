#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#

import sys

if __name__ == "__main__":


    for line in sys.stdin:
        key = line.split()[1]
        value = int(line.split()[0])
        sys.stdout.write("{},{}\n".format(key, value))
            

