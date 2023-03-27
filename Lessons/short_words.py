def short_words(my_list:list[str]) ->list[str]:
    for idx in range(0,len(my_list)-1,1):
        if len(my_list[idx])>5:
            print(f"{my_list[idx]}is too long!")
            my_list.pop(idx)
    return(my_list)