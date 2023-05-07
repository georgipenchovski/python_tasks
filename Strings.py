
if __name__ == '__main__':

 my_string = "Hello, world!"
 print(my_string)

print('1. задача:')
'''Извличане на символ по индекс'''
print(my_string[0])
print(my_string[-1])

print('2. задача:')
'''Извличане на подниз чрез срезове'''
print(my_string[0:5])  # "Hello"
print(my_string[7:])  # "world!"

print('3. задача:')
'''Използване на низови методи за конвертиране или модифициране на низове'''
print(my_string.upper())  # "HELLO, WORLD!"
print(my_string.replace("world", "Python"))  # "Hello, Python!"