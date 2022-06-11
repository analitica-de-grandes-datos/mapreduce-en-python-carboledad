#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

#
# Esta funcion reduce los elementos que tienen la misma clave
#
if __name__ == "__main__":

    curkey = None
    v_max = 0

    #
    # cada linea de texto recibida es una entrada clave \tabulador valor
    #
    for line in sys.stdin:

        key, val = line.split("\t")
        val = float(val)

        if key == curkey:
            #
            # No se ha cambiado de clave. Aca se acumulan los valores para la misma
            # clave.
            #
            if val > v_max:
                v_max = val
            if val < v_min:
                v_min = val
        else:
            #
            # Se cambio de clave. Se reinicia el acumulador.
            #
            if curkey is not None:
                #
                # una vez se han reducido todos los elementos
                # con la misma clave se imprime el resultado en
                # el flujo de salida
                #
                sys.stdout.write("{}\t{}\t{}\n".format(curkey, v_max, v_min))

            curkey = key
            v_max = val
            v_min = val

    sys.stdout.write("{}\t{}\t{}\n".format(curkey, v_max, v_min))
