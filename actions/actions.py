from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionPedirInformacionSobreReparaciones(Action):

    def name(self) -> Text:
        return "action_pedir_informacion_sobre_reparaciones"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        button_resp=[{"title":"Equipo de sobremesa","payload":"equipo de sobremesa"}
        ,{"title":"Portatiles","payload":"portatiles"}
        ,{"title":"Moviles","payload":"moviles"}
        ,{"title":"Play Station 4","payload":"play station"}
        ,{"title":"Nintendo Switch","payload":"switch"}
        ,{"title":"Tablets","payload":"tablet"}
        ,{"title":"Mac","payload":"mac"}
        ,{"title":"Ipad","payload":"ipad"}
        ,{"title":"Ayuda","payload":"ayuda"}]

        dispatcher.utter_message(text="En Doctor Pc Las Palmas reparamos todo tipo de equipos electrónicos de todas las marcas:", buttons=button_resp)

        return [{"rep_menu" : True}]
