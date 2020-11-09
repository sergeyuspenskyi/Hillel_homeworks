from random import randint


def input_list_length() -> int:
    """Returns list length (int) from user input"""
    return int(input('Please input length of list: '))


def random_list_generator(list_length: int) -> list:
    """Returns a random list """
    return [randint(0, 1000) for i in range(list_length)]


def quick_list_sort(unsorted_list: list) -> list:
    """Returns sorted list from unsorted one"""
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


my_list_length = input_list_length()
my_random_list = random_list_generator(my_list_length)
print(quick_list_sort(my_random_list))
