def remove_duplicate(data):
    result = []

    for val in data:
        if val not in result:
            result.append(val)

    return result

nested_list = [[1, 2], [3, 4], [1, 2, 3], [5], [3, 4]]
print(remove_duplicate(nested_list))