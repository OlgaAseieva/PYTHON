# 5.1 числа от 1 до 100 kратніе 7

for i  in range(7, 101, 7):
    print (i)

# 5.2 найти n!, 4<n<16
while True:
    n=int(input('\n enter n = '))
    if  n < 4 or n > 16:
        print('incorrect n ')
    else:
        break
for i in range(1, n+1):
    n *= i
print('\n n! = ', n)


# 5.3 таблица умножения на 5
for i in range (11):
    print(f'{i} * 5 = {i*5}')

# 5.4 нарисовать прямоугольник из *
a = int(input('\n enter width a ='))
b = int(input('enter height b ='))
b_=' '*(a-2)
print("*"*a)
print((b-2)*f"*{' '*(a-2)} *\n")
print("*"*a)


# 5.5 вівести все простіе числа от 1 до 100

for n in range(2, 101):
    for i in range(2, n):
        if n % i == 0:
            break
    else:
        print(n)

# 5.6 нарисовать песочне часи из **

a = int(input('\n enter odd number a ='))
if a % 2 and a > 0:
    for i in range(a // 2 +1):
        print(" "*i + '*'*(a-2*i))
    for i in range(a // 2-1, -1, -1):
        print(" "*i + '*'*(a-2*i))
else:
    print('incorrect number!')
