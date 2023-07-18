while True:
    value = input("(note: type 'exit' to exit) pyramid's width: ")

    if value == 'exit':
        break

    try:
        width = int(value)
        print("The width is:", width)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

    for row in range(width):
        print(' ' * (width-row), end='')
        row_values = '*' * row
        print(' '.join(row_values))

    for row in range(width, -1, -1):
        print(' '*(width-row), end='')
        row_values = "*" * row
        print(' '.join(row_values))

    stopper = input();