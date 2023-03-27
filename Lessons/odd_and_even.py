def odd_and_even (x:list[int]) -> list[int]:
    y:list[int]=[]
    for idx in range(0,len(x),1):
        if idx % 2 ==0 and x[idx] % 2 ==1:
            y.append(x[idx])
    return y