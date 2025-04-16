def flatten_recursive(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten_recursive(item))
        else:
            result.append(item)

    return result

# print(flatten_recursive([[1, 2, [3]], [4, [5, 6]]]))
print(flatten_recursive([[1, [2, [3]]]]))