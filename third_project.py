number = (input("введіть 5-значне число: "))
number = int(number)
print(number // 10000)
hundredths = (number // 1000) % 10
print(hundredths)
tenths = (number // 100) % 10
print(tenths)
units = (number // 10) % 10
print(units)
number_five = (number % 10)
print(number_five)
rev_number1 = (number_five % 10)
rev_number2 = (units * 1)
rev_number3 = (tenths * 1)
rev_number4 = (hundredths * 1)
rev_number5 = (number // 10000)
print("перевернуте число:")
print(rev_number1)
print(rev_number2)
print(rev_number3)
print(rev_number4)
print(rev_number5)
