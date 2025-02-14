# You will be given two strings.
# Transform the first string into the second one, letter by letter, starting from the first one.
# After each interaction, print the resulting string only if it is unique.
#
# Note: the strings will have the same length.
s1 = input()
s2 = input()
for l in range(0, len(s1)):
    if s2[l] != s1[l]:
        print(f'{s2[:l+1] + s1[l+1:]}')
