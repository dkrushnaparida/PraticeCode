def count_the_value(mylist):
    count = {}

    for i in mylist:
        if i in count:
            count[i] +=1
        else:
            count[i] =1
        
    return count

print(count_the_value([1,1,1,2,2,1,2,3,2,3]))