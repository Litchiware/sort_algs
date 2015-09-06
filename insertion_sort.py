def sort(array):
    """implemention of insertion sort algrithm

    :array: input array of elements
    :returns: sorted array

    """
    for i in range(1,len(array)):
        insert_value = array[i]
        flag = 0
        for j in range(i):
            if array[i-1-j] <= insert_value:
                array[i-j] = insert_value
                flag = 1
            else:
                array[i-j] = array[i-1-j]
        if flag == 0:
            array[0] = insert_value
    return array

a=[4,3,2,1]
print(sort(a))
