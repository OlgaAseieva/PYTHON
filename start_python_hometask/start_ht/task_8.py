# 8.1 создать словарь дней недели

week = {1:'Monday', 2: 'Thuesday', 3: 'Wendnesday', 4:'Thursday', 5:'Friday'}
week[6] ='Saturday'
week[7] = 'Sunday'
print(week)

# 8.2 Описание кота
cats = {
    'cat_1' :{
        'name' : "Mouse",
        'sex' : 'female',
        'age' : 5,
        'weight' : 2.5
    },
    'cat_2' :{
        'name' : "Majesties",
        'sex' : 'male',
        'age' : 3,
        'weight' : 4
    }
}
print(cats)
print(cats['cat_1'])
#print(f'cat 1, name : {cats['cat_1']['name']}, cat 2 name: {cats['cat_2']['name']}')

# 8.3.1 Считать строку и посчитать сколько каких букв в ней содержится
s = input('enter string:')
res ={}
for item in s:
    if res.get(item):
        res[item] += 1
    else:
        res[item] = 1
print(res)

# 8.3.2 Считать строку и посчитать сколько каких букв в ней содержится
s = input('enter string:')
res ={}
for item in s:
    if not res.get(item):
        res[item] = s.count(item)
print(res)




