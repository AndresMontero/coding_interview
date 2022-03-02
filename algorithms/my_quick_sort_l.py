# implementation of quick sort using lomoto partition scheme with first element as pivot

def partition(elements, start, end):
    pivot_value = elements[end]
    p_i = start
    for i in range(start, end):
        if elements[i] <= pivot_value:
            tmp = elements[i]
            elements[i] = elements[p_i]
            elements[p_i] = tmp
            p_i += 1

    tmp = elements[end]
    elements[end] = elements[p_i]
    elements[p_i] = tmp
    return p_i


def quick_sort_l(elements, start, end):
    if len(elements) < 2:
        return
    if start < end and end > 0 and start < len(elements):
        # First find the first partition
        p_i = partition(elements, start, end)
        # Continue sorting left array
        quick_sort_l(elements, start, p_i - 1)
        # Continue sorting right array
        quick_sort_l(elements, p_i + 1, end)

    return elements


if __name__ == '__main__':
    tests = [
        [4, 2, 7, 3, 1, 9, 6, 0, 8],
        [11, 9, 29, 7, 2, 15, 28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]
    elements = [4, 2, 7, 3, 1, 9, 6, 0, 8]

    quick_sort_l(elements, 0, len(elements) - 1)
    print(elements)

    # elements = [25, 22, 21, 10]
    # quick_sort_l(elements, 0, len(elements) - 1)
    # print(elements)
    for elements in tests:
        quick_sort_l(elements, 0, len(elements) - 1)
        print(f'sorted array: {elements}')
