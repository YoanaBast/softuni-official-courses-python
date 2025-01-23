thing = input()
fruit = 'banana', 'apple', 'kiwi', 'cherry', 'lemon', 'grapes'
vegetable = 'tomato', 'cucumber', 'pepper', 'carrot'
if thing in fruit:
    print("fruit")
elif thing in vegetable:
    print("vegetable")
else:
    print("unknown")

