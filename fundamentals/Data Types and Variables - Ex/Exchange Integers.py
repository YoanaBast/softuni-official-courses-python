# 1. Exchange Integers
#
# Read two integer numbers and, after that, exchange their values.
# Print the variable values before and after the exchange, as shown below:

a = int(input())
b = int(input())

new_a = b
new_b = a
print('Before:')
print(f'a = {a}')
print(f'b = {b}')
print('After:')
print(f'a = {new_a}')
print(f'b = {new_b}')