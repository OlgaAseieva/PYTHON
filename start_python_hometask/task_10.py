# class work
def words_count (text):
    text_1 = list(text.split())

    return len(text_1)

def simb_count (text):
    text_2 = list(text)

    return len(text_2)

def sent_count (text):
    simb = ".!?"
    res=text
    for item in simb:
        res = res.replace(item, '*')
        #print(res)
    res = res.count('*')

    return res

text = input(' enrer text:')

print(words_count (text))
print(simb_count (text))
print(sent_count(text))

# ht_1
def max_number(l_n):
    l_n = l_n.split()
    l_n = list(map(int, l_n))

    return max(l_n)

l_n = input('Enter list number: ')

print(max_number(l_n))

# ht_2 принимает 2 числа и строку, возвращает сумму чисел +строка
def concaten(a, b, c):

    sum_number = str(int(a) + int (b)) + c
    return sum_number

print(concaten(input('number 1:'), input('number 2:'), input('enter string:')))

# ht_3 нарисовать прямоугольник из **
def rectangle (a,b):

    p_1 ='*'*a
    p_2 = (b-2)*f"*{' '*(a-2)} *\n"

    return print(f'{p_1}\n{p_2+p_1}')

rectangle(int(input('\n enter width a =')), int(input('enter height b =')))

# ht_4 найти в списке нужній єл-т и вернуть его индекс, если нет єл- та, то вкрнуть -1
def find_element(l,n):
    l= list(l.split())
    if n in l:
        return l.index(n)
    else:
        return -1

l = input('enter list:')
n = input('enter element:')

print(f' element index or -1 as default: {find_element(l, n)}')

# ht_5 вернуть количкство слов
def words_qv(l):
    l= list(l.split())

    return len(l)

text = input('enter text:')

print(words_qv(text))

# ht_6
dic_seq={
    1: lambda a,: a +2,
    2: lambda a,: a +3,
    3: lambda a,: a +4,
    4: lambda a,: a +5,
    5: lambda a,: a *2,
    6: lambda a,: a *3,
    7: lambda a,: a **2,
    8: lambda a,: a **3
}

def find_seq(l):
        for i in range (len(dic_seq)) :
            new =[l[0], dic_seq[i](l[0]), dic_seq[i](l[1])]
            print(new)
            if l[:3] == new:
                print(i)
                return k = dic_seq[i]
        return 'error'

def nextel_sequence(l, k):
    l = l.append(k (l[-1]))
    print(l)
    return l[-1]

l = input('enter sequence:')
l = list(map(int, l.split(',')))
print (f' i= {find_seq(l)}')

print(nextel_sequence(l, k))
