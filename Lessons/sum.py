"""Example function for unit tests"""

def sum(xs: list [float]) -> float:
    """return sum off all element in xs"""
    sum_total:float = 0.0
    for idx in range(0,len(xs),1):
        sum_total +=xs[idx]
    return sum_total
