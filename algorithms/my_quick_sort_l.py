# implementation of quick sort using lomoto partition scheme with first element as pivot

def partition(elements, start, end):
    pivot_value = elements[end]
    p_i = start

    while True:
        p_i_value = elements[p_i]
        if p_i_value < pivot_value:
            p_i += 1

        else:
            i = p_i + 1
            i_value = elements[i]
            if i_value < pivot_value:
                tmp = elements[i]
                elements[i] = elements[p_i]
                elements[p_i] = tmp
                p_i += 1
                i += 1
                # break
            else:
                i += 1
        if p_i == end - 1:
            tmp = elements[end]
            elements[end] = elements[p_i]
            elements[p_i] = tmp
            break
    print(p_i)
    return p_i


def quick_sort_l(elements, start, end):
    if start < end:
        # First find the first partition
        start_i, end_i = partition(elements, start, end)
        # Continue sorting left array
        quick_sort_l(elements, start, end_i - 1)
        # Continue sorting right array
        quick_sort_l(elements, start_i + 1, end)

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
    elements = [11, 9, 29, 7, 2, 15, 28]
    partition(elements, 0, len(elements) - 1)
    print(elements)
    # for elements in tests:
    #     partition(elements, 0, len(elements) - 1)
    #     print(f'sorted array: {elements}')
