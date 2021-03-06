def find_min(arr, pointer):
    tmp_min = arr[pointer]
    min_index = pointer
    for i in range(pointer + 1, len(arr)):

        if arr[i] < tmp_min:
            min_index = i
            tmp_min = arr[i]

    return min_index


def selection_sort(arr):
    size = len(arr)
    for j in range(size - 1):  # iterate over the entire array
        # This approach is using my function
        min_index = find_min(arr, j)

        # This approach is without using function
        # min_index = j
        # for i in range(j + 1, size):  # find min index from current position forward
        #     curr = arr[i]
        #     if curr < arr[min_index]:
        #         min_index = i

        if j != min_index:  # Only swap if min index is not already at correct position
            arr[j], arr[min_index] = arr[min_index], arr[j]


def selection_sort_dict(arr, keys=[]):
    size = len(arr)
    # for key in keys:
    for key in keys[::-1]:  # need to do the sorting in reverse order of what we received
    # for key in keys:
        for j in range(size - 1):  # iterate over the entire array
            # This approach is without using function
            min_index = j
            for i in range(j + 1, size):  # find min index from current position forward
                curr = arr[i][key]
                if curr < arr[min_index][key]:
                    min_index = i

            if j != min_index:  # Only swap if min index is not already at correct position
                arr[j], arr[min_index] = arr[min_index], arr[j]


if __name__ == '__main__':
    test = [21, 38, 29, 17, 4, 25, 11, 32, 9]
    print(find_min(test, 0))

    test = [21, 38, 29, 17, 4, 25, 11, 32, 9]
    selection_sort(test)
    print(f'sorted array: {test}')

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
        selection_sort(elements)
        print(f'sorted array: {elements}')

    excercise = [
        {'First Name': 'Raj', 'Last Name': 'Nayyar'},
        {'First Name': 'Suraj', 'Last Name': 'Sharma'},
        {'First Name': 'Karan', 'Last Name': 'Kumar'},
        {'First Name': 'Jade', 'Last Name': 'Canary'},
        {'First Name': 'Raj', 'Last Name': 'Thakur'},
        {'First Name': 'Raj', 'Last Name': 'Sharma'},
        {'First Name': 'Kiran', 'Last Name': 'Kamla'},
        {'First Name': 'Armaan', 'Last Name': 'Kumar'},
        {'First Name': 'Jaya', 'Last Name': 'Sharma'},
        {'First Name': 'Ingrid', 'Last Name': 'Galore'},
        {'First Name': 'Jaya', 'Last Name': 'Seth'},
        {'First Name': 'Armaan', 'Last Name': 'Dadra'},
        {'First Name': 'Ingrid', 'Last Name': 'Maverick'},
        {'First Name': 'Aahana', 'Last Name': 'Arora'}
    ]

    selection_sort_dict(excercise, keys=['First Name', 'Last Name'])
    for item in excercise:
        print(item)
    # print(f'sorted array: {excercise}')
