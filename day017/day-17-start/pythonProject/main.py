class User:
    """User class"""
    def __init__(self, id, username):
        self.id = id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "Chase")
user_2 = User("002", "Schmirl")


user_1.follow(user_2)
print(user_1.followers, user_2.following)
print(user_1.following, user_2.followers)
# print(user_2, user_1)

class Car:
    """Car Class"""
    def __init__(self, seats):
        self.seats = seats

    def get_seats(self):
        return self.seats

    def set_seats(self, seats):
        self.seats = seats

    def enter_race_mode(self):
        self.seats = 2


