from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import AllSlotsReset
from rasa_sdk.types import DomainDict
from rasa_sdk.forms import FormAction

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
            {"title":"AMD ryzen 9","payload":"ryzen 9"}]
        if familia_procesador == "intel":
            button_resp=[{"title":"Intel i3","payload":'i3'},
            {"title":"Intel i5","payload":"i5"},
            {"title":"Intel i7","payload":"i7"},
            {"title":"Intel i9","payload":"i9"}]
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
        date = datetime.datetime.now()
        datestr = self.toWeekDay(int(date.strftime("%w")))+", "+str(date.day)+" de "+ self.toMonthYear(int(date.strftime("%m")))+" de " +str(date.year)
        saludo = self.greetHourSelection(int(date.strftime("%w")))
        dispatcher.utter_message(text="{saludo} soy Amelio 🙊, hoy es {datestr}. Soy el asistente virtual de DoctorPC y estoy aquí para ayudarte, por favor selecciona lo que necesites:", buttons=button_resp)
        return []
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