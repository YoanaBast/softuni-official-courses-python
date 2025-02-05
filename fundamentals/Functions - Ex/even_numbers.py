# Write a program that receives a sequence of numbers (integers) separated by a single space.
# It should print a list of only the even numbers. Use filter()
def only_even(number: int) -> bool:
    return number % 2 == 0


nums = [int(item) for item in input().split()]

result = list(filter(only_even, nums))
print(result)
