ask_user = int(input("how many favorite fruits you like to insert ? "))

storage_fruits = []

for repeat in range(ask_user):
    fruits = input("Enter Fruits you like : ")
    storage_fruits.append(fruits)

for fruits in storage_fruits:
    print(fruits)