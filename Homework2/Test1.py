# Пользователь вводит одно число N – количество арбузов.
# Вторая строка содержит N чисел, записанных на новой строчке каждое.
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

countOfWatermelons = int(input("Введите количество арбузов: "))
weight = []

for i in range(countOfWatermelons):
    weight.append(int(input()))

min = weight[0]
max = weight[0]
i = 1
for i in range(len(weight)):
    if weight[i] > max:
        max = weight[i]
    if weight[i] < min:
        min = weight[i]
print(f"{min}  {max}")
