import calendar
import datetime

class AmelioSaludaCorrectamente:
    def __init__(self):
        self.date = datetime.datetime.now()
    def obtenerSaludo(self):
        return self.greetHourSelection(int(self.date.strftime("%w")))
    def obtenerFechaFormateada(self):
        return self.toWeekDay(int(self.date.strftime("%w")))+", "+str(self.date.day)+" de "+ self.toMonthYear(int(self.date.strftime("%m")))+" de " +str(self.date.year)
    def obtenerFechaSimplificada(self):
        return str(self.date.day)+"/"+str(self.date.strftime("%m"))+"/" +str(self.date.year)
    def toWeekDay(self, weeknumber):
        days =["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"]
        return days[weeknumber-1]
    def toMonthYear(self, yearnumber):
        months = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
        return months[yearnumber-1]
    def greetHourSelection(self, hournumber):
        if hournumber < 12 and hournumber >= 6:
            return "Buenos días"
        if hournumber > 21 and hournumber < 6:
            return "Buenas noches"
        return "Buenas tardes"

amelio = AmelioSaludaCorrectamente()
message = amelio.obtenerSaludo() +"\n\nSoy Amelio 🙊, hoy es "+amelio.obtenerFechaFormateada() +".\nSoy el asistente virtual de DoctorPC y estoy aquí para ayudarte, por favor selecciona lo que necesites:"
print(message)