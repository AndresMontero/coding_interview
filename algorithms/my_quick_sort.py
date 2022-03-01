def partition(elements, start, end):
    start_init = start
    pivot = start_init - 1
    pivot_value = elements[pivot]
    while True:
        start_value = elements[start]
        end_value = elements[end]
        if start <= end:
            if start_value > pivot_value:

                if end_value < pivot_value:

                    tmp = elements[start]
                    elements[start] = elements[end]
                    elements[end] = tmp
                else:
                    end -= 1
            elif start == end:
                tmp = elements[start]
                elements[start] = elements[pivot]
                elements[pivot] = tmp
                start = pivot
                break
            else:
                start += 1
        else:
            tmp = elements[end]
            elements[end] = elements[pivot]
            elements[pivot] = tmp
            break
        if start < 0 or end > len(elements) + 1:
            break
    return start, end


def quick_sort(elements, start, end):
    if start < end:
        start_i, end_i = partition(elements, start, end)
        quick_sort(elements, start, end_i - 1)
        quick_sort(elements, start_i + 1, end)

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
        quick_sort(elements, 1, len(elements) - 1)
        print(f'sorted array: {elements}')
