import datetime

class Person:
    def __init__(self, age: int, sex : str):
        self.age = age
        self.sex = sex

    def __str__(self):
        return f'{self.sex}: {self.age}'

class Student(Person):

    def __init__(self, name: str, surname: str, age: int, sex : str, *args, **kwargs):
        super().__init__(age, sex)
        self.name = name
        self.surname = surname


    def __str__(self):
        return f'{self.surname} {self.name}, {self.age} y.o., {self.sex}'

class Group:
    limit = 10

    def __init__(self, id_group: str,  *args, **kwargs):
        self.group =[]
        self.reserve = []
        self.id_group = id_group

    def add_group(self, stud: Student):
        if stud not in self.group and len(self.group) < Group.limit:
            self.group.append(stud)
        else:
            self.reserve.append(stud)

    def remove_stud (self, stud: Student):
        if stud in self.group:
            self.group.remove(stud)
            return f'{stud.surname} {stud.name} was removed from group {self.id_group} \n'

    def find_st(self, stud: Student):
        if stud in self.group:
            return f'Student {stud.surname} {stud.name} is in group {self.id_group} \n'
        else:
            return f'Student {stud.surname} {stud.name} was not find in the group {self.id_group} \n'


    def __str__(self):
        res = f'{datetime.date.today()} \n'
        res += f'Group {self.id_group}: \n'
        for i, item in enumerate(self.group):
            res += f" {i+1}.  {item} \n"
        res += f' Reserve: \n'
        for i, item in enumerate(self.reserve):
            res += f' {i+1}. {item} \n'

        return res

if __name__ == '__main__':

    st_1 = Student('Olga', 'As', 20, 'F')
    st_2 = Student('Georg', 'Fed', 22, 'M')
    st_3 = Student('Irina', 'Mar', 21, 'F')
    st_4 = Student('Irina', 'Gut', 23, 'F')
    st_5 = Student('Roman', 'Mus', 22, 'M')
    st_6 = Student('David', "Zas", 23, 'M')
    st_7 = Student('Vera', 'Tom', 19, 'F')
    st_8 = Student('Sasha', "Cot", 19, "F")
    st_9 = Student('Dima', 'Dor', 23, 'M')
    st_10 = Student('Dima', 'Ganz', 20, 'M')
    st_11 = Student('Oksana', 'Dok', 20, "F")
    st_12 = Student('Illya', 'Dok', 21, 'M')

    gr = Group('Salsa')
    gr.add_group(st_1)
    gr.add_group(st_2)
    gr.add_group(st_3)
    gr.add_group(st_4)
    gr.add_group(st_5)
    gr.add_group(st_6)
    gr.add_group(st_7)
    gr.add_group(st_8)
    gr.add_group(st_9)
    gr.add_group(st_10)
    gr.add_group(st_11)
    gr.add_group(st_12)

    print(gr)
    print(gr.remove_stud(st_9))
    print(gr.find_st(st_1))


