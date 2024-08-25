def bubble_sort(some_list: list):
    for i in range(len(some_list) - 1):
        for num in range(len(some_list) - 1):
            if some_list[num] > some_list[num + 1]:
                some_list[num], some_list[num + 1] = some_list[num + 1], some_list[num]


bubble_sort([82, 15, 51, 2, 17, 18, 25, 6])


def binary_search(search_element, some_list: list):
    pos = 0
    result_ok = False
    first = 0
    last = len(some_list) - 1

    while first <= last:
        middle = (first + last) // 2
        if some_list[middle] == search_element:
            first = middle
            last = first - 1
            result_ok = True
            pos = middle
        elif some_list[middle] < search_element:
            first = middle + 1
        else:
            last = middle - 1
    if result_ok:
        print(f'{search_element} was found, position {pos}')
    else:
        print(f'{search_element} was not found')


binary_search(23, [2, 4, 7, 11, 15, 18, 21, 23, 35, 43, 56])