def sum_nested_list_loop(data):
    totla = 0

    for val in data:
        for d in val:
            totla +=d

    return totla

print(sum_nested_list_loop([[1, 2], [3, 4], [5, 6]]))