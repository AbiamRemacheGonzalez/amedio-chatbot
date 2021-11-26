import calendar
import datetime


# datestr = date.weekday+", "+date.day+" de "+ date.month+" de " +date.year

def toWeekDay(weeknumber):
    days =["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"]
    return days[weeknumber-1]
def toMonthYear(yearnumber):
    months = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
    return months[yearnumber]
def greetHourSelection(hournumber):
    if hournumber < 12 and hournumber >= 6:
        return "Buenos días"
    if hournumber > 21 and hournumber < 6:
        return "Buenas noches"
    return "Buenas tardes"
date = datetime.datetime.now()
datestr = toWeekDay(int(date.strftime("%w")))+", "+str(date.day)+" de "+ toMonthYear(int(date.strftime("%m")))+" de " +str(date.year)
saludo = greetHourSelection(int(date.strftime("%w")))
print(saludo)