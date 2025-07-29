class movie:
    def __init__(self, title: str, year: int, rating: float):
        self.title = title
        self.year = year
        self.rating = rating

    def classic(self) -> bool:
        return self.year < 2000
    
    def info(self) -> None:
        print(f"title   : {self.title}")
        print(f"Year    : {self.year}")
        print(f"Rating  : {self.rating}/10")

        if self.classic():
            print("This is a classic movie.")

movie1 = movie("The Matrix", 1999, 8.7)
movie1.info()







