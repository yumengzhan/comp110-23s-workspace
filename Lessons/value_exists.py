def value_exists(test_dict:dict[str,int],test_val:int)->bool:
    for characters in test_dict:
        if test_dict[characters] == test_val:
            return True   
    return False