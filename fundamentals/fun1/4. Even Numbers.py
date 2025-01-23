# Write a program that receives a number n on the first line. On the following n lines, it receives different integer numbers.
# If the program receives an odd number, print "{num} is odd!" and end the program.
# Otherwise, if all numbers given are even, print "All numbers are even."

n1 = int(input())
for rotate in range(n1):
    new_int = int(input())
    if new_int % 2 != 0:
        print(f"{new_int} is odd!")
        break
else:
    print("All numbers are even.")

