# Write a function that receives two integer numbers. Calculate the factorial of each number.
#
# Divide the first result by the second and print the division formatted to the second decimal point.
def my_function(first_num: int, second_num: int) -> float:
    for div in range(first_num - 1, 0, -1):
        first_num *= div

    for div in range(second_num  - 1, 0, -1):
        second_num  *= div

    return f'{float(first_num / second_num):.2f}'

input_one = int(input())
input_two = int(input())

result = my_function(input_one, input_two)
print(result)
