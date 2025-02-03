# Write a function that receives three integer numbers and returns the smallest. Print the result on the console.
# Use an appropriate name for the function.

def smallest(a, b, c):
    list = [a, b, c]
    return min(list)
d = int(input())
f = int(input())
g = int(input())
print(smallest(d, f, g))