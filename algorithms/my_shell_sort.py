def shell_sort_i(arr):
    size = len(arr)
    gap = size // 2
    while gap > 0:

        for i in range(gap, size):
            anchor = arr[i]
            for j in range(i - gap, -1, -gap):
                if anchor <= arr[j]:
                    arr[j + gap] = arr[j]
                    arr[j] = anchor
                else:
                    break

        gap //= 2

    # when the gap is 1 we do a normal insertion sort
    # for m in range(1, len(arr)):
    #     anchor = arr[m]
    #     for j in range(m-1, -1, -1):
    #         if anchor <= arr[j]:
    #             arr[j + 1] = arr[j]
    #             arr[j] = anchor


def shell_sort_i_no_duplicates(arr):
    size = len(arr)
    gap = size // 2
    items_to_delete = []
    while gap > 0:

        for i in range(gap, size):
            anchor = arr[i]
            for j in range(i - gap, -1, -gap):
                if anchor < arr[j]:
                    arr[j + gap] = arr[j]
                    arr[j] = anchor
                elif anchor == arr[j]:
                    items_to_delete.append(anchor)
                else:
                    break

        items_to_delete = list(set(items_to_delete))
        if items_to_delete:
            for x in items_to_delete:
                arr.remove(x)
        size = len(arr)
        items_to_delete = []
        gap //= 2

    # when the gap is 1 we do a normal insertion sort
    # for m in range(1, len(arr)):
    #     anchor = arr[m]
    #     for j in range(m-1, -1, -1):
    #         if anchor <= arr[j]:
    #             arr[j + 1] = arr[j]
    #             arr[j] = anchor


def shell_sort_t(arr):
    size = len(arr)
    gap = size // 2
    while gap > 0:
        for i in range(gap, size):
            anchor = arr[i]
            j = i
            while j >= gap and arr[j - gap] > anchor:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = anchor
        gap = gap // 2


def shell_sort_b(arr):
    gap = len(arr) // 2
    i = 0
    count = 0
    while gap > 0:

        for k in range(i, len(arr) - gap, gap):
            for j in range(i, len(arr) - gap - i, gap):
                a = arr[j]
                b = arr[j + gap]
                count += 1

                if a > b:
                    tmp = arr[j]
                    arr[j] = arr[j + gap]
                    arr[j + gap] = tmp

        i += 1

        if i + gap > len(arr):
            gap -= 1
            i = 0
    print(count)
    # when the gap is 1 we do a normal insertion sort
    # for m in range(1, len(arr)):
    #     anchor = arr[m]
    #     for j in range(m-1, -1, -1):
    #         if anchor <= arr[j]:
    #             arr[j + 1] = arr[j]
    #             arr[j] = anchor


if __name__ == '__main__':
    # test = [21, 38, 29, 17, 4, 25, 11, 32, 9]
    # shell_sort_b(test)
    # print(f'sorted array: {test}')
    test = [21, 38, 29, 17, 4, 25, 11, 32, 9]
    shell_sort_i(test)
    print(f'sorted array: {test}')
    test = [21, 38, 29, 17, 4, 25, 11, 32, 9]
    # shell_sort_t(test)
    # print(f'sorted array: {test}')

    tests = [
        [21, 38, 29, 17, 4, 25, 11, 32, 9],
        [11, 9, 29, 7, 2, 15, 28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]

    for elements in tests:
        shell_sort_i(elements)
        print(f'sorted array: {elements}')

    excercise = [2, 1, 5, 7, 2, 10, 10, 0, 5, 1, 2, 9, 5, 8, 3, 8]

    shell_sort_i_no_duplicates(excercise)
    print(f'sorted array: {excercise}')
