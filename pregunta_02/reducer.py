#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    
    
    
    curkey = None
    list_values = []
    for line in sys.stdin:
        key, value = line.split("\t")
        value = int(value)
        if key == curkey:
            list_values.append(value)
        elif curkey is None:
            curkey = key
            list_values.append(value)
        else:
            sys.stdout.write("{}\t{}\n".format(curkey,max(list_values)))
            list_values = []
            list_values.append(value)
            curkey = key
    sys.stdout.write("{}\t{}\n".format(curkey,max(list_values)))        