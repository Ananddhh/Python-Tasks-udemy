height = int(input("what is your height?"))
if height <= 80:
    print("cant ride")
else:
    print("yes you can ride")
    age = int(input("whats your age"))
    if age <= 12:
     print("$7")
    elif age <= 18:
     print("pay $12")
    else:
     print("$14")    
    