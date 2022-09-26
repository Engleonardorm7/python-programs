from datetime import datetime
import pytz

bogota_timezone=pytz.timezone("America/Bogota")
bogota_date=datetime.now(bogota_timezone)
print("Bogota: ",bogota_date.strftime("%d/%m/%Y, %H:%M:%S"))

mexico_timezone=pytz.timezone("America/Mexico_City")
mexico_date=datetime.now(mexico_timezone)
print("Mexico: ",mexico_date.strftime("%d/%m/%Y, %H:%M:%S"))