# You will receive a single integer number between 0 and 100 (inclusive) divisible by 10 without remainder (0, 10, 20, 30...).
# Your task is to create a function that returns a loading bar depending on the number you have received in the input.
# Print the result on the console. For more clarification, see the examples below.
def is_it_100(percents: int) -> bool:
    index = int((str(percents)[:1]))
    dots = '.' * (10 - index)
    percents_print = '%' * index
    is_100 = percents == 100
    if is_100:
        return '100% Complete!' + "\n" + '[%%%%%%%%%%]'
    else:
        return f'{percents}% [{percents_print}{dots}]' + "\n" + 'Still loading...'

user_input = int(input())
result = is_it_100(user_input)
print(result)
