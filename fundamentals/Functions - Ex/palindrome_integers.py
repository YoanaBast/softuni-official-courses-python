# A palindrome is a number that reads the same backward as forward, such as 323 or 1001.
# Write a function that receives a list of positive integers, separated by comma and space ", ".
# The function should check if each integer is a palindrome - True or False. Print the result.

def is_palindrome(number: int) -> bool:
    return str(number) == str(number)[::-1]

nums = [int(item) for item in input().split(", ")]
result = list(map(is_palindrome, nums))
print("\n".join(map(str, result)))
# map to apply to all since it is a list and str to make bool into str

