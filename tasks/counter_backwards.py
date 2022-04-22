def count_backwards(start_value: int):
    """
    Counts backwards from provided start_value to 1

    :param start_value: Any non-negative integer value.
    :return:
        “Agile” if the number is divisible by 5,
        “Software” if the number is divisible by 3,
        “Testing” if the number is divisible by both
        or just the number if none of those cases are true.
    """
    if start_value <= 0:
        raise ValueError(f'Can not count backwards from {start_value} to 1')

    for value in range(start_value, 0, -1):
        if not((value % 5) or (value % 3)):
            print("Testing")
            continue
        elif not(value % 5):
            print("Agile")
        elif not(value % 3):
            print("Software")
        else:
            print(value)


def main():
    start = int(input('Please, enter a number: '))
    count_backwards(start)


if __name__ == '__main__':
    try:
        main()
    except ValueError:
        print('Input number should be INTEGER and POSITIVE')
