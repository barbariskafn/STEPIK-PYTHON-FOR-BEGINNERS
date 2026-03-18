#here will be only code exercises, not the test exsercises and also not anwsers for exams

#exercise 1

a = int(input())
q = int(input())
n = int(input())
b = int(a**1*q**(n-1))
print(b)

#exercise 2

a = int(input())
b = int(a//100)
print(b)

#exercise 3

n = int(input())
k = int(input())
res = int(k//n)
res2 = int(k%n)
print(res)
print(res2)

#exercise 4

a = int(input())
res = int((a+1)//2)
print(res)

#exercise 5

a = int(input())
chas = int(a//60)
min = int(a%60)
print(a, "мин - это", chas, "час", min, "минут.")

#exercise 6

a = int(input())
n = ((a+3)//4)
print(n)

#exercise 7

n = int(input())

a = n // 100
b = (n // 10) % 10
c = n % 10

print("Сумма цифр =", a + b + c)
print("Произведение цифр =", a * b * c)

#exercise 8

n = int(input())

a = n // 100
b = (n // 10) % 10
c = n % 10

print(a, b, c, sep = '')
print(a, c, b, sep = '')
print(b, a, c, sep = '')
print(b, c, a, sep = '')
print(c, a, b, sep = '')
print(c, b, a, sep = '')

#exercise 9

n = int(input())

# Получаем цифры
a = n // 1000          # тысячи → 3281 // 1000 = 3
b = (n // 100) % 10    # сотни → 3281 // 100 = 32, 32 % 10 = 2
c = (n // 10) % 10     # десятки → 3281 // 10 = 328, 328 % 10 = 8
d = n % 10             # единицы → 3281 % 10 = 1

# Вывод
print('Цифра в позиции тысяч равна', a)
print('Цифра в позиции сотен равна', b)
print('Цифра в позиции десятков равна', c)
print('Цифра в позиции единиц равна', d)

#exercise 10