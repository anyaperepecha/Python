# 1) Создать переменную типа String
a = 'a'

# 2) Создать переменную типа Integer
a = 12

# 3) Создать переменную типа Float
a = 1.22

# 4) Создать переменную типа Bytes
a = bytes(10)

# 5) Создать переменную типа List
a = list('world')

# 6) Создать переменную типа Tuple
a = tuple('world')

# 7) Создать переменную типа Set
a = {1, 'a', 3}

# 8) Создать переменную типа Frozen set
a = frozenset('hello')

# 9) Создать переменную типа Dict
a = {'cats': 3,
     'dogs': 2}

# 10) Вывести в консоль все выше перечисленные переменные с добавлением типа данных.
print(type(a), a)

# 11) Создать 2 переменные String, создать переменную в которой сканкатенируете эти переменные. Вывести в консоль.
a = 'Dear'
b = 'Lord'
c = a + b
print(type(c), c)

# 12) Вывести в одну строку переменные типа String и Integer используя “,” (Запятую)
a = 'Dear'
b = 2
print(a, str(b))

# 13) Вывести в одну строку переменные типа String и Integer используя “+” (Плюс)
a = 'Dear'
b = 2
print(a + str(b))