def text_to_bold_decorator(func):
    def wrapper() -> str:
        """Returns string in bold"""
        return '**' + func() + '**'
    return wrapper


def text_to_italic_decorator(func):
    def inner() -> str:
        """Returns string in italic"""
        return '*' + func() + '*'
    return inner


@text_to_bold_decorator
@text_to_italic_decorator
def display_user_input() -> str:
    """Returns string from user input"""
    result = input('Please input your text: ')
    return result


print(display_user_input())
