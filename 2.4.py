#here will be only code exercises, not the test exsercises and also not anwsers for exams

#exercise 1

a = int(input())
b = int(a + 1)
c = int(a + 2)
print(a)
print(b)
print(c)

#exercise 2

num1 = int(input())
num2 = int(input())
num3 = int(input())
print(num1 + num2 + num3)

#exercise 3

num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
print((num1 + num2 + num3 + num4) * 3)

#exercise 4

a = int(input())
b = int(input())

result = 3 * (a + b) * (a + b) * (a + b) + 275 * b * b - 127 * a - 41

print(result)

#exercise 5

a = int(input())
b = int(a + 1)
c = int(a - 1)
print("Следующее за числом", a,"число:", b)
print("Для числа", a,"предыдущее число:", c)

#exercise 6

a = int(input())
v = int(a * a * a)
s = int(a * 6 * a )

print("Объем =", v)
print("Площадь полной поверхности =", s)

#exercise 7

a = int(input())
b = int(input())

print(a, "+", b ,"=", a + b)
print(a, "-", b ,"=", a - b)
print(a, "*", b ,"=", a * b)

#exercise 8

a1 = int(input())
d = int(input())
n = int(input())

an = a1 + d * (n - 1)

print(an)

#exercise 9

x = int(input())

print(1 * x, 2 * x, 3 * x, 4 * x, 5 * x, sep = "---")