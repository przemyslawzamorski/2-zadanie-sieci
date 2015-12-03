def quickSort(arr):
    less = []
    pivotList = []
    more = []
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        for i in arr:
            if get_package_number(i) < get_package_number(pivot):
                less.append(i)
            elif get_package_number(i) > get_package_number(pivot):
                more.append(i)
            else:
                pivotList.append(i)
        less = quickSort(less)
        more = quickSort(more)
        return less + pivotList + more


def get_package_number(package):
    binary_number=package[0]
    return int(str(binary_number),2)
