from datetime import datetime
from BankOperation.client import Client

class DatabaseHandling(Client):
    def __init__(self, account_number, savings, first_name, middle_name, last_name, password):
        super().__init__(self.account_number,savings,first_name,middle_name,last_name,password)
    
    def add_client(self):
        with open("database.txt", "w") as data:
            data.write(f"{self.account_number}/{self.first_name}/{self.middle_name}/{self.last_name}/{self.password}/{self.savings}")

    def deposit(self,value):
        import os

        temp_file = open("temp_file.txt",mode="w")
        file = open("database.txt", "r")
        
        for line in file:
            toList = line.split("/")
            if(toList[0] == id):
                savings = int(toList[1])
                savings += value
                temp_file.write(f"{id}/{savings}/{name}\n")
            else:
                temp_file.write(f"{toList[0]}/{toList[1]}/{toList[2]}")

        temp_file.close()
        file.close()

        os.remove("database.txt")
        os.rename("temp_file.txt","database.txt")