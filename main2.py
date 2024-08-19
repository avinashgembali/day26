# list comprehension
# lists = [7, 8, 9]
# new_list = [n + 1 for n in lists]
# print(new_list)
# name = "avinash"
# new_letter_list = [letter for letter in name]
# print(new_letter_list)
#
# double_list = [n * 2 for n in range(1,5)]
# print(double_list)
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_list = [n for n in numbers if n % 2 == 0]
# print(even_list)

# dictionary comprehension
import random
names = ["avinash", "rahul", "sai"]
marks_dict = {name: random.randint(1, 100) for name in names}
print(marks_dict)
passed_students = {name: marks for (name, marks) in marks_dict.items() if marks > 60}
print(passed_students)
