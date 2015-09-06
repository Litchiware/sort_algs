def my_sort(array):
    """implemention of merge sort algrithm

    :array: TODO
    :returns: TODO

    """
    n = len(array)
    if n == 1:
        return array
    else:
        m = int(n/2)
        a = my_sort(array[0:m])
        b = my_sort(array[m:])
    merged_array = []
    while len(a) != 0 and len(b) != 0:
       if a[0] <= b[0]:
           merged_array.append(a.pop(0))
       else:
           merged_array.append(b.pop(0))
    if len(a) != 0:
        merged_array.extend(a)
    if len(b) != 0:
        merged_array.extend(b)
    return merged_array

a = [4,3,2,1]
print(my_sort(a))
