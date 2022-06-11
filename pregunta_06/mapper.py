#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

if __name__ == "__main__":
    for line in sys.stdin:
        # se separan las columnas separadas
        lista = line.split("  ")
        # se genera la salida del dato llamando la columna objetivo
        sys.stdout.write("{}\t{}\n".format(lista[0], float(lista[2])))
