def item_present_in_list(item, c):
    count = 0
    for i in item:
        for j in i:
            if j == c:
                count +=1

    return count

print(item_present_in_list([[1, 2, 3], [2, 4, 2], [5, 2]], 2))