print("welcome to the tip  calculator")
bill = int(input("what was the total bill ? $"))
tip = int(input("how percentage tip would you like to give? 10,12 or 15?"))
people = int(input("how many people to split the bill?"))
tip_as_percent = tip / 100
total_tip_ampunt = bill * tip_as_percent
total__bill = total_tip_ampunt + bill
per_person =  total__bill / people
final= round(per_person,2)
print(final)

