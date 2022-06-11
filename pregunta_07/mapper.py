#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys


if __name__ == "__main__":
    for line in sys.stdin:
        tercera_columna = line.split("   ")[2].strip()
        tercera_columna = tercera_columna.zfill(4)
        sys.stdout.write(
            "{} {} {}\n".format(
                str(line.split("   ")[0]), tercera_columna, line.split("   ")[1]
            )
        )
