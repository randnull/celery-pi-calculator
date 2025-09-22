import math

from typing import Callable
from decimal import Decimal, getcontext


def sign(i):
    if i % 2 == 0:
        return 1
    return -1


def get_pi(n: int, update_trigger: Callable) -> str:
    getcontext().prec = n + 10

    A = Decimal(1)
    b_cur = Decimal(1) / (Decimal(2).sqrt())
    t = Decimal("0.25")
    ppp = Decimal(1)
    iter_limit = int(math.log2(n + 5)) + 5
    tol = Decimal(10) ** (-(n + 1))

    for k in range(iter_limit):
        mid_val = (A + b_cur) / Decimal(2)
        b_new = (A * b_cur).sqrt()
        d = A - mid_val

        t = t - ppp * (d * d)
        ppp = ppp * Decimal(2)
        A = mid_val
        b_cur = b_new

        update_trigger(float((k + 1) / iter_limit))

        if abs(A - b_cur) < tol:
            break

    pi_val = ((A + b_cur) * (A + b_cur)) / (Decimal(4) * t)
    return f"{pi_val:.{n}f}"
