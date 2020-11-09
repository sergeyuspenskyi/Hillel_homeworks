def infinitive_cycle(iterable):
    """Returns the infinitive cycle from an iterable"""
    while True:
        pivot = []
        for element in iterable:
            pivot.append(element)
            yield element
