# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# Пример 10: 0, 1, 2, 3
2^1
number = int(input("Введите число: "))


count = 0
while pow(2, count) <= number:
    print(count, end=' ')
    count +=1


