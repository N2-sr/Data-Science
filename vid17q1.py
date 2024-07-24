def splitArray(arr):
    size = len(arr)
    mid = size//2
    return [arr[0:mid],arr[mid:size]]

def mergeSortedArraysAscending(arr1, arr2, key):
    p1 = p2 = 0
    l1 = len(arr1)
    l2 = len(arr2)

    res = []
    while p1 < l1 and p2 < l2:
        if arr1[p1][key] <= arr2[p2][key]:
            res.append(arr1[p1])
            p1 += 1
        else:
            res.append(arr2[p2])
            p2 += 1

    while p1 < l1:
        res.append(arr1[p1])
        p1 += 1
    while p2 < l2:
        res.append(arr2[p2])
        p2 += 1

    return res

def mergeSortedArraysDescending(arr1, arr2, key):
    p1 = p2 = 0
    l1 = len(arr1)
    l2 = len(arr2)

    res = []
    while p1 < l1 and p2 < l2:
        if arr1[p1][key] >= arr2[p2][key]:
            res.append(arr1[p1])
            p1 += 1
        else:
            res.append(arr2[p2])
            p2 += 1

    while p1 < l1:
        res.append(arr1[p1])
        p1 += 1
    while p2 < l2:
        res.append(arr2[p2])
        p2 += 1

    return res

def mergeSort(arr, key, descending=False):
    if len(arr) > 1:
        arrs = splitArray(arr)
        arrs[0] = mergeSort(arrs[0],key,descending)
        arrs[1] = mergeSort(arrs[1],key,descending)
        if descending is False:
            arr = mergeSortedArraysAscending(arrs[0],arrs[1],key)
        else:
            arr = mergeSortedArraysDescending(arrs[0],arrs[1],key)
    return arr

if __name__ == '__main__':
    arr1 = [12, 21, 31, 34, 54]
    arr2 = [1, 43, 43, 55, 56]
    arr = [
        { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
        { 'name': 'rajab', 'age': 12,  'time_hours': 3},
        { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
        { 'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
    ]

    print("Original:")
    for i in arr:
        print(i)
        
    print("\nAscending Sort:  ")
    for i in mergeSort(arr,'age'):
        print(i)

    print("\nDescending Sort:  ")
    for i in mergeSort(arr,'age',True):
        print(i)