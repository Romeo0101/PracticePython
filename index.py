from BankOperation.client import Client
from BankOperation.file_handling import *

print("""
########################################

          SIMPLE BANKING SYSTEM

########################################
""")

c1 = Client("Romeo","Delacruz","Estoy","Password")

print(c1.get_saving())


# c1 = client.client("Romeo","Delacruz","Estoy","Password")

# add = file_handling.DatabaseHandling(c1.account_number,c1.savings,c1.first_name,c1.middle_name,c1.last_name,c1.password)

# add.deposit("219762-789121-346369",250)