# Write a program that rounds all the given numbers, separated by a single space, and prints the result as a list.
# Use round()
# i know round is already a fuction, but i wanted to define one for ex
def round_me(x):
    return round(x)

list1 = [float(z) for z in input().split()]
list2 = []
for y in list1:
    result = round_me(y)
    list2.append(result)

print(list2)

#here is a shorter solution:
list3 = [round(float(z)) for z in input().split()]
print(list3)