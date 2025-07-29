class user:
    user_count = 0

    def __init__(self, username):
        self.username = username
        user.user_count += 1

    def user_info(self):
        print(f"Username: {self.username}")

    @classmethod
    def user_count_info(cls):
        print(f"Total users created: {cls.user_count}")

user1 = user("Mohan")
user2 = user("Balor")
user3 = user("Thor")
user4 = user("Mark")

user1.user_info()
user2.user_info()
user3.user_info()
user4.user_info()

user.user_count_info()