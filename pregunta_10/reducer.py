#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    
    
    
    curkey = None
    list_values = []
    for line in sys.stdin:
        key, value = line.split()
        value = int(value)
        if key == curkey:
            list_values.append(value)
        elif curkey is None:
            curkey = key
            list_values.append(value)
        else:
            list_values_sorted = sorted(list_values)
            list_vales_tostr = list(map(lambda element:str(element),list_values_sorted))         
            sys.stdout.write("{}\t{}\n".format(curkey,",".join(list_vales_tostr)))
            list_values = []
            list_values.append(value)
            curkey = key 
    list_values_sorted = sorted(list_values)
    list_vales_tostr = list(map(lambda element:str(element),list_values_sorted))         
    sys.stdout.write("{}\t{}\n".format(curkey,",".join(list_vales_tostr)))    
