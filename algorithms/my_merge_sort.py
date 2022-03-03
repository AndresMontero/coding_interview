def merge_two_sorted_lists(a, b):
    final_list = []
    j = 0  # this will be the right index
    for i in range(len(a)):
        if a[i] < b[j]:
            final_list.append(a[i])
        else:
            final_list.append(b[j])
            j += 1

    final_list.extend(b[j:])
    return final_list


def merge_sort(elemments):
    pass


if __name__ == '__main__':
    a = [1, 2, 3, 4]
    b = [5, 6, 7, 8]

    print(merge_two_sorted_lists(a,b))

    # tests = [
    #     [11, 9, 29, 7, 2, 15, 28],
    #     [3, 7, 9, 11],
    #     [25, 22, 21, 10],
    #     [29, 15, 28],
    #     [],
    #     [6]
    # ]
    #
    # for elements in tests:
    #     merge_sort(elements)
    #     print(f'sorted array: {elements}')
