from datetime import datetime

print(f"Today is {datetime.now()}")
now=datetime.now()
day=(now.strftime('%m/%d/%Y'))
print(day)
day=(now.strftime('%d/%m/%Y'))
print(day)
day=(now.strftime('estamos en el año %Y'))
print(day)
