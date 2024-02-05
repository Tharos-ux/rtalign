from math import sqrt
from statistics import mean
from random import random
from typing import Callable


def rta(seq_a: str, seq_b: str) -> int:
    pos_a: int = 0
    pos_b: int = 0
    len_a: int = len(seq_a)
    len_b: int = len(seq_b)
    d: Callable[[int, int], float] = lambda x, y: abs(
        len_a*x + len_b*y)/sqrt(len_a**2 + len_b**2)
    score: int = 0

    # Iterating on both pos corresponds to a aligned nucleotide.
    # Choosing between substitution and gap is based upon distance to diagonal
    while pos_a < len_a and pos_b < len_b:
        if seq_a[pos_a] == seq_b[pos_b]:
            pos_a += 1
            pos_b += 1
            score += 1
        else:
            d_a: float = d(pos_a+1, pos_b) * random()
            d_b: float = d(pos_a, pos_b+1) * random()

            pos_a += (x := d_a < d_b)
            pos_b += not x

    return score


print(
    mean(
        [
            rta('TTTTTTTTATTTTCCCACTACCAGC', 'TTTTTTTTATTTTCCCCTACCAGC') for _ in range(1000000)
        ]
    )
)
