def take_first_digit(num: int) -> int:
    digits_list = [str(n) for n in str(num)]
    first_digit = digits_list.pop(0)
    return first_digit