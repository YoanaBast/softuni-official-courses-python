username = input()
password = input()
created_password = password
while True:
    enter_password = input()
    if enter_password == created_password:
        print(f"Welcome {username}!")
        break