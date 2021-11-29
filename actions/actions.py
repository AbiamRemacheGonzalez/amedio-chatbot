from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import AllSlotsReset
from rasa_sdk.types import DomainDict
from rasa_sdk.forms import FormAction
from mail_manager import MailManager

import datetime
import calendar
import smtplib

#https://www.youtube.com/watch?v=dGH91BxXVis

class ActionResetCompraSlots(Action):

    def name(self) -> Text:
        return "action_reset_comprar_slots"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [SlotSet("familia_procesador", None),SlotSet("modelo_procesador", None),SlotSet("cantidad_ram", None),SlotSet("grafica_dedicada", None)]
class ActionResetCompraSlots(Action):

    def name(self) -> Text:
        return "action_reset_personal_slots"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [SlotSet("nombre", None),SlotSet("telefono", None),SlotSet("mail", None),SlotSet("proteccion_datos", None)]

class ActionAyudaAdicional(Action):

    def name(self) -> Text:
        return "action_ayuda_adicional"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        button_resp=[{"title":"Horario","payload":'horario'},
            {"title":"Contacto","payload":"contacto"},
            {"title":"Dirección","payload":"ubicacion"},
            {"title":"🔧¿Que reparamos?🔧","payload":"reparación"},
            {"title":"Comprar equipo","payload":"comprar equipo"},
            {"title":"Consultas","payload":"consultas"},
            {"title":"Estado de reparación","payload":"estado de reparación"},
            {"title":"Otros","payload":"otros"},
            {"title":"Salir","payload":"adios"}]

        dispatcher.utter_message(text="¿Puedo ayudarte en algo más?", buttons=button_resp)

        return []

class ActionAskModeloProcesador(Action):
    def name(self) -> Text:
        return "action_ask_modelo_procesador"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        familia_procesador = tracker.get_slot("familia_procesador")
        if familia_procesador == "amd":
            button_resp=[{"title":"AMD ryzen 3","payload":'ryzen 3'},
            {"title":"AMD ryzen 5","payload":"ryzen 5"},
            {"title":"AMD ryzen 7","payload":"ryzen 7"},
            {"title":"AMD ryzen 9","payload":"ryzen 9"},
            {"title":"Cancelar","payload":"cancelar"}]
        if familia_procesador == "intel":
            button_resp=[{"title":"Intel i3","payload":'i3'},
            {"title":"Intel i5","payload":"i5"},
            {"title":"Intel i7","payload":"i7"},
            {"title":"Intel i9","payload":"i9"},
            {"title":"Cancelar","payload":"cancelar"}]
        dispatcher.utter_message(text="¿Que modelo de procesador quieres?", buttons=button_resp)
        return []

class ActionSaludo(Action):
    def name(self) -> Text:
        return "action_saludo"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        button_resp=[{"title":"Horario","payload":'horario'},
            {"title":"Contacto","payload":"contacto"},
            {"title":"Dirección","payload":"ubicacion"},
            {"title":"🔧¿Que reparamos?🔧","payload":"reparación"},
            {"title":"Comprar equipo","payload":"comprar equipo"},
            {"title":"Consultas","payload":"consultas"},
            {"title":"Estado de reparación","payload":"estado de reparación"},
            {"title":"Otros","payload":"otros"},
            {"title":"Salir","payload":"adios"}]
        amelio = AmelioSaludaCorrectamente()
        message = amelio.obtenerSaludo +"\n\nSoy Amelio 🙊, hoy es "+amelio.obtenerFechaFormateada+".\nSoy el asistente virtual de DoctorPC y estoy aquí para ayudarte, por favor selecciona lo que necesites:"
        dispatcher.utter_message(text=message, buttons=button_resp)
        return []

class AmelioSaludaCorrectamente:
    def __init__(self):
        date = datetime.datetime.now()
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
        return months[yearnumber]
    def greetHourSelection(self, hournumber):
        if hournumber < 12 and hournumber >= 6:
            return "Buenos días"
        if hournumber > 21 and hournumber < 6:
            return "Buenas noches"
        return "Buenas tardes"

class ActionMostrarResultadosSobremesa(Action):

    def name(self) -> Text:
        return "action_tratar_resultados_sobremesa"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Recoger los datos
        familia_procesador = tracker.get_slot("familia_procesador")
        modelo_procesador = tracker.get_slot("modelo_procesador")
        cantidad_ram = tracker.get_slot("cantidad_ram")
        grafica_dedicada = tracker.get_slot("grafica_dedicada")
        nombre = tracker.get_slot("nombre")
        telefono = tracker.get_slot("telefono")
        mail = tracker.get_slot("mail")
        proteccion_datos = tracker.get_slot("proteccion_datos")
        if proteccion_datos:
            # Enviar correo electrónico
            mail_manager = MailManager()
            message = "El cliente "+nombre+" con telefono "+telefono+" y con correo electrónico "+mail+" quiere un presupuesto de un Equipo sobremesa:\n\
            Procesador=\t"+familia_procesador+" "+modelo_procesador+"\n\
            RAM=\t"+cantidad_ram+"\n\
            Gráfica dedicada=\t"+grafica_dedicada
            # Mostrar mensaje
            message = nombre + " tu petición se ha enviado. Lo atenderemos con la mayor brevedad."
            dispatcher.utter_message(text=message)
        else:
            button_resp=[{"title":"Aceptar","payload":'horario'},
            {"title":"Rechazar","payload":"contacto"},
            {"title":"Cancelar","payload":"cancelar"}]
            amelio = AmelioSaludaCorrectamente()
            message = amelio.obtenerSaludo +", "+nombre + " para poder tratar la información debes aceptar la política de protección de datos."
            dispatcher.utter_message(text=message,buttons=button_resp)
        return [SlotSet("familia_procesador", None),SlotSet("modelo_procesador", None),SlotSet("cantidad_ram", None),SlotSet("grafica_dedicada", None)]