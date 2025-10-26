
dictionary = {1: "Monday", 2: "Tusday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}

#q=int(input("Input numeric from 1 to 7:"))
#
#if 1 <= q <= 7:
#    print(f"Today is {dictionary[q]}.")
#else:
#    print("Invalid input! Please enter a number between 1 and 7.")

### below variant #2


q = int(input("Please enter a number from 1 to 7: "))

day = dictionary.get(q, "Invalid input! Please enter a number between 1 and 7.")
print(f"Today is {day}.")
