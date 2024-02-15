height = float(input("whats your height in m: "))
weight = float(input("whats your weight in kg: "))
bmi = round(weight / height ** 2)
if bmi < 18.5:
    print("u r underweight")
elif bmi < 25:
    print("u r normal weight")
elif bmi < 30:
    print("u r overweight")
else:
    print("scene ahnu bud")
