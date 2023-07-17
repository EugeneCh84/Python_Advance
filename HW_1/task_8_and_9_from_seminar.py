# Нарисовать в консоли ёлку спросив у пользователя количество рядов.
# Пример результата:
# Сколько рядов у ёлки?
#    *
#    ***
#   *****
#  *******
# *********

print("Задание №8 с семинара")
rows = int(input("Сколько рядов у ёлки? "))
for i in range(1, rows + 1):
    spaces = " " * (rows - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)



# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.


print("Задание №9 с семинара")
factor = 2
number = 2
while (number < 10):
    if (factor <= 10):
        print(f"{number}x{factor} = {number * factor}")
        factor +=1
    else:
        print(" ")
        factor = 2
        number += 1
        continue