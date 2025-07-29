class car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model 
        self.year = year
    
    def __str__(self):
        return f"{self.year} {self.brand} {self.model}"
    
car1 = car("BMW", "X1", 2024)
car2 = car("Toyota", "Camry", 2021)

print(car1)
print(car2)