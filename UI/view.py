import flet as ft
from flet.core.types import MainAxisAlignment

from UI.alert import AlertManager


'''
    VIEW:
    - Rappresenta l'interfaccia utente
    - Riceve i dati dal MODELLO e li presenta senza modificarli
'''

class View:
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "Lab07"
        self.page.horizontal_alignment = "center"
        self.page.theme_mode = ft.ThemeMode.DARK

        # Alert
        self.alert = AlertManager(page)

        # Controller
        self.controller = None

        # creo un contenitore verticale nel flet per ospitare la lista di artefatti
        #momentaneamente lo nascondo, così da farlo comparire solo quando premo mostra artefatti
        self.lista_artefatti = ft.Column()


    def show_alert(self, messaggio):
        self.alert.show_alert(messaggio)

    def set_controller(self, controller):
        self.controller = controller

    def update(self):
        self.page.update()

    #implemento funzioni per aggiornare il dropdown con i dati del model
    def mostra_musei_dropdown(self, lista_musei):
        #riempie il menù dei musei
        self.menu_musei.options = ([ft.dropdown.Option(text="Nessun filtro", key="")] +
                                   [ft.dropdown.Option(text=m, key=m) for m in lista_musei])
        self.menu_musei.value = ""
        self.page.update()

    def mostra_epoche_dropdown(self, lista_epoche):
        #riempie il menù delle epoche
        self.menu_epoca.options = ([ft.dropdown.Option(text="Nessun filtro", key="")] +
                                   [ft.dropdown.Option(text=e, key=e) for e in lista_epoche])
        self.menu_epoca.value = ""
        self.page.update()

    def get_filtro_museo(self):
        #Restituisce il museo selezionato
        valore = self.menu_musei.value
        return valore if valore!= "" else None

    def get_filtro_epoca(self):
        #Restituisce l’epoca selezionata
        valore = self.menu_epoca.value
        return valore if valore!= "" else None


    def load_interface(self):
        """ Crea e aggiunge gli elementi di UI alla pagina e la aggiorna. """

        # --- Sezione 1: Intestazione ---
        self.txt_titolo = ft.Text(value="Musei di Torino", size=38, weight=ft.FontWeight.BOLD)

        # --- Sezione 2: Filtraggio ---
        #definisco i dropdown vuoti, poi credo delle funzioni per riempirli con i dati del model
        #tramite on change viene chiamata la funzione sotto definita, che registra il nuovo filtro impostato
        self.menu_musei = ft.Dropdown(label = 'Museo', width = 200, on_change=self._filtri_changed)
        self.menu_epoca = ft.Dropdown(label = 'Epoca',width = 200, on_change=self._filtri_changed)

        self.row = ft.Row(controls = [self.menu_musei, self.menu_epoca], alignment = MainAxisAlignment.CENTER)
        # TODO

        # Sezione 3: Artefatti
        self.btn_artefatti = ft.ElevatedButton(text="Mostra Artefatti", on_click= self._click_mostra_artefatti )
        # TODO

        # --- Toggle Tema ---
        self.toggle_cambia_tema = ft.Switch(label="Tema scuro", value=True, on_change=self.cambia_tema)

        # --- Layout della pagina ---
        self.page.add(
            self.toggle_cambia_tema,

            # Sezione 1
            self.txt_titolo,
            ft.Divider(),

            # Sezione 2: Filtraggio
            self.row,
            ft.Divider(),
            # TODO

            # Sezione 3: Artefatti
            self.btn_artefatti,
            self.lista_artefatti
            # TODO
        )

        self.page.scroll = "adaptive"
        #self.page.add(self.lista_artefatti)
        self.page.update()

    def cambia_tema(self, e):
        """ Cambia tema scuro/chiaro """
        self.page.theme_mode = ft.ThemeMode.DARK if self.toggle_cambia_tema.value else ft.ThemeMode.LIGHT
        self.toggle_cambia_tema.label = "Tema scuro" if self.toggle_cambia_tema.value else "Tema chiaro"
        self.page.update()

    def _filtri_changed(self, e):
        """Quando cambia un filtro, avvisa il controller."""
        if self.controller:
            self.controller.aggiorna_risultati()

    def _click_mostra_artefatti(self, e):
        """Quando clicchi il bottone, avvisa il controller."""
        if self.controller:
            self.controller.aggiorna_risultati()

    def mostra_artefatti(self, artefatti):
         #svuota prima
        self.lista_artefatti.controls.clear()
        if not artefatti:
            self.lista_artefatti.controls.append(ft.Text("Nessun artefatto trovato."))
        else:
            for a in artefatti:
                 #a è un oggetto artefatto con attributi (id, nome, epoca, id_museo)
                self.lista_artefatti.controls.append(ft.Text(f"{a.nome} • {a.epoca} • {a.nome_museo}"))
        self.lista_artefatti.update()

