#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys



if __name__ == "__main__":
    campo_lista = []
    for line in sys.stdin:
        marca,date,value = line.split()
        value = int(value)
        campo_lista.append([marca,date,value])

    campo_lista = sorted(campo_lista,key=lambda x:(x[0],x[2]))
    for list_ in campo_lista:
        sys.stdout.write(list_[0] +"   " + list_[1] +"   " + str(list_[2]) + "\n")
    


        
