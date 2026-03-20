#here will be only code exercises, not the test exsercises and also not anwsers for exams

#exercise 1

p1 = input()
p2 = input()
if p1 == p2:
    print("Пароль принят")
else:
    print("Пароль не принят")
    
#exercise 2

p = int(input())
if p % 2 == 0:
    print("Четное")
else:
    print("Нечетное")

#exercise 3

age = int(input())

if age >= 18:
    print("Доступ разрешен")
else:
    print("Доступ запрещен")
    
#exercise 4

n1 = int(input())
n2 = int(input())
if n1 < n2:
    print(n1)
else:
    print(n2)

#exercise 5

n1 = int(input())
n2 = int(input())
n3 = int(input())

if (n2 - n1) == (n3 - n2):
    print("YES")
else:
    print("NO")

#exercise 6

a1 = int(input())
d = a1 % 10
c = (a1 // 10) % 10
b = (a1 // 100) % 10
a = a1 // 1000
#pp = p1 + p4
#pm = p2 - p3
if (a + d) == (b - c):
    print("ДА")
else:
    print("НЕТ")
    
#also

a, b, c, d = map(int, input())
print('ДА' if a + d == b - c else 'НЕТ')

#exercise 7

n1 = int(input())
n2 = int(input())
n3 = int(input())

na = 0

if n1 < na:
    n1 = na
if n2 < na:
    n2 = na
if n3 < na:
    n3 = na
print(n1 + n2 + n3)

#exercise 8

age = int(input())

if age <= 13:
    print("детство")
elif age <= 24:
    print("молодость")
elif age <= 59:
    print("зрелость")
else:
    print("старость")

#or also

age = int(input())

if 0 <= age <= 13:
    print('детство')
if 14 <= age <= 24:
    print('молодость')
if 25 <= age <= 59:
    print('зрелость')
if 60 <= age:
    print('старость')
    
#exercise 9

a, b, c, d = int(input()), int(input()), int(input()), int(input())
if a > b:
    a = b
if c > d:
    c = d
if a > c:
    a = c
print(a)