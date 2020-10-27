def calculator() -> print:
    """Calculates input formula"""
    print('Welcome to Calculator!'
          '\nProceed with formula input (with spaces), use only "+, -, *, /" as operators, example: "2 * 2"'
          '\nTo exit enter "exit"')

    user_input = str(input('Please enter formula: '))
    if user_input == 'exit':
        exit(0)
    list_input = user_input.split(' ')

    if len(list_input) != 3:
        raise ValueError('Please, put spaces and one operator "+, -, *, /" in formula')
    try:
        number_1 = float(list_input[0])
        operator = list_input[1]
        number_2 = float(list_input[2])
    except ValueError:
        print('Please use numbers/digits in formula and operator')
        raise ValueError
    if not(operator == '+' or operator == '-' or operator == '*' or operator == '/'):
        raise IOError('Please input correct operator with spaces.')
    if operator == '/' and number_2 == 0:
        raise ZeroDivisionError('You cannot divide into zero')

    if operator == '+':
        print(number_1 + number_2)
    if operator == '-':
        print(number_1 - number_2)
    if operator == '*':
        print(number_1 * number_2)
    if operator == '/':
        print(number_1 / number_2)
