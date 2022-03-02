def insertion_sort(elements):
    for i in range(1, len(elements)):
        anchor = elements[i]
        for j in range(i-1, -1, -1):
            if anchor < elements[j]:
                elements[j+1] = elements[j]
                elements[j] = anchor
            else:
                break


    return elements


if __name__ == '__main__':
    tests = [
        [11, 9, 29, 7, 2, 15, 28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]

    for elements in tests:
        insertion_sort(elements)
        print(f'sorted array: {elements}')
