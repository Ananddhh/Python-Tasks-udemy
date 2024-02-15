import random
letters = ['a', 'b', 'c', 'd']
numbers = ['1','2', '3', '4']
symbols = ['!', ['@', '#', '$']]

print("welcome to the password gen.")
nr_letters = int(input("how many letters would you like in your password\n"))
nr_numbers = int(input("how many numbers would you like in your password\n"))
nr_symbols = int(input("how many symbols would you like in your password\n"))

password_list = ""

for char in range(1, nr_letters + 1):
    password_list += random.choice(letters)
for char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)
for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)
random.shuffle(password_list)
print(password_list)
