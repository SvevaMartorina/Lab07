from database.museo_DAO import MuseoDAO
from database.artefatto_DAO import ArtefattoDAO
import mysql.connector
'''
    MODELLO: 
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di MuseoDAO e ArtefattoDAO)
'''

class Model:
    def __init__(self):
        self._museo_dao = MuseoDAO()
        self._artefatto_dao = ArtefattoDAO()

        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="musei_torino"
        )


    # --- ARTEFATTI ---
    def get_artefatti_filtrati(self, museo:str, epoca:str):
        """Restituisce la lista di tutti gli artefatti filtrati per museo e/o epoca (filtri opzionali)."""
        return self._artefatto_dao.get_artefatti_filtrati(museo, epoca)
        # TODO

    def get_epoche(self):
        """Restituisce la lista di tutte le epoche."""
        return self._artefatto_dao.get_epoche()
        # TODO

    # --- MUSEI ---
    def get_musei(self):
        """ Restituisce la lista di tutti i nomi dei musei."""
        return [museo.nome for museo in self._museo_dao.get_museo()]
        # TODO

