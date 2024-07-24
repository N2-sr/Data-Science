def insertionSort(elements):
    ptr = 1
    size = len(elements)
    while ptr < size:
        key = elements[ptr]
        i = ptr-1
        while i >= 0 and key < elements[i]:
            elements[i+1] = elements[i]
            i -= 1
        elements[i+1] = key
        ptr += 1

    return elements

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
        insertionSort(elements)
        print(f'sorted array: {elements}') 