# Вариант 2: Генерировать предварительные списки с данными, итерируя которые вы будите записывать данные в создаваемый файл.
import names
import csv
import datetime
import random

# Вариант 2. Создать digits_2.csv файл с 1-м полем которое называется number, в котором будут 300 строк с числами от 10 до 310

def digits_2_file(file_name, digits_list):
    with open(file_name, 'w') as f:
        column = ['Number']
        writer = csv.DictWriter(f, fieldnames=column, lineterminator='\n')
        writer.writeheader()
        writer = csv.writer(f, lineterminator='\n')
        writer.writerows(digits_list)

# Вариант 2. Создать names_2.csv файл с 1-м полем которое называется name, в котором будут 400 строк с разными именами

def names_2_file(file_name, names_list):
    with open(file_name, 'w') as f:
        column = ['Name']
        writer = csv.DictWriter(f, fieldnames=column, lineterminator='\n')
        writer.writeheader()
        writer = csv.writer(f, lineterminator='\n')
        writer.writerows(names_list)

# Вариант 2. Создать emails_2.csv файл с 1-м полем которое называется email, в котором будут 400 строк с разными имейлами что-то@gmail.com


def emails_2_file(file_name, emails_list):
    with open(file_name, 'w') as f:
        column = ['Email']
        writer = csv.DictWriter(f, fieldnames=column, lineterminator='\n')
        writer.writeheader()
        writer = csv.writer(f, lineterminator='\n')
        writer.writerows(emails_list)

# Вариант 2. Создать nne_2.csv файл с 3-мя полями(Number, Name, Email ), в котором будут 450 строк. Имя и часть email до @ должны совпадать.

def nne_2_file(file_name, nne_list):
    with open(file_name, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=['Number', 'Name', 'Email'])
        writer.writeheader()
        writer.writerows(nne_list)

# Добавить в файл nne_2.csv столбец Date и заполнить каждую строку текущей датой и временем. Поле даты заполнить следующим образом:
# a) Первые 50 строк даты по годам от 1980 - 1990 (распределение рандомно)
# b) Следующие 100 строк даты по годам от 1991 - 2000 (распределение рандомно)
# с) Следующие 150 строк даты по годам от 2001 - 2010 (распределение рандомно)
# в) Следующие 150 строк даты по годам от 2011 - 2021 (распределение рандомно)

def nne_2_update(file_name):
    with open(file_name, 'r', newline='') as f:
        date_list = []
        reader = csv.DictReader(f, fieldnames=['Number', 'Name', 'Email'])
        for a in reader:
            date_list.append(a)

    with open(file_name, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=[*date_list[0].keys(), 'Date'])
        writer.writeheader()
        for b in range(0, 451):
            date = datetime.datetime.now()
            if b in range(0, 51):
                date_list[b]['Date'] = date.replace(year=random.randint(1980, 1990))
            elif b in range(50, 151):
                date_list[b]['Date'] = date.replace(year=random.randint(1991, 2000))
            elif b in range(150, 301):
                date_list[b]['Date'] = date.replace(year=random.randint(2001, 2010))
            else:
                date_list[b]['Date'] = date.replace(year=random.randint(2011, 2021))
            writer.writerow(date_list[b])

# Создать файл combo.csv с полями Name, Email, Date. 1000 строк.
# a) Соберите имена из файла nne_2.csv.
# b) недостающие 550 строк имён сгенерируйте.
# с) Имена расположите в алфавитном порядке.
# d) Для имён из файла nne_2.csv забрать даты из nne_2.csv которые были с этими именами в nne_2.csv.
# e) Остальные даты генерировать рандомно.
# f) Добавить и заполнить (можно рандомно) столбы Email, Phone, Gender, Salary.


def combo(nne_2_file, combo_file, names_list):
    with open(nne_2_file, 'r', newline='') as f:
        reader = csv.DictReader(f, fieldnames=['Number', 'Name', 'Email', 'Date'])
        nd_list = []
        for i in reader:
            nd_list.append([i['Name'], i['Date']])
        nd_list = nd_list + names_list
        sorted_list = sorted(nd_list[1:])

    with open(combo_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['Name', 'Email', 'Date', 'Phone', 'Salary', 'Gender'])
        writer.writeheader()
        gender_list = ['Male', 'Female']
        dict = {}
        for j in range(0, 1000):
            if len(sorted_list[j]) == 1:
                dict['Name'] = sorted_list[j][0]
                dict['Date'] = datetime.datetime.now()
                dict['Email'] = dict['Name'].replace(' ', '_') + '@yahoo.com'
                dict['Phone'] = '+375 33 ' + str(random.randint(1111111, 9999999))
                dict['Gender'] = gender_list[random.randint(0, 1)]
                dict['Salary'] = random.randint(1000, 9999)
            else:
                dict['Name'] = sorted_list[j][0]
                dict['Date'] = sorted_list[j][1]
                dict['Email'] = dict['Name'].replace(' ', '_') + '@yahoo.com'
                dict['Phone'] = '+375 33 ' + str(random.randint(1111111, 9999999))
                dict['Gender'] = gender_list[random.randint(0, 1)]
                dict['Salary'] = random.randint(1000, 9999)
            writer.writerow(dict)

digits_list = []
names_list = []
emails_list = []
nne_list = []

for i in range(0, 1000):
    digits_list.append([i])
    name = names.get_full_name()
    names_list.append([name])
    email = names.get_full_name().replace(' ', '_')+'@gmail.com'
    emails_list.append([email])
    nne_list.append({'Number': i, 'Name': name, 'Email': email})

digits_2_file('digits_2.csv', digits_list[10:311])
names_2_file('names_2.csv', names_list[1:401])
emails_2_file('emails_2.csv', emails_list[1:401])
nne_2_file('nne_2.csv', nne_list[0:451])
nne_2_update('nne_2.csv')
combo('nne_2.csv', 'combo.csv', names_list[450:1000])



