class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.isrewards_memeber = False
        self.gold_card_points = 0
        self.usesr = []


    def display_Info(self):
        print(self.first_name, self.last_name, self.email, self.age, self.isrewards_memeber, self.gold_card_points, sep='\n')
        return self
    def enroll(self):
        users = []
        if(self.isrewards_memeber == True):
            print("User already a member")
            return False
        else:
            self.isrewards_memeber = True
            self.gold_card_points = 200
        return self

    def spend_points(self, amount):
        if self.gold_card_points > amount:
            self.gold_card_points -= amount
        return self
alan = User("alan", "chin", "willian.tun@gmail.com", 31)
alan.display_info().enroll().spend_points(50).display_info()
kelly = User("kelly" , "chin", "kellychin@gmail.com", 22)
kelly.enroll().spend_points(80).display_info()

"""
alan = User("alan", "chin", "willian.tun@gmail.com", 31)
alan.enroll()
kelly = User("kelly" , "chin", "kellychin@gmail.com", 22)
ashley = User("Ashley", "chin", "ashley@gmail.com", 33)
alan.spend_points(50)
kelly.enroll()
kelly.spend_points(80)
alan.display_Info()
kelly.display_Info()
"""


