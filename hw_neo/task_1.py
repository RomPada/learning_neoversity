

date = "2020-10-09"

def get_days_from_today(date):
    from datetime import datetime
   
    try:
        date_format = "%Y-%m-%d" # бажаний формат дати
        datetime.strptime(date, date_format) # чи відповідає введений формат бажаному
        
        date_today = datetime.today() # визначення сьогодні
        date_vrbl = datetime.strptime(date, "%Y-%m-%d") # дата у дейтайм
        different = date_today - date_vrbl # отримання різниці
        print(f"{different.days} days") # вивід різниці тільки у .days
    
    except:
        print("Дата у неправильному форматі.")

get_days_from_today(date)

