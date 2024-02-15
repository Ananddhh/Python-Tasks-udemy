print("welcome to the pizzaappie")
size =input("which size do you prefer? S , M or L")
add_pepperoni =input("do you want extra pepperoni ? Y or N")
extra_cheese =input("do you want to add extra cheese ? Y or N")
bill = 0
if size == "S":
    bill += 15
    print("you must pay {bill} ")
elif size == "M":
    bill += 20
    print("you must pay $20")
else:
    bill +=  25
    print("you must pay $25")

if add_pepperoni == "y":
    bill += 5
    print("you must pay {bill}")
if extra_cheese == "y":
    bill += 5
    print("you must pay {bill}")


