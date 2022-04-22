def calculate_factorial(number: int) -> int:
    """
    Calculates a factorial of a specified number.

    :param number: Any non-negative integer value.
    :return: Non-negative integer value.
    """
    if number < 0:
        raise ValueError(f'Can not calculate a factorial for {number}')
    if not number:
        return 1
    if number == 1 or number == 2:
        return number

    result = 1
    for num in range(2, number + 1):
        result *= num
    return result


def main():
    number = int(input('Please, enter a number: '))
    return calculate_factorial(number)


if __name__ == '__main__':
    try:
        print(main())
    except ValueError:
        print('Input number should be INTEGER and NON-NEGATIVE')
