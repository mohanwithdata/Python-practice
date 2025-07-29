class car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

mycar = car("BMW", "X1", 2024)

print("Car Brand: ", mycar.brand)
print("Car Model: ", mycar.model)
print("Car Year: ", mycar.year)

