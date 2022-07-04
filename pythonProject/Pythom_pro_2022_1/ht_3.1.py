try:
    f_text = open('text_for_ht_3.txt', 'rt')
    f_text = f_text.read()
    print(f_text)
except FileExistsError:
    print ('No file')

import string


class Count_text:

    def __init__(self, f_text):
        self.f_text = f_text

    def count_letters(self):
        if not self.f_text:
            raise FileExistsError('Trable with file reading')
        else:
            sum_leters=0
            for item  in self.f_text:
                if item not in (string.punctuation+'1234567890'):
                    sum_leters +=1
            return sum_leters

    def count_words(self):
        if not self.f_text:
            raise FileExistsError('Trable with file reading')
        else:
            for item in self.f_text:
                if item in string.punctuation:
                       data = self.f_text.replace(item, " ")
            sum_word = len(data.split())
        return  sum_word

    def count_lines(self):
        if not self.f_text:
            raise FileExistsError('Trable with file reading')
        else:
            count = 0
            sum_lines = [count + 1 for i in self.f_text if i == '\n']
        return sum_lines

    def __str__(self):
        res = f'Summa of letters in file: {self.count_letters()}, \n quantity of words in file is: {self.count_words()}, \n Quantity of lines is : {self.count_lines()} \n'
        return  res

statist = Count_text('text_for_ht_3.txt')
#print(Count_text.__dict__)
print(statist)
