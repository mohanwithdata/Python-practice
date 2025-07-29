class dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def bark(self):
        print(f"{self.name} says: Woof! I am a {self.breed}")

dog1 = dog("Bruno", "Labrador")
dog2 = dog("Max", "German Shepherd")
dog3 = dog("Daisy", "Pug")

dog1.bark()
dog2.bark()
dog3.bark()