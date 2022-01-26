# Задача №4
# ПРОЦЕДУРНЫЙ ВИД
# Обменник. Скрипт запускается в консоли и работает постоянно. Остановится нажатием ctrl+c.
#     1. Скрипт сначала выводит "Выберите валюту из ['USD','EUR','CHF','GBP','CNY']"
#     2. Пользователь вводит один из 5 вариантов ['USD','EUR','CHF','GBP','CNY']
#     3. Потом Скрипт выводит "Введите сумму"
#     4. Пользователь вводит сумму int
#     5. Скрипт выводит:
#             "Вы ввели сумму int и валюту "Валюта" "
#             "конвертированная сумма в "Валюта" = int"
#     6. Скипт должен выдать сообщение
#                 "Введите положительное число." Если число меньше 0.
#                 "Вы ввели не число. Введите число." Если введены буквы.
#                 "Вы ввели пустое поле. Введите число." Если введено пустое значение.
#     7. После сообщеня об ошибке, скрипт должен автоматом вернуться к шагу 1.
#     8. Валюту пользователя определите сами.

currency_range = ['USD', 'EUR', 'CHF', 'GBP', 'CNY']
rate = [0.39, 0.34, 0.36, 0.91, 0.29]

while True:
    currency = None
    currency_name = input("Выберите валюту из ['USD', 'EUR', 'CHF', 'GBP', 'CNY'] = ")

    for i in range(len(currency_range)):
        if currency_name.lower() == currency_range[i].lower():
            currency = i

    if currency is None:
        print("Выберите валюту из списка")
        continue

    target_amount = input("Введите сумму = ")

    try:
        target_amount = int(target_amount)
        integer = True
    except:
        integer = False

    if not target_amount:
        print("Вы ввели пустое поле. Введите число.")

    elif integer:
        if target_amount > 0:
            currency_result = int(target_amount) * rate[currency]
            print("Вы ввели сумму =", target_amount, "и валюту = ", currency_range[currency])
            print("Конвертированная сумма в BYN = ", currency_result)

        else:
            print("Введите положительное число.")

    else:
        print("Вы ввели не число. Введите число.")