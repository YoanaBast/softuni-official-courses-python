# A perfect number is a positive integer that is equal to the sum of its proper positive divisors.
# That is the sum of its positive divisors, excluding the number itself (also known as its aliquot sum).
#
# Write a function that receives an integer number and returns one of the following messages:
# · "We have a perfect number!" - if the number is perfect.
# · "It's not so perfect." - if the number is NOT perfect.
# Print the result on the console.
def is_it_perfect(number: int) -> bool:
    div_sum = 0
    div_list = []
    for div in range(1, number):
        if number % div == 0:
            div_list.append(div)
            div_sum += div
    is_perfect = div_sum == number
    return is_perfect


num = int(input())

if is_it_perfect(num):
    print('We have a perfect number!')
else:
    print("It's not so perfect.")