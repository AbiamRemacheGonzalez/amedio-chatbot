from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionPedirInformacionSobreReparaciones(Action):

    def name(self) -> Text:
        return "action_ofrecer_ayuda_adicional"

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

class ActionPedirInformacionSobreReparaciones(Action):

    def name(self) -> Text:
        return "action_modelo_procesador"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # button_resp=[{"title":"Horario","payload":'horario'},
        #     {"title":"Contacto","payload":"contacto"},
        #     {"title":"Dirección","payload":"ubicacion"},
        #     {"title":"🔧¿Que reparamos?🔧","payload":"reparación"},
        #     {"title":"Comprar equipo","payload":"comprar equipo"},
        #     {"title":"Consultas","payload":"consultas"},
        #     {"title":"Estado de reparación","payload":"estado de reparación"},
        #     {"title":"Otros","payload":"otros"},
        #     {"title":"Salir","payload":"adios"}]

        dispatcher.utter_message(text="Pregunta del modelo de procesador")

        return []