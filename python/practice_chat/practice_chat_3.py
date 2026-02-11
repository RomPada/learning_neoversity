
number = int(input("Input number: "))

if number % 2:
# version from chat (але тоді потрібно замінити місцями парне/непарне):
# if number % 2 == 0:  # Перевірка, чи залишок від ділення на 2 дорівнює 0
    print("Число непарне")
else:
   print("Число парне")

num = int(input("Enter a number: "))
if num > 0: 
    if num % 2:
        result = "Positive odd number"
    else:
        result = "Positive even number"
elif num < 0:
    result = "Negative number"
else:
    result = "It is zero"
print(result)
