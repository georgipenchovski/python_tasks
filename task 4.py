if __name__ == '__main__':

    # a.
    numbers = [num for num in range(1, 31)]
    print(numbers)


    # b.
    def sum_numbers_ending_in_3(numbers):
        """
        Изчислява сумата на числата от даден списък, които завършват на 3.

        :param numbers: списък с числа
        :return: сумата на числата, завършващи на 3
        """
        total = 0
        for num in numbers:
            if num % 10 == 3:
                total += num
        return total


    numbers = [num for num in range(1, 31)]
    print(numbers)

    total = sum_numbers_ending_in_3(numbers)
    print(total)
