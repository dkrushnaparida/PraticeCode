def find_max_simple(value):
    max_val = float("-inf")
    for val in value:
        for data in val:
            max_val = max(max_val,data)

    return max_val

print(find_max_simple([[7, 2, 9], [4, 11, 3], [8, 5]]))

## with recursive approch
def find_max_recursive(nested_list):
    max_val = float('-inf')
    for item in nested_list:
        if isinstance(item, list):
            val = find_max_recursive(item)
            if val > max_val:
                max_val = val
        else:
            if item > max_val:
                max_val = item
    return max_val

print(find_max_recursive([[7, 2, 9], [4, 11, 3], [8, 5]]))