def quick_sort(arr):
    if len(arr) <= 1:
        return arr[:]

    pivot = arr[0]

    less = []
    equal = []
    greater = []

    for num in arr:
        if num < pivot:
            less.append(num)
        elif num > pivot:
            greater.append(num)
        else:
            equal.append(num)

    return quick_sort(less) + equal + quick_sort(greater)
