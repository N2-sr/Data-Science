def partition(list,start,end):
    pivot = start

    while start < end:
        while list[start] < list[pivot]:
            start += 1
        while list[end] > list[pivot]:
            end -= 1

        if start < end:
            list[start], list[end] = list[end], list[start]
    list[end], list[pivot] = list[pivot], list[end]

    return end

def quicksort(list,start,end):
    if start < end:
        p = partition(list,start,end)
        quicksort(list,start,p-1)
        quicksort(list,p+1,end)


if __name__ == '__main__':
    test = [
        [11,9,29,7,2,15,28],
        [3,7,9,11],
        [25,22,21,10],
        [29,15,28],
        [],
        [6]
    ]

    for elements in test:
        quicksort(elements,0,len(elements)-1)
        print(f'sorted array: {elements}')
