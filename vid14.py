def bubbleSort(elements):
    size = len(elements)

    for i in range(size-1):
        for j in range(size-1-i):
            if elements[j] > elements[j+1]:
                temp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = temp

    return elements

if __name__ == '__main__':
    elements = [5,9,2,1,67,34,88,34]

    elements = bubbleSort(elements)

    print(elements)