#here will be only code exercises, not the test exsercises and also not anwsers for exams

#exercise 1

x = int(input())

if -1 < x < 17:
    print('Принадлежит')
else:
    print('Не принадлежит')
    
#exercise 2

x = int(input())

if -30 < x <= -2 or 7 < x <= 25:
    print('Принадлежит')
else:
    print('Не принадлежит')
    
#exercise 3

num = int(input())

if 1000 <= num <= 9999 and (num % 7 == 0 or num % 17 == 0):
    print("YES")
else:
    print("NO")

#exercise 4

a = int(input())
b = int(input())
c = int(input())

if a + b > c and a + c > b and b + c > a:
    print("YES")
else:
    print("NO")

#exercise 5

x = int(input())
if (x % 4 == 0 and x % 100 != 0) or (x % 400 == 0):
    print("YES")
else:
    print("NO")
    
#exercise 6

a = int(input())
b = int(input())
c = int(input())
d = int(input())
if (a == c) or (b == d):
    print("YES")
else:
    print("NO")
    
#exercise 7

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if (x1 - 1 <= x2 <= x1 + 1) and (y1 - 1 <= y2 <= y1 + 1):
    print("YES")
else:
    print("NO")