# Задача 4: Требуется определить, можно ли от шоколадки размером n × m долек
# отломить k долек, если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no

number1 = int(input("Введите размер n: "))
number2 = int(input("Введите размер m: "))
number3 = int(input("Введите количество долек, которые хотите отломить: "))

if number3 < number1 * number2 and (number3 % number1 == 0 or number3 % number2 == 0):
    print("yes")
else:
    print("no")