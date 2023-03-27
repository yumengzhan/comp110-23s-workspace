def favorite_color(x: dict[str,str]) -> str:
    """returns the color that appears most frequently."""
    value_list:list[str]=[]
    frequency:dict[str,int]={}
    newfrequency:dict[int,str]={}
    frequency2:dict[int,str] = newfrequency
    val:int=0
    maxnum:int = 0
    numlist:list[int]=[]
    for k in x:
        value = x[k]
        value_list.append(value)
    for item in value_list:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1 
    for key in frequency:
        val = frequency[key]
        newfrequency[val] = key
        numlist.append(frequency[key])
    for idx in range(1,len(numlist),1):
            if value_list[idx]==value_list[idx-1]:
                newfrequency.pop(idx)
                
    for keys in newfrequency:
        if keys > maxnum:
            maxnum=keys   
    return frequency2[maxnum] 