def quick_list_sort(unsorted_list: list) -> list:
    """Returns sorted list"""
    if len(unsorted_list) < 2:
        return unsorted_list
    pivot = unsorted_list[0]
    after_pivot = []
    before_pivot = []
    for i in unsorted_list[1:]:
        if i >= pivot:
            after_pivot.append(i)
        else:
            before_pivot.append(i)
    return quick_list_sort(before_pivot) + [pivot] + quick_list_sort(after_pivot)


def int_to_list_converter() -> list:
    """Returns a random list with the length you enter"""
    from random import randint
    my_list_length = int(input('Please input length of list: '))
    return [randint(0, 1000) for i in range(my_list_length)]


print(quick_list_sort(int_to_list_converter()))
