from typing import Optional
from td7.custom_types import Records
from td7.database import Database

class Schema:
    def __init__(self):
        self.db = Database()
    
    def get_bosques(self) -> Records:
        return self.db.run_select("SELECT * FROM Bosques")

    def get_afluencias(self, nombre_bosque: str) -> Records:
        query = "SELECT * FROM AfluenciasTuristicas"
        if nombre_bosque:
            query += f" WHERE nombre_bosque = '{nombre_bosque}'"
        return self.db.run_select(query)

    def get_incendios(self) -> Records:
        return self.db.run_select("SELECT * FROM IncendiosForestales ORDER BY ts_inicio DESC")
    
    def get_estaciones(self) -> Records:
        return self.db.run_select("SELECT * FROM EstacionesMetereologicas")
    
    def get_informes_meteorologicos(self, desde: str) -> Records:
        query = "SELECT * FROM InformesMetereologicos"
        if desde:
            query += f" WHERE timestamp >= '{desde}'"
        return self.db.run_select(query)

    def get_indices_gli(self, nombre_bosque: str) -> Records:
        query = "SELECT * FROM IndicesGLI"
        if nombre_bosque:
            query += f" WHERE nombre_bosque = '{nombre_bosque}'"
        return self.db.run_select(query)

    def get_indices_savi(self, nombre_bosque: str) -> Records:
        query = "SELECT * FROM IndicesSAVI"
        if nombre_bosque:
            query += f" WHERE nombre_bosque = '{nombre_bosque}'"
        return self.db.run_select(query)
    
    def get_comportamientos_incendios(self, nombre_bosque: str) -> Records:
        query = "SELECT * FROM ComportamientosIncendios"
        if nombre_bosque:
            query += f" WHERE nombre_bosque = '{nombre_bosque}'"
        return self.db.run_select(query)

    def get_recursos_utilizados(self) -> Records:
        return self.db.run_select("SELECT * FROM RecursosUtilizadosEnIncendios")
    
    def get_tacticas_utilizadas(self) -> Records:
        return self.db.run_select("SELECT * FROM TacticasUtilizadasEnIncendios")

    def get_causas_incendios(self) -> Records:
        return self.db.run_select("SELECT * FROM CausasIncendios")

    def get_bomberos(self) -> Records:
        return self.db.run_select("SELECT * FROM Bomberos")
    
    def get_partidos(self) -> Records:
        return self.db.run_select("SELECT * FROM Partidos")

    def insert(self, records: Records, table: str):
        self.db.run_insert(records, table)
