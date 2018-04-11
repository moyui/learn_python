class Student(object):
    count = 0 

    def __init__(self, name):
        self.name = name
a = Student('gaogao')
b = Student('qiqi')
a.count = 1
print(a.count)
print(b.count)