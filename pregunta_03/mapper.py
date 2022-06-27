#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    


    for line in sys.stdin:
        key = line.split(',')[0]
        value = int(line.split(',')[1])
        sys.stdout.write("{}\t{}\n".format(value,key))