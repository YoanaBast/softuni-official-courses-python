to_be_removed = input()
main = input()
while to_be_removed in main:
    main = main.replace(to_be_removed, '')

print(main)