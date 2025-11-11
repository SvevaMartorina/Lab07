from database.DB_connect import ConnessioneDB
from model.museoDTO import Museo

"""
    Museo DAO
    Gestisce le operazioni di accesso al database relative ai musei (Effettua le Query).
"""

class MuseoDAO:
    def __init__(self):
        #creo la connessione usando il metodo della classe ConnessioneDB
       pass

    #restituisce una lista con tutti i musei
    def get_museo (self):
        cnx = ConnessioneDB.get_connection()
        if cnx is None:
            raise RuntimeError("Connessione al DB non disponibile")
        else:
            cursor = cnx.cursor()
            query = ("SELECT id, nome, tipologia "
                     "FROM museo "
                     "ORDER BY nome")
            cursor.execute(query)
            musei = []
            for row in cursor.fetchall():
                museo = Museo(row[0], row[1], row[2])
                musei.append(museo)
            cursor.close()
        return musei
    # TODO
