# 8.4 написать числа буквами (в деньгах)
s = input('enter number')
s_l = list(s)
print(s_l)
if '.' in s:
    t = s.find('.')
    s_kop = s_l[t+1:t+3]
    s_z = int(''.join(s_l[:t]))

else:
        s_kop ='00 коп.'
        s_z = int(''.join(s_l))

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

alfa_numbee = [0]*6

for i in range(0, len(s_l), 3):
        if not s_l[i]:
                alfa_numbee[i] = digits_let.get(s_l[i]) + digits_let.get(s_l[100])
                print(alfa_numbee)
        else:
                alfa_numbee[i] = '*'
# for i in range(1, len(s_l), step=3):
#         if  0 < int(''.join(s_l[i:i+2]) < 20:
#                 alfa_numbee[i] = digits_let.get(s_l[i])
#                 alfa_numbee[i+1] = '*'
#                 print(alfa_numbee)
#         elif not s_l[i]:
        #a = digits_let.get(s_l[-4])
        #b = digits_let.get(s_l[-5])
        #print(a,b)


#print(f'{''.join(s_kop)} коп.' if s_kop else '00 коп.')
#print(digits_let.keys())
