def enumerate_my_iterable(iterable):
    """Returns enumerate iterable"""
    pivot = -1
    for element in iterable:
        pivot += 1
        result = pivot, element
        yield result
