# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

 '''Сравняване на променлива с if/else'''
 print('1. задача:')
x = 10
print(f'x = {x}')
if x > 5:
    print("x е по-голямо от 5")
else:
    print("x е по-малко или равно на 5")

print('2. задача:')

x = 11
print(f'x = {x}')
if x > 15:
    print("x е по-голямо от 15")
elif x > 5:
    print("x е по-голямо от 5, но по-малко или равно на 15")
else:
    print("x е по-малко или равно на 5")
