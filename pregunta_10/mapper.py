#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

if __name__ == "__main__":
    for line in sys.stdin:
        clave, valor = line.split("\t")
        valor = list(valor.strip().split(","))
        clave = clave.zfill(4)
        for letra in valor:
            sys.stdout.write("{}\t{}\n".format(letra, clave))
