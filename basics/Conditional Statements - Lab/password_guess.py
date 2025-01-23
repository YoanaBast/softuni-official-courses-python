#фразата "s3cr3t!P@ssw0rd"
# При съвпадение да се изведе "Welcome".
# При несъвпадение да се изведе "Wrong password!".

password = input()
correct_pass = "s3cr3t!P@ssw0rd"

if password == correct_pass:
    print("Welcome")
else:
    print("Wrong password!")