"""Example function for unit tests"""

def sum(xs: list [float]) -> float:
    """return sum off all element in xs"""
    sum_total:float = 0.0
    idx: int=0
    while idx <= len(xs) -1 :
        sum_total += xs[idx]
        idx += 1
    return sum_total

