def min_of_three(q,w,e):
    if q < w and q < e:
        return(f"min num is {q}")
    elif w < q and w < e:
       return(f"min num is {w}")
    else:
       return(f"min num is {e}")
print(min_of_three(-1,0,1))