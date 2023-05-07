
if __name__ == '__main__':

 print('1. задача:')
'''Принтиране на 'i', докато е по-малко или равно на 5'''
i = 1
while i <= 5:
  print(i)
  i += 1

print('2. задача:')
'''обхождане на масив и принтиране на всеки елемент от него'''
fruits = ["ябълка", "банан", "ягода"]
for fruit in fruits:
  print(fruit)

print('3. задача:')
'''обхождане и принтиране на числата от 1 до 4 с for loop'''
for i in range(1, 4):
  for j in range(1, 4):
   print(i, j)