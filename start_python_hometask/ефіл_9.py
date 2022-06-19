
def func (a,b):
    if not b :
        return 1
    return a*func(a,b-1)

print(func (2,5))

