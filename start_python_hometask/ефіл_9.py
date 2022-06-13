text = input()
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
        print(res)
    res = res.count('*')

    return res

text = input()

print(words_count (text))
print(simb_count (text))
print(sent_count(text))


# text = input()
# K={'а','у','о','и','e','я'}
# res =set(text) & K
# print (res)
