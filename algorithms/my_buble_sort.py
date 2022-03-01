### Here you are comparing element and index i with all the rest, not pair comparison
def modified_bubble_sort(elements):
    size = len(elements)
    count = 0
    for i in range(size - 1):
        for j in range(i, size):
            count += 1
            if elements[i] > elements[j]:
                tmp = elements[j]
                elements[j] = elements[i]
                elements[i] = tmp

    print(f"Total number of times modified_bubble_sort: {count}")

    return elements


def bubble_sort(elements, key=None):
    size = len(elements)
    count = 0
    for i in range(size - 1):
        swapped = False
        for j in range(0, size - 1 - i):
            count += 1
            if key is not None:
                if elements[j][key] > elements[j + 1][key]:
                    tmp = elements[j + 1]
                    elements[j + 1] = elements[j]
                    elements[j] = tmp
                    swapped = True
            else:
                if elements[j] > elements[j + 1]:
                    tmp = elements[j + 1]
                    elements[j + 1] = elements[j]
                    elements[j] = tmp
                    swapped = True

        if not swapped:
            break
    print(f"Total number of times bubble sort: {count}")
    return elements


if __name__ == '__main__':
    elements = [
        {'name': 'mona', 'transaction_amount': 1000, 'device': 'iphone-10'},
        {'name': 'dhaval', 'transaction_amount': 400, 'device': 'google pixel'},
        {'name': 'kathy', 'transaction_amount': 200, 'device': 'vivo'},
        {'name': 'aamir', 'transaction_amount': 800, 'device': 'iphone-8'},
    ]
    bubble_sort(elements, key='transaction_amount')
    print(elements)
    bubble_sort(elements, key='name')
    print(elements)

    elements = [5, 9, 2, 1, 67, 34, 88, 34]
    bubble_sort(elements)
    print(elements)
