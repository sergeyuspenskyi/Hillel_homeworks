def square_definer(width: int, length: int) -> int:
    """Returns the size of the smallest square side possible in area"""
    while width != length:
        if width > length:
            width -= length
            return square_definer(width, length)
        elif length > width:
            length -= width
            return square_definer(width, length)
    return width


your_width = int(input('Put a width: '))
your_length = int(input('Put a length: '))
print(square_definer(your_width, your_length))
