class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def compare_age(self, other_person):
        if self.age > other_person.age:
            print(f"{self.name} is older than {other_person.name}.")
        elif self.age < other_person.age:
            print(f"{self.name} is younger than {other_person.name}.")
        else:
            print(f"{self.name} and {other_person.name} are of the same age.")
        
person1 = person("Mohan", 25)
person2 = person("Balor", 20)

person1.compare_age(person2)
