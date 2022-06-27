#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == "__main__":
    list_of_list = []
    for line in sys.stdin:
        value,date,letter = line.split()
        value = int(value)
        list_of_list.append([value,date,letter])
    list_of_list = sorted(list_of_list,key=lambda x:x[0],reverse=False)
    i = 0
    for list in list_of_list:
        i += 1
        if i > 6:
            break
        else: 
            sys.stdout.write(list[2] + "   " + list[1] + "   " + str(list[0]) + "\n")


