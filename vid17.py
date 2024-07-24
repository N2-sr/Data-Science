def splitArray(arr):
    size = len(arr)
    mid = size//2
    return [arr[0:mid],arr[mid:size]]

def mergeSortedArrays(arr1, arr2):
    p1 = p2 = 0
    l1 = len(arr1)
    l2 = len(arr2)

    res = []
    while p1 < l1 and p2 < l2:
        if arr1[p1] <= arr2[p2]:
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

def mergeSort(arr):
    if len(arr) > 1:
        arrs = splitArray(arr)
        arrs[0] = mergeSort(arrs[0])
        arrs[1] = mergeSort(arrs[1])
        arr = mergeSortedArrays(arrs[0],arrs[1])
    return arr

if __name__ == '__main__':
    arr1 = [21,34,54,12,31]
    arr2 = [43,43,55,56,1]
    arr = arr1 + arr2

    print("Original:",arr)
    print("Sorted:  ",mergeSort(arr))
