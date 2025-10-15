users = [
    {"name": "John Doe", "birthday": "1985.10.20"},
    {"name": "Jane Smith", "birthday": "1990.11.27"}
]


def get_upcoming_birthdays(users):
    from datetime import datetime
    for user in users:
        birthday = datetime.strptime(user["birthday"], "%m.%d")
    date_today = datetime.today() # визначення сьогодні   
    
    
    year_of_birth = int(user["birthday"].split(".")[0])  # Отримуємо рік народження

    if year_of_birth > 1990:
        print(user["name"])



upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
