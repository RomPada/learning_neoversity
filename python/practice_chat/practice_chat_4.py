
age = int(input("Enter your age: "))

if age == 0:
    print("You cann`t input 0. Please enter your age.")
elif 1 <= age <= 13:
    print("You are child.")
elif 14 <= age <= 17:
    print("You are teenager.")
else:
    print("You are adult.")

# while True:
#     age = int(input("Enter your age: "))
#     
#     if age == 0:
#         print("You can't input 0. Please enter your age.")
#     elif 13 <= age <= 19:
#         print("You are a teenager.")
#         break  # Виходимо з циклу, якщо вік підліток
#     else:
#         print("You are not a teenager.")
#         break  # Виходимо з циклу, якщо вік не підліток
