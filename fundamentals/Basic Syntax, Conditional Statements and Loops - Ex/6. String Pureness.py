# You will be given the number n. After that, you'll receive different strings n times.
# Your task is to check if the given strings are pure,
# meaning that they do NOT consist of any of the characters: comma ",", period ".", or underscore "_":
#
# · If a string is pure, print "{string} is pure."
#
# · Otherwise, print "{string} is not pure!"

n = int(input())
for nx in range(n):
    stringche = input()

    if "," in stringche \
        or "." in stringche \
        or "_" in stringche:

        print(f"{stringche} is not pure!")
    else:
        print(f"{stringche} is pure.")