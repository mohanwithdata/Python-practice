class studentinfo():

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def info(self):
        print(f'student Name: {self.name}')
        print(f'Student Age: {self.age}')
        print(f'Student Grade: {self.grade}')

student1 = studentinfo("Mohan", 20, "D+")

student1.info()