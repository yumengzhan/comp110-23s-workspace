"""EX07 - dictionary functions."""
__author__ = "730619940"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Invert keys to values."""
    output: dict[str, str] = {}
    value_list: list[chr] = []
    val: str = ""
    for key in input:
        val = input[key]
        output[val] = key
        value_list.append(input[key])
    for idx in range(1, len(value_list), 1):
        if value_list[idx] == value_list[idx - 1]:
            raise KeyError("more than one of the same key")
    return output


def favorite_color(x: dict[str, str]) -> str:
    """Returns the color that appears most frequently."""
    frequency: dict[str, int] = {}
    num: int = 0
    result: str = ""
    for people in x:
        if (x[people] in frequency):
            frequency[x[people]] += 1
        else:
            frequency[x[people]] = 1
    for keys in frequency:
        if frequency[keys] > num:
            num = frequency[keys]
            result = keys
    return result

 
def count(x: list[str]) -> dict[str, int]:
    """Count of the number of times that value appeared in the input list."""
    frequency: dict[str, int] = {}
    for item in x:
        if (item in frequency):
            frequency[item] += 1
        else:
            frequency[item] = 1
    return frequency        