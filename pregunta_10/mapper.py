#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

if __name__ == "__main__":

    for line in sys.stdin:
        value = line.split()[0]
        keys = line.split()[1]
        list_keys = keys.split(",")
        for list_ in list_keys:
            sys.stdout.write("{}\t{}\n".format(list_[0],value))
    