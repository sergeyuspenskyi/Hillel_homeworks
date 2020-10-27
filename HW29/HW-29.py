from main import calculator
while True:
    try:
        calculator()
    except Exception as e:
        print(f'Error: {e}')
        exit(0)
