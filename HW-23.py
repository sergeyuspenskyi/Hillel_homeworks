def magic_seven(number) -> bool:
    """Checks if digit 7 in number"""
    if str(7) in str(number):
        return True
    return False


list_ = [211, 323, 732, 32, 87, 12, 2, 6, 7, 89]
print({number: magic_seven(number) for number in list_})
