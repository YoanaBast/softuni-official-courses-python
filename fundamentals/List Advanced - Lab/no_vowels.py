# Using comprehension, write a program that receives a text and removes all its vowels, case insensitive.
# Print the new text string after removing the vowels.
# The vowels that should be considered are 'a', 'o', 'u', 'e', 'i'
text = input()
letters = [letter for letter in text if letter.lower() not in ['a', 'o', 'u', 'e', 'i']]
print(''.join(letters))
