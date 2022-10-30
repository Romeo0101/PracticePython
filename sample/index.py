import os

temp_file = open("temp_file.txt",mode="w")

id = "1"
value = 2
name = "Ohms"

file = open("file.txt", "r")
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

os.remove("file.txt")
os.rename("temp_file.txt","file.txt")