print("welcome to the game fizzbuzz geeks!")
for number in range(1, 101):
  if number % 3 == 0 & number % 5 == 0:
    print("fizzzzbuzz")
  elif number % 3 == 0:
    print("fizz")
  elif number % 5 == 0:
    print("buzz")
  else:
    print(number)

      