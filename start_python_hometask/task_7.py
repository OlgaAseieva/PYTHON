# # 7.1 посчитать колво подстроки 'b' в введенной
# x = input('Enter string:')
# count = x.count('b')
# print(count)
#
# # 7.2 Почистить строку и вівести ее с большой букви
# x = input('Enter name:')
# import string
# #print(string.punctuation)
# for item in string.punctuation + ' 0987654321':
#     x = x.replace(item, '')
# print(x.title())
#
# #7.3 посчитать сумму кодов символов в строке
# x = input('Enter string:')
# sum_code = 0
# for item in x:
#     sum_code += ord(item)
# print(sum_code)

# #7.4 вівести 10 раз число Пи с кол-м знаков 2 и более
# from math import pi
# for i in range(2,5):
#       print(f'pi = {pi:.{i}f}')

# #7.5 Найти самое длинное слово в строке
# x = input('Enter string:')
# x=x.split()
# y = list(map(len, x))
# print('Max length =', max(y))
#
# # 7.6 виделить слово из строки повторов єтого слова
# x = input('Enter string:')
# y =[x[0]]
# for i in range (1, len(x)):
#     if x[i] != y[i-1]:
#         y.append(x[i])
#         if ''.join(y) == x[i+1:i+1+len(y)]:
#             break
#     else:
#         break
# print(''.join(y))
#
# # 7.7 избавиться от хежтегов
# x = input('Enter string:')
# while '<' in x:
#     k1, k2 = x.find('<'), x.find('>')
#     print(k1,k2, x[k1:k2+1])
#     x = x.replace(x[k1:k2+1], '')
# print(x)
#
#
x= input("str")
x = x.replace('!','.')
x = x.replace('?','.')
while ".." in x:
    x = x.replace("..", '.')

print(x.count('.'))

