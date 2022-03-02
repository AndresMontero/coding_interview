def insertion_sort(elements):
    for i in range(1, len(elements)):
        anchor = elements[i]
        for j in range(i - 1, -1, -1):
            if anchor < elements[j]:
                elements[j + 1] = elements[j]
                elements[j] = anchor
            else:
                break

    return elements


def running_median(elements):
    if len(elements) < 1:
        print(None)
    if len(elements) < 2:
        print(elements)

    for i in range(1, len(elements)):
        anchor = elements[i]

        if i % 2 == 0:
            a = elements[i // 2]
            b = elements[i // 2 - 1]
            print((a + b) / 2)
        else:
            print(elements[i // 2])

        for j in range(i - 1, -1, -1):
            if anchor < elements[j]:
                elements[j + 1] = elements[j]
                elements[j] = anchor
            else:
                break
    if len(elements) % 2 == 0:
        a = elements[len(elements) // 2]
        b = elements[len(elements) // 2 - 1]
        print((a + b) / 2)
    else:
        print(elements[len(elements) // 2])


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

    running_median([2, 1, 5, 7, 2, 0, 5])
