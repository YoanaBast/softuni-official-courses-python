# You will receive three integer numbers.
# Write functions named:
# · sum_numbers() that returns the sum of the first two integers
# · subtract() that returns the difference between the returned result of the first function and the third integer
# Wrap the two functions in a function named add_and_subtract() which will receive the three numbers as parameters.
# Print the result of the subtract() function on the console.


def sum_numbers(first: int, second:int) -> int:
    return first + second

def subtract(result: int, third: int) -> int:
    return result - third

def add_and_subtract(first: int, second:int, third: int) -> int:
    result_arg = sum_numbers(a, b)
    return subtract(result_arg, c)

a = int(input())
b = int(input())
c = int(input())

print(add_and_subtract(a, b, c))