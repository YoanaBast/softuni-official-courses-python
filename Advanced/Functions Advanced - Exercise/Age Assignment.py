# def age_assignment(*args, **kwargs):
#     result = ''
#     for key, value in kwargs.items():
#         for name in args:
#             if name.startswith(key):
#                 result += f"{name} is {value} years old.\n"
#     return result

# def age_assignment(*args, **kwargs):
#     result = ''
#     for name in args:
#         if name and name[0] in kwargs:
#             result += f"{name} is {kwargs[name[0]]} years old.\n"
#     return result

def age_assignment(*args, **kwargs):
    data = {}
    for first_letter, age in kwargs.items():
        names = [name for name in args if name.startswith(first_letter)]
        for name in names:
            data[name] = age

    sorted_data = sorted(data.items(), key=lambda kvp: kvp[0])
    result = ''
    for name, age in sorted_data:
        result += f"{name} is {age} years old.\n"

    return result

# import unittest
#
# class Tests(unittest.TestCase):
#     def test(self):
#         res = age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61)
#         self.assertEqual(res.strip(),
#                          "Amy is 22 years old.\n"
#                          "Bill is 61 years old.\n"
#                          "Willy is 36 years old.")
#
# if __name__ == "__main__":
#     unittest.main()

print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))