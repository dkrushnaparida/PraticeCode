def pair_of_sum(lst, k):
    result = []
    data = set()

    for i in range(len(lst)):
        if i in data:
            continue

        for j in range(i+1, len(lst)):
            if j in data:
                continue

            if lst[i] + lst[j]==k:
                result.append((lst[i],lst[j]))
                data.add(i)
                data.add(j)

    return result

lst = [1,2,3,4,5,6]
k = 7
print(pair_of_sum(lst,k))