import random

class Client():
    def __init__(self, first_name, middle_name, last_name, password):
        self.id = 1
        self.account_number = f"{random.randint(100000,999999)}-{random.randint(100000,999999)}-{random.randint(100000,999999)}"
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.password = password
        self.savings = 0
    
    def get_name(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"
    
    def get_account_number(self):
        return self.account_number
    
    def get_password(self):
        return self.password
    
    def get_saving(self):
        return self.savings
    
    

