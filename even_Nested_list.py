nested_list = [[1, 2, 3, 4], [22, 3, 5, 6], [11, 23, 32]]

even_number = []

for numlist in nested_list:
    for num in numlist:
        if num%2==0:
            even_number.append(num)

# print(even_number)


res = [num for numlist in nested_list for num in numlist if num%2==0]
print(res)