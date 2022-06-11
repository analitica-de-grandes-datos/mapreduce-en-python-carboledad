#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys


if __name__ == "__main__":
    for line in sys.stdin:
        lista = line.split("   ")
        tercera_columna = line.split("   ")[2].strip()
        tercera_columna = tercera_columna.zfill(4)
        sys.stdout.write("{}   {}   {}\n".format(tercera_columna, lista[0], lista[1]))
