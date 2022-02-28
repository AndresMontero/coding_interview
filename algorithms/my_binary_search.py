from util import time_it
import time


@time_it
def linear_search(numbers_list, number_to_find):
    for index, element in enumerate(numbers_list):
        if element == number_to_find:
            return index

    return -1


@time_it
def binary_search(numbers_list, number_to_find):
    left_index = 0
    right_index = len(numbers_list) - 1

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = numbers_list[mid_index]

        if mid_number == number_to_find:
            return mid_index

        if mid_number < number_to_find:

            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

    return -1


@time_it
def binary_search_all_occurrences(numbers_list, number_to_find):
    left_index = 0
    right_index = len(numbers_list) - 1
    answer = []
    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = numbers_list[mid_index]

        if mid_number == number_to_find:
            answer.append(mid_index)

            tmp = mid_index + 1
            while numbers_list[tmp] == mid_number:
                answer.append(tmp)
                tmp += 1

            tmp = mid_index - 1
            while numbers_list[tmp] == mid_number:
                answer.append(tmp)
                tmp -= 1

            return sorted(answer)

        if mid_number < number_to_find:

            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

    return -1


def binary_search_recursive(numbers_list, number_to_find, left_index, right_index):
    if right_index < left_index:
        return -1

    mid_index = (left_index + right_index) // 2
    mid_number = numbers_list[mid_index]

    if mid_index < 0 or mid_index >= len(numbers_list):
        return -1
    if mid_number == number_to_find:
        return mid_index

    if mid_number < number_to_find:
        left_index = mid_index + 1
    else:
        right_index = mid_index - 1

    return binary_search_recursive(numbers_list, number_to_find, left_index, right_index)


def find_all_occurrences(numbers_list, number_to_find):
    initial_index = binary_search_recursive(numbers_list, number_to_find, 0, len(numbers_list) - 1)
    occurrences = [initial_index]

    left_index = initial_index - 1

    while left_index > 0:
        if numbers_list[left_index] == number_to_find:
            occurrences.append(left_index)
        else:
            break
        left_index -= 1

    right_index = initial_index + 1
    while right_index < len(numbers_list) - 1:
        if numbers_list[right_index] == number_to_find:
            occurrences.append(right_index)
        else:
            break

        right_index += 1

    return sorted(occurrences)


if __name__ == '__main__':
    # numbers_list = [12, 15, 17, 19, 21, 24, 45, 67]
    # number_to_find = 19848

    # numbers_list = [i for i in range(500000001)]
    # number_to_find = 500000000

    # numbers_list = [1, 4, 6, 9, 10, 5, 7]
    # number_to_find = 5 This does not work because the list is not sorted

    numbers_list = [1, 4, 6, 9, 11, 15, 15, 15, 17, 21, 34, 34, 56]
    number_to_find = 15

    index = linear_search(numbers_list, number_to_find)
    print(f"The index of the number is {index}")
    index_binary = binary_search(numbers_list, number_to_find)
    print(f"The index of the number is {index_binary}")
    start = time.time()
    index_binary_rec = binary_search_recursive(numbers_list, number_to_find, 0, len(numbers_list) - 1)
    end = time.time()
    print("Binary recursive took " + str((end - start) * 1000) + " mil sec")
    print(f"The index of the number is {index_binary_rec}")

    print(f"All the occurrences are  {find_all_occurrences(numbers_list, number_to_find)}")
    print(f"All the occurrences are  {binary_search_all_occurrences(numbers_list, number_to_find)}")
