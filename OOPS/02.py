class car():
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def startengine(self):
        print(f"The engine of {self.year} {self.brand} {self.model} has started.")

mycar = car("BMW", "X1", 2024)

mycar.startengine()