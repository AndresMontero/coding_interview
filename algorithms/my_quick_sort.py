
def partition(elements):
    pivot = 0
    start = pivot + 1
    end = len(elements) - 1

    while True:
        if start <= end:
            if elements[start] > elements[pivot]:

                if elements[end] < elements[pivot]:

                    tmp = elements[start]
                    elements[start] = elements[end]
                    elements[end] = tmp
                else:
                    end -= 1

            else:
                start += 1
        else:
            tmp = elements[end]
            elements[end] = elements[pivot]
            elements[pivot] = tmp
            break
    return start, end


def quick_sort(elements):

    start, end = partition(elements)
    print(start, end)

    return elements

if __name__ == '__main__':
    elements = [11, 9, 29, 7, 2, 15, 28]
    quick_sort(elements)
    print(elements)
