# Задача 2: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.

print("1- орел <=> 0 - решка.")
n = int(input("Введите количество монеток: "))
money = []

import random
for i in range(n):
    money.append(random.randint(0, 1))
print(money)
count1 = 0
count2 = 0
for i in range(len(money)):
    if money[i] == 0:
        count1 += 1
    if money[i] == 1:
        count2 += 1

if count2 > count1:
    print(count1)
if count1 > count2:
    print(count2)



