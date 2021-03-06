# Задача №3 Обменник.Создать скрипт который будет запускаться из консоли 1 раз из консоли, выдавать результат и зарываться.
# ПРОЦЕДУРНЫЙ ВИД
# 1. На вход обменнику вводишь количество денег int.
# 2. На выходе в консоль выводится отввет в таком виде:
# "Ты ввёл int (Валюта)"
# "конвертированная сумма в USD = int"
# "конвертированная сумма в EUR = int"
# "конвертированная сумма в CHF = int"
# "конвертированная сумма в GBP = int"
# "конвертированная сумма в CNY = int"
# 3. Скрипт должен выдать сообщение
# "Введите положительное число." Если число меньше 0.
# "Вы ввели не число. Введите число." Если введены буквы.
# "Вы ввели пустое поле. Введите число." Если введено пустое значение.
# 4. Валюту пользователя определите сами.

currency = ["USD", "EUR", "CHF", "GBP", "CNY"]
rate = [0.39, 0.34, 0.36, 0.91, 0.29]
target_amount = input("Количество денег в BYN = ")

try:
    target_amount = float(target_amount)
    it_float = True

except ValueError:
    it_float = False

if it_float and target_amount > 0:
    print("Вы ввели сумму =", target_amount, "BYN")

    for i in range(len(currency)):
        currency_result = target_amount * rate[i]
        print("Конвертированная сумма в", currency[i], "=", currency_result)

elif it_float and target_amount < 0:
    print("Введите положительное число.")

elif not (target_amount and target_amount.isspace()) == 0:
    print("Вы ввели пустое поле. Введите число.")

else:
    print("Вы ввели не число. Введите число.")