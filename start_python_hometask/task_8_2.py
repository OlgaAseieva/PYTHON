# 8.4 написать числа  до 1 000 000 буквами (в деньгах)
s = input('enter number')
s_l = s.split('.')
s_z = s_l[0].rjust(6,'0')
s_z = list(s_z)
s_kop = s_l[1] if len(s_l) > 1 else ' 00'

# print(s_l, s_z, s_kop)

digits_let = {
    #'unit':{
        0: 'zero',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
    #},
    #'dosens_1':{
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eightteen',
        19: 'nineteen',
    #},
   #  'dosens_2':{
        20: 'tventy',
        30: 'thirty',
        40: 'forty',
        50: 'fifty',
        60: 'sixty',
        70: 'seventy',
        80: 'eighty',
        90: 'ninety',
  #   },
 #    'hundreds':{
        100: 'hundred',
        1000: "thousand",
        1000000: 'million'
  #   }
}

alfa_number = [0]*6

for i in range (0, len(s_z), 3):
        if  int(s_z[i]):
                alfa_number[i] = digits_let.get(int(s_z[i])) + " " + digits_let.get(100)
        else:
                alfa_number[i] = ' '
# print(alfa_number)
# k=int(s_z[1]+s_z[2])
# print(k, type(k))

for i in range (1, len(s_z), 3):
         if  9 < int(s_z[i] +s_z[i+1]) < 20:
                 alfa_number[i] = digits_let.get(int(s_z[i] +s_z[i+1]))
                 alfa_number[i+1] = ' '
         elif  int(s_z[i]):
                 alfa_number[i] = digits_let.get(int(s_z[i])*10)
         else:
                alfa_number[i] = ' '
# print(alfa_number)

for i in range (2, len(s_z), 3):
        if int(s_z[i]):
                if alfa_number[i] != ' ':
                        alfa_number[i] = digits_let.get(int(s_z[i]))
        else:
                alfa_number[i] = ' '
#print(alfa_number)

if  alfa_number[0] != " " or alfa_number[1] != " " or alfa_number[2] != " ":
        alfa_number.insert (3, digits_let.get(1000))

print(alfa_number)

k = ' '.join(alfa_number)

if alfa_number == [' ']*6:
        k += digits_let.get(0)

print(f' {k} hriven {s_kop} kop.')


