from datetime import datetime

def get_days_from_today(date):
    
    try:
        day = datetime.strptime(date, '%Y-%m-%d').date()
    except ValueError:
        return "Неправильний формат дати. Використовуйте формат 'РРРР-ММ-ДД'."

    day_today = datetime.today().date()
    difference = (day_today - day).days
    return difference

print(get_days_from_today('2007-03-12'))