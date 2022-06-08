#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#

def make_counts(acc, nxt):
    acc[nxt] = acc.get(nxt, 0) + 1
    return acc

from functools import reduce
reduce(
    make_counts,
    result,
    {},
)
