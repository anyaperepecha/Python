# Задача №3 Обменник.Создать скрипт который будет запускаться из консоли 1 раз из консоли, выдавать результат и зарываться.
# В ВИДЕ ФУНКЦИЙ
# 1. На вход обменнику вводишь количество денег int.
# 2. На выходе в консоль выводится отввет в таком виде:
# "Ты ввёл int (Валюта)"
# "конвертированная сумма в USD = int"
# "конвертированная сумма в EUR = int"
# "конвертированная сумма в CHF = int"
# "конвертированная сумма в GBP = int"
# "конвертированная сумма в CNY = int"
#
# 3. Скипт должен выдать сообщение
# "Введите положительное число." Если число меньше 0.
# "Вы ввели не число. Введите число." Если введены буквы.
# "Вы ввели пустое поле. Введите число." Если введено пустое значение.
# 4. Валюту пользователя определите сами.

def number_check(n):
    try:
        target_amount = float(n)
        return True
    except ValueError:
        return False

def empty_check(n):
    if not (n and n.isspace()) == 0:
        return True
    else:
        return False

def value_check(n):
    if n > 0:
        return True
    else:
        return False

def convertation(n):
    print("Вы ввели сумму =", target_amount, "BYN")
    for i in range(len(currency)):
        currency_result = float(target_amount) * rate[i]
        print("Конвертированная валюта в", currency[i], "=", currency_result)

currency = ["USD", "EUR", "CHF", "GBP", "CNY"]
rate = [0.39, 0.34, 0.36, 0.91, 0.29]
target_amount = input("Количество денег в BYN = ")

if empty_check(target_amount):
    print("Вы ввели пустое поле. Введите число.")

elif number_check(target_amount):

    if float(target_amount) > 0:
        convertation(target_amount)

    elif float(target_amount) < 0:
        print("Введите положительное число.")

else:
    print("Вы ввели не число. Введите число.")