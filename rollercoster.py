print("welcum to rollercoster")
height = int(input("what is your height in m"))
bill = 0
if height <= 80:
    print("you cant ride")
else:
    print("you can ride")
age = int(input("what is your age ?"))
if age <= 18:
    bill = 12
    print("you want to pay $12")
elif age <= 12:
    bill = 7
    print("you must pay $7")
elif age <= 12:
    bill = 12
    print("you must pay $5")
elif age >= 45 and age <= 55:
    print("everything is going to be ok. have a free ride on us!")
else:
    bill = 13
    print("you must pay $13")
pic = input("if you want pictures ? y or N")
if pic == "y":
    bill += 3
    print(f"then you must pay {bill}") 
 

