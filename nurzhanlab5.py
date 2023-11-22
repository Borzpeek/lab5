# task
# 1.1
# a = input("Ввод: ")
# b = a.lower().replace(' ', '')
# char_list = list(b)
# print("Созданный список является:")
# print(char_list)
#
# task
# 1.2
# work = ['p', 'u', 'l', 'p', 'f', 'i', 'c', 't', 'i', 'o', 'n']
# fr_list = [(char, work.count(char)) for char in set(work)]
# print("Вывод: ")
# print(fr_list)
# task
# 1.3
# task = [('p', 2), ('u', 1), ('l', 1), (' ', 1), ('f', 1), ('i', 2), ('c', 1), ('t', 1), ('o', 1), ('n', 1)]
# vowels = "aeiou"
# list_vow = [(char, freq) for char, freq in task if char in vowels]
# list_cons = [(char, freq) for char, freq in task if char.isalpha() and char not in vowels]
# list_sym = [(char, freq) for char, freq in task if not char.isalnum()]
# print("list_vow =", list_vow)
# print("list_cons =", list_cons)
# print("list_sym =", list_sym
# task
# 1.4
# import numpy as np
#
#
# def divide_into_quartiles(task):
#     sorted_list = np.sort(task)
#     quartiles = np.array_split(sorted_list, 4)
#
#     return tuple(quartiles)
#
#
# task1 = [1, 5, 8, 7, 9, 6, 7, 5, 8, 3, 9, 10, 2, 1, 3, 4]
# q1, q2, q3, q4 = divide_into_quartiles(task1)
# print("Code Output:")
# print("q1 =", q1)
# print("q2 =", q2)
# print("q3 =", q3)
# print("q4 =", q4)
#
# task2 = [1, 5, 8, 7, 9, 6, 7, 5, 8, 3, 9, 10, 2, 1, 3, 4, 8]
# q1, q2, q3, q4 = divide_into_quartiles(task2)
# print("\nSecond Code Output:")
# print("q1 =", q1)
# print("q2 =", q2)
# print("q3 =", q3)
# print("q4 =", q4)
# task
# 2.1
# student1 = 'Adam'
# assignment_scores = [82, 56, 44, 30]
# lab_scores = [78.20, 77.20]
# test_scores = [78, 77]
# student = {
#     'name': student1,
#     'assignment': assignment_scores,
#     'test': test_scores,
#     'lab': lab_scores
#
# }
# print("student =", student['name'])
# task
# 2.2
# student = {'name': 'Adam', 'assignment': [82, 56, 44, 30], 'test': [78, 77], 'lab': [78.2, 77.2]}
# submission_rate = 6 if len(student['assignment']) == 4 and len(student['test']) == 2 and len(student['lab']) == 2 else 0
# submission_check = {student['name']: submission_rate}
# print(submission_check)
#
# task
# 2.3
#
#
# def calculate_final_grade(student, submission_rate):
#     if student['name'] in submission_rate and submission_rate[student['name']] >= 4:
#         assignment_average = sum(student.get('assignment', [])) / len(student.get('assignment', []))
#         lab_average = sum(student.get('lab', [])) / len(student.get('lab', []))
#         test_average = sum(student.get('test', [])) / len(student.get('test', []))
#         final_grade = 0.3 * assignment_average + 0.5 * lab_average + 0.2 * test_average
#         student['final_grade'] = round(final_grade, 2)
#     else:
#         student['final_grade'] = 0
#
#     return student
#
#
# student = {'name': 'Nur', 'assignment': [82, 56, 44, 30], 'test': [78, 77], 'lab': [78.2, 77.2]}
# submission_rate = {'Nur': 6}
# student = calculate_final_grade(student, submission_rate)
# print(student)
#
# student2 = {'name': 'Nurzhan', 'assignment': [82, 30], 'test': [], 'lab': [78.2]}
# submission_rate2 = {'Adam': 6, 'Kevin': 3}
# student2 = calculate_final_grade(student2, submission_rate2)
# print(student2)
# task
# 2.4
# student = {'name': 'Nurzhan', 'assignment': [82, 56, 44, 30], 'test': [78, 77], 'lab': [78.2, 77.2],
#            'final_grade': 70.25}
# student1 = {'name': 'Nur', 'assignment': [82, 30], 'test': [], 'lab': [78.2], 'final_grade': 0}
#
# students = {s['name']: {key: s[key] for key in ['assignment', 'test', 'lab', 'final_grade']} for s in
#             [student, student1]}
# print(students)
# task
# 3.1
# transactions = [(1001, 2), (1001, 1), (1003, 2), (1005, 2), (1001, 3), (1007, 1), (1007, 2), (1100, 2), (1003, 2),
#                 (1001, 1)]
# stats = {}
# for user, transaction_type in transactions:
#     user_stats = stats.setdefault(user, {1: 0, 2: 0, 3: 0, 'mft': None, 'lft': None})
#     user_stats[transaction_type] += 1
#     if user_stats['mft'] is None or user_stats[transaction_type] > user_stats[user_stats['mft']]:
#         user_stats['mft'] = transaction_type
#     if user_stats['lft'] is None or user_stats[transaction_type] < user_stats[user_stats['lft']]:
#         user_stats['lft'] = transaction_type
# stats = {str(user): stats[user] for user in stats}
# print(stats)
