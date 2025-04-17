def merge_list(l1,l2):
    merging = []

    for i in range(min(len(l1),len(l2))):
        merging.append(l1[i])
        merging.append(l2[i])

    return merging

l1 = [1,2]
l2 = ['a','b']
print(merge_list(l1,l2))