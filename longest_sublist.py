def longest_sublist(data):
    longest_lst = []

    for sub in data:
        if len(sub) > len(longest_lst):
            longest_lst = sub

    return longest_lst

data = [[1, 2], [3, 4, 5], [6]]

print(longest_sublist(data))