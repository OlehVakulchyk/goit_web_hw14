# # Import the os module
# import os

# # Print the current working directory
# print("Current working directory: {0}".format(os.getcwd()))

# # Change the current working directory
# os.chdir('./goit_web_hw13/')

# # Print the current working directory
# print("Current working directory: {0}".format(os.getcwd()))


# import unittest

# def multiply_numbers(x, y):
#     return x * y

# class TestMultiplication(unittest.TestCase):
#     def test_multiply_two_positive_numbers(self):
#         result = multiply_numbers(2, 3)
#         self.assertEqual(result, 6)
    
#     def test_multiply_positive_and_negative_numbers(self):
#         result = multiply_numbers(2, -3)
#         self.assertEqual(result, -6)
    
#     def test_multiply_two_negative_numbers(self):
#         result = multiply_numbers(-2, -3)
#         self.assertEqual(result, 6)

# if __name__ == '__main__':
#     unittest.main()

import sys
print(sys.path)

"""
Функцию pkgutil.iter_modules() можно использовать, чтобы получить 
список всех модулей, которые можно импортировать из заданного пути:
"""
import pkgutil
search_path = ['.'] # Используйте None, чтобы увидеть все модули, импортируемые из sys.path
all_modules = [x[1] for x in pkgutil.iter_modules(path=search_path)]
print('----------------------')
print(all_modules)

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


from goit_web_hw13.database.models import UserContact, User
#import ..goit_web_hw13