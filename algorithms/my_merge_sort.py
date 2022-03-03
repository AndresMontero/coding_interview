def merge_two_sorted_lists(a, b, arr):
    i = 0  # this will be the left index
    j = 0  # this will be the right index
    k = 0  # this for the final sorted array
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            arr[k] = a[i]
            i += 1
        else:
            arr[k] = b[j]
            j += 1
        k += 1
    while i < len(a):
        arr[k] = a[i]
        i += 1
        k += 1
    while j < len(b):
        arr[k] = b[j]
        j += 1
        k += 1


def merge_sort(arr):
    if len(arr) <= 1:
        return
    mid = len(arr) // 2

    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    merge_two_sorted_lists(left, right, arr)

def merge_two_sorted_lists_athletes(a, b, arr, key = None, descending = False):
    i = 0  # this will be the left index
    j = 0  # this will be the right index
    k = 0  # this for the final sorted array
    while i < len(a) and j < len(b):
        if descending:
            if a[i][key] > b[j][key]:
                arr[k] = a[i]
                i += 1
            else:
                arr[k] = b[j]
                j += 1
        else:
            if a[i][key] > b[j][key]:
                arr[k] = a[i]
                i += 1
            else:
                arr[k] = b[j]
                j += 1
        k += 1
    while i < len(a):
        arr[k] = a[i]
        i += 1
        k += 1
    while j < len(b):
        arr[k] = b[j]
        j += 1
        k += 1


def merge_sort_athletes(arr, key=None, descending=None):
    if len(arr) <= 1:
        return
    mid = len(arr) // 2

    left = arr[:mid]
    right = arr[mid:]

    merge_sort_athletes(left, key, descending)
    merge_sort_athletes(right, key, descending)

    merge_two_sorted_lists_athletes(left, right, arr, key, descending)


if __name__ == '__main__':
    a = [1, 2, 3]
    b = [8, 9, 10, 11, 12, 13, 14]

    a = [7]
    b = [2]
    arr = [7, 2]
    merge_two_sorted_lists(a, b, arr)
    print(arr)

    tests = [
        [11, 9, 29, 7, 2, 15, 28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]

    for elements in tests:
        merge_sort(elements)
        print(f'sorted array: {elements}')

    athletes = [
        {'name': 'vedanth', 'age': 17, 'time_hours': 1},
        {'name': 'rajab', 'age': 12, 'time_hours': 3},
        {'name': 'vignesh', 'age': 21, 'time_hours': 2.5},
        {'name': 'chinmay', 'age': 24, 'time_hours': 1.5},
    ]

    merge_sort_athletes(athletes, key='time_hours', descending=True)
    print(athletes)

    merge_sort_athletes(athletes, key='time_hours', descending=False)
    print(athletes)

    merge_sort_athletes(athletes, key='name', descending=False)
    print(athletes)