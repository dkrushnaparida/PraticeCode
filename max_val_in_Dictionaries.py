def getMaxVlaue(data):
    max_key = None
    max_val = float('-inf')

    for key,value in data.items():
        if value > max_val:
            max_val = value
            max_key = key

    return max_key, max_val

data = {'a': 25, 'b': 30, 'c': 12,'d': 23}
print(getMaxVlaue(data))


