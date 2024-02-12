from math import sqrt
from statistics import mean
from random import random
from typing import Callable


def rta(seq_a: str, seq_b: str) -> list[tuple[int, int]]:
    pos_a: int = 0
    pos_b: int = 0
    len_a: int = len(seq_a)
    len_b: int = len(seq_b)
    # The further we are from the diagonal, the more we want to go back to it
    d: Callable[[int, int], float] = lambda x, y: (
        len_a*x + len_b*y)/sqrt(len_a**2 + len_b**2)
    score: int = 0
    while pos_a < len_a-3 and pos_b < len_b-3:
        # Iterating on both pos corresponds to a aligned nucleotide.
        if seq_a[pos_a] == seq_b[pos_b]:
            pos_b += 1
            pos_a += 1
            score += 1
        # We want to see if we can align some behind it, to erase snps
        else:
            # Can we align at least two nucleotides?
            a: bool = seq_a[pos_a+2] == seq_b[pos_b +
                                              1] and seq_a[pos_a+3] == seq_b[pos_b+2]
            b: bool = seq_a[pos_a+1] == seq_b[pos_b +
                                              2] and seq_a[pos_a+2] == seq_b[pos_b+3]
            if a and not b:
                pos_a += 1
            elif b and not a:
                pos_b += 1
            # Choosing between gaps is based upon distance to diagonal
            else:
                pos_a += (
                    x := random()/d(pos_a+1, pos_b)
                    >= random()/d(pos_a, pos_b+1)
                )
                pos_b += not x
    return score
