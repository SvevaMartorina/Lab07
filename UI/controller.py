import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.museo_selezionato = None
        self.epoca_selezionata = None

        self._view.load_interface()  # 1) crea i controlli
        self.carica_musei()  # 2) popola dropdown
        self.carica_epoca()

        self.aggiorna_risultati()


    # POPOLA DROPDOWN
    def carica_musei(self):
        musei = self._model.get_musei()  # prendi dal DB
        #for museo in musei:
            #lista_musei.append(museo)
        self._view.mostra_musei_dropdown(musei) # passa alla View

    def carica_epoca(self):
        lista_epoche = []
        epoche = self._model.get_epoche()
        #for epoca in epoche:
            #lista_epoche.append(epoca)
        self._view.mostra_epoche_dropdown(epoche)
    # TODO

    # CALLBACKS DROPDOWN - # AZIONE: MOSTRA ARTEFATTI
    #riceve i risultati dei filtri impostati e aggiorna la lista degli artefatti filtrandoli

    def aggiorna_risultati(self):
        self.museo_selezionato = self._view.get_filtro_museo()
        self.epoca_selezionata = self._view.get_filtro_epoca()
        artefatti = self._model.get_artefatti_filtrati(self.museo_selezionato, self.epoca_selezionata)
        self._view.mostra_artefatti(artefatti)

    # TODO