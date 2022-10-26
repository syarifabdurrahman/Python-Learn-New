class User:
    def __init__(self,user_id,username) -> None:
        #initialise attribute
        self.id = user_id
        self.username = username
        self.followers = 0 # this default value
        self.following = 0

    def follow(self,user):
        user.followers += 1
        self.following += 1


user_1 = User("002","syarifabdr")
user_2 = User("023","slappmaass")

user_1.follow(user_2)
print(user_2.following)