class User: 
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password 

    def say_hi_to_user(self,user):
        print(
            f"Sending message to {user.username} at {user.email} from {self.username} : Hi {user.username}, it's {self.username} here"
        )
user1 = User("rits", "ritika@gmail.com", "123")
user2 = User("prachi", "prachi@gmail.com", "456")

user1.say_hi_to_user(user2)
