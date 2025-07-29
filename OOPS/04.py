class laptop:
    def __init__(self, brand, processor, price):
        self.brand = brand
        self.processor = processor
        self.price = price

    def specs(self):
        print(f"Laptop Brand: {self.brand}")
        print(f"Laptop Processor: {self.processor}")
        print(f"Laptop Price: {self.price}")

laptop1 = laptop("Dell", "Intel i5", 55000)
laptop2 = laptop("Acer", "Intel i5", 75000)

laptop1.specs()

print("-"*30)

laptop2.specs()

