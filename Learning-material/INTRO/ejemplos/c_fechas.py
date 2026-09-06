from datetime import datetime, date, timedelta
hoy = date(2026, 9, 6)
print("hoy:", hoy)
print("formato dd/mm/aaaa:", hoy.strftime("%d/%m/%Y"))
print("dentro de 7 dias:", hoy + timedelta(days=7))
nacimiento = date(1995, 3, 15)
dias_vividos = (hoy - nacimiento).days
print("dias vividos:", dias_vividos)
momento = datetime(2026, 9, 6, 21, 30)
print("fecha y hora:", momento.strftime("%d/%m/%Y %H:%M"))
print("solo la hora:", momento.hour)
