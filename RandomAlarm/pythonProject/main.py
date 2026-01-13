import random
from datetime import datetime, timedelta

start_time_str = input("Введи початковий час (наприклад 5:00): ")
end_time_str = input("Введи кінцевий час (наприклад 6:00): ")

start_time = datetime.strptime(start_time_str, "%H:%M")
end_time = datetime.strptime(end_time_str, "%H:%M")

delta_minutes = int((end_time - start_time).total_seconds() // 60)

random_minutes = random.randint(0, delta_minutes)

alarm_time = start_time + timedelta(minutes=random_minutes)

print("Твій будильник стоїть на:", alarm_time.strftime("%H:%M"))