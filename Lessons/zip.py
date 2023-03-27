"""Dic Function Writing"""


def zip(x: list [str],y:list[int]) -> dict[str,int]:
    """return a dictionary"""
    if len(x)==0 or len(y)==0 or len(x) != len(y):
        return {}
    newdict: dict[str,int]={x[i]:y[i] for i in range(len(x))}
    return newdict

