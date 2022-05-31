# 6.1 счастливий билет
print('******** task 1 var 1 ********\n ')
k = list(input('enter ticket number k= '))
sum1, sum2 = 0, 0
if not len(k) % 2:
    t1 = k[:int(len(k)/2)]
    for i in t1:
        sum1 += int(i)
    t2=k[int(len(k)/2):]
    for i in t2:
        sum2 += int(i)
    print('lucky ticket' if sum1 == sum2 else 'try again')
else:
    print('incorrect number')

# 6.1 var 2
print('******** task 1 var 2 ********\n ')
#k = list(input('enter ticket number k= '))

sum1, sum2 = 0, 0
if not len(k) % 2:
    for i in range (int(len(k)/2)):
        sum1 += int(k[i])
    for i in range (int(len(k)/2), len(k)):
        sum2 += int(k[i])
    print('lucky ticket' if sum1 == sum2 else 'try again')
else:
    print('incorrect number')


# 6.1 var 3
print('******** task 1 var 3 ********\n ')
k = list(map(int, input('enter ticket number = ')))

# USEFUL TO KNOW:
#k=[int(i) for i in t]
# or
#for i in t:
#    k.append(int(i))
#print(k, type(k[0]))
#k1 = k[:int(len(k)/2)]
#k2 = k[int(len(k)/2):len(k)]


sum1 = sum(k[:len(k)//2])
sum2 = sum(k[len(k)//2:len(k)])
print('lucky ticket' if sum1 == sum2 else 'try again')

# 6.2 является ли введенное число палиндромом
print('******** task 2 ********\n ')
k = input('enter number k= ')
print('polinom' if k == k[::-1] else 'not polinom')

# 6.3 опредилить лежит ли точка внутри круга
print('******** task 3 ********\n ')

x, y = int(input('enter coordinates x= ')), int(input('y= '))
R = 4
# coordinate of center O (0,0)
xO=0
yO=0
print('Yes' if (x-xO)**2 + (y-yO)**2 <= R**2 else 'no')

# 6.4 посчитать нечетніе числа в списке
print('******** task 4 ********\n ')
l = [0, 5, 2, 4, 7, 1, 3, 19]
sum_even = 0
for i in l:
    if i % 2:
        sum_even += i
print('sum of even numbers in list =', sum_even)

# 6.5.1 создать список, потом из него другой в 2 раза большу с удвоен 2й частью
print('******** task 5 var 1 ********\n ')
x = list(input('enter list x= '))
print(x, type(x[0]))
y=[]
for i in x:
    y.append(int(i))
for i in range(len(x)):
    y.append(2*int(x[i]))
print(x)
print(y)

#6.5.2
print('******** task 5 var 2 ********\n ')
x = list(input('enter list x= '))
y=[0]*2*len(x)
for i in range (len(x)):
    y[i], y[i+len(x)] = int(x[i]), 2*int(x[i])

print(x)
print(y)

# 6.6.  Найти среднюю зп рабочего за 12 мес(зп в списке и єто случ числа от7500 до 1500
print('******** task 6 ********\n ')
import random
times = 12
x=[]
sum_salary = 0
i = 0
while i < times:
    k=random.randint(7500, 15000)
    x.append(k)
    sum_salary += x[i]
    i += 1

print(x)
print(f'average salary for {times} months = {int(sum_salary/times)}')

# 6.7 содать матрицу в ввиде влож сиасков и вівести ее, знач от 1 до 16
print('******** task 7 ********\n ')
m=4
n=5
x =[]
el = 1
for i in range(m):
    x.append([0]*n)
print(x)
for i in range(0, m):
    for j in range (0, n):
        x[i][j] = el
        el += 1
print(x, type(x[2][2]), type(x[1]) )

