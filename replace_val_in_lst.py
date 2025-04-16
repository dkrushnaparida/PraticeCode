original_val = [2,3,4,5,6,7,4,4,3]

def replace_value(lst, traget, rep):
    for i in range(len(lst)):
        if lst[i] == traget:
            lst[i] = rep

    return lst

print(replace_value([2,3,4,5,6,7,4,4,3], 4, 40))
