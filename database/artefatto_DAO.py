from database.DB_connect import ConnessioneDB
from model.artefattoDTO import Artefatto

"""
    ARTEFATTO DAO
    Gestisce le operazioni di accesso al database relative agli artefatti (Effettua le Query).
"""

class ArtefattoDAO:
    def __init__(self):
        # creo la connessione usando il metodo della classe ConnessioneDB
        pass

    #creo una funzione che dopo aver creato la connessione con il database
    #seleziona tutte le righe della colonna artefatto
    #inserendoli nella classe artefatto

#restituisce una lista contenente tutti gli artefatti
    def getArtefatto(self, u):
        cnx = ConnessioneDB.get_connection()
        if cnx is None:
            raise RuntimeError("Connessione al DB non disponibile")
        else:
            cursor = cnx.cursor()
            query = ("SELECT A.id, A.nome,A.tipologia, A.epoca, A.id_museo "
                     "FROM artefatto A "
                     "JOIN museo M ON A.id_museo = M.id" )
            cursor.execute(query)
            result = []
            for row in cursor:
                artefatto = Artefatto(id = row[0], nome = row[1], tipologia = row[2],
                                      epoca = row[3], id_museo = row[4])
                result.append(artefatto)
            cursor.close()
            cnx.close()
            return result

    #restituisce una lista di artefatti filtrati per epoca e museo
    def get_artefatti_filtrati(self, museo:str, epoca:str):
        cnx = ConnessioneDB.get_connection()
        if cnx is None:
            raise RuntimeError("Connessione al DB non disponibile")
        else:
            cursor = cnx.cursor()
            query = ("SELECT A.id, A.nome, A.tipologia, A.epoca, M.id, M.nome "
                     "FROM artefatto A "
                     "JOIN museo M ON A.id_museo = M.id "
                     "WHERE 1=1")

            # i parametri sono facoltativi, se l'utente li ha inseriti vengono presi in considerazione
            filtri = []
            if museo:
                query += " AND M.nome = %s"
                filtri.append(museo.strip())

            if epoca:
                query += " AND A.epoca = %s"
                filtri.append(epoca.strip())

            cursor.execute(query, filtri)
            rows = cursor.fetchall()
            artefatti = []
            for row in rows:
                artefatto = Artefatto(id = row[0], nome = row[1], tipologia = row[2],
                                      epoca = row[3], id_museo = row[4], nome_museo = row[5])
                artefatti.append(artefatto)
            cursor.close()
            cnx.close()
            return artefatti

#restituisce una lista contenente tutte le epoche
    def get_epoche(self):
        cnx = ConnessioneDB.get_connection()
        if cnx is None:
            raise RuntimeError("Connessione al DB non disponibile")
        else:
            cursor = cnx.cursor()
            query = ('SELECT DISTINCT epoca '
                     'FROM artefatto')
            cursor.execute(query)
            epoche = []
            for row in cursor:
                epoca = row[0]
                epoche.append(epoca)
            cursor.close()
            cnx.close()
            return epoche

    # TODO