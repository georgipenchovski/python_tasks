
if __name__ == '__main__':

 even_sum = 0  # променлива за сумата на четните числа
odd_sum = 0   # променлива за сумата на нечетните числа

# обхождаме числата от 1 до 200 включително
for num in range(1, 201):
    if num % 2 == 0:
        # числото е четно
        even_sum += num
    else:
        # числото е нечетно
        odd_sum += num

# извеждаме резултатите
print("Сумата на четните числа е:", even_sum)
print("Сумата на нечетните числа е:", odd_sum)