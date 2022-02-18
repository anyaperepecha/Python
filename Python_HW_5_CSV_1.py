# Вариант 1: Генерировать данные на лету, не создавая предварительных списков.

# Создать пустой empty.csv файл.
import csv
import names

def empty_file(file_name):
    f = open(file_name, 'w')
    f.close()

empty_file("empty.csv")

# Вариант 1. Создать digits.csv файл с 1-м полем, в котором будут 150 строк с числами от 0 до 150

def digits_file(file_name):
    with open(file_name, 'w') as f:
        writer = csv.writer(f, lineterminator='\n')
        for i in range(0, 151):
            writer.writerow([i])

digits_file("digits.csv")

# Вариант 1. Создать names.csv файл с 1-м полем, в котором будут 100 строк с разными именами

def names_file(file_name):
    with open(file_name, 'w') as f:
        writer = csv.writer(f, lineterminator='\n')
        for i in range(0, 100):
            writer.writerow([names.get_full_name()])

names_file("names.csv")

# Вариант 1. Создать emails.csv файл с 1-м полем, в котором будут 100 строк с разными имейлами что-то@gmail.com

def emails_file(file_name):
    with open(file_name, 'w') as f:
        writer = csv.writer(f, lineterminator='\n')
        for i in range(0, 100):
            writer.writerow([names.get_full_name().replace(' ', '_')+'@gmail.com'])

emails_file("emails.csv")

# Вариант 1. Создать nne.csv файл с 3-мя полями (Number, Name, Email), в котором будут 100 строк. Имя и часть email до @ должны совпадать.

def nne_file(file_name):
    with open(file_name, 'w') as f:
        columns = ['Number', 'Name', 'Email']
        writer = csv.DictWriter(f, fieldnames=columns, lineterminator='\n')
        writer.writeheader()
        for i in range(1, 101):
            writer.writerow({'Number': i,
                             'Name': names.get_full_name(),
                             'Email': names.get_full_name().replace(' ', '_')+'@gmail.com'})

nne_file("nne.csv")



