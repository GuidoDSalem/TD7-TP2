import datetime
import random
from faker import Faker
from faker.providers import address, date_time, internet, passport, phone_number
import uuid

from td7.custom_types import Records

PHONE_PROBABILITY = 0.7

class DataGenerator:
    def __init__(self):
        """Instantiates faker instance"""
        self.fake = Faker()
        self.fake.add_provider(address)
        self.fake.add_provider(date_time)
        self.fake.add_provider(internet)
        self.fake.add_provider(phone_number)
    
    def generar_bosques(self, cant_bosques) -> Records:
        return [
             {
                "nombre": f"Bosque {self.fake.unique.word().capitalize()}",
                "superficie": round(random.uniform(1000, 50000), 2)
             } for _ in range(cant_bosques)
        ]
    
    def generar_incendios_forestales(self, bosques: Records, cant_incendios) -> Records:
        incendios = []
        for _ in range(cant_incendios):
            bosque = random.choice(bosques)
            inicio = self.fake.date_time_between(start_date="-1y", end_date="-1w")
            final = inicio + datetime.timedelta(hours=random.randint(1, 156))
            incendios.append({
                "ts_inicio": inicio, "ts_fin": final, "nombre_bosque": bosque["nombre"],
                "estacion": random.choice(["verano", "otoño", "invierno", "primavera"]),
                "hect_quemadas": round(random.uniform(0.5, 1000), 2),
                "latitud_inicio": round(random.uniform(-90, 90), 6),
                "longitud_inicio": round(random.uniform(-180, 180), 6)
            })
            return incendios
        
    def generar_partidos(self, cant_partidos) -> Records:
        return [
            {
                "nombre": self.fake.unique.city(),
                "densidad_poblacional": round(random.uniform(10,1000), 2),
                "superficie_total": round(random.uniform(100, 10000), 2)
            } for _ in range(cant_partidos)
        ]
    
    def generar_estaciones_meteorologicas(self, partidos: Records) -> Records:
        return [
             {
                 "nombre": f"Estacion {i+1}",
                 "nombre_partido": partido["nombre"],
                 "calle": self.fake.street_name(),
                 "numero": self.fake.building_number(),
                 "mail": self.fake.email(),
                 "telefono": self.fake.phone_number()
             }
             for i, partido in enumerate(partidos)
        ]

    def generar_informes_meteorologicos(self, estaciones: Records, n=10) -> Records:
        return [
            {
                "timestamp": self.fake.date_time_between(start_date="-1y", end_date="now"),
                "nombre_estacionMetereologica": est["nombre"],
                "dir_viento": random.choice(["N", "S", "E", "O"]),
                "vel_viento": round(random.uniform(0, 50), 2),
                "precipitacion_6h": round(random.uniform(0, 100), 2),
                "precipitacion12_h": round(random.uniform(0, 200), 2),
                "humedad": round(random.uniform(0, 100), 2),
                "temperatura": round(random.uniform(-10, 40), 2)
            }
            for est in estaciones
            for _ in range(n)
        ]
    
    

# import datetime
# import random
# from faker import Faker
# from faker.providers import address, date_time, internet, passport, phone_number
# import uuid

# from td7.custom_types import Records

# PHONE_PROBABILITY = 0.7

# class DataGenerator:
#     def __init__(self):
#         """Instantiates faker instance"""
#         self.fake = Faker()
#         self.fake.add_provider(address)
#         self.fake.add_provider(date_time)
#         self.fake.add_provider(internet)
#         self.fake.add_provider(phone_number)

#     def generar_bosques(self, n=5) -> Records:
#         return [
#             {
#                 "nombre": f"Bosque {self.fake.unique.word().capitalize()}",
#                 "superficie": round(random.uniform(1000, 50000), 2)
#             } for _ in range(n)
#         ]

#     def generar_afluencias_turisticas(self, bosques: Records, fechas: list[datetime.date]) -> Records:
#         return [
#             {
#                 "fecha": fecha,
#                 "nombre_bosque": bosque["nombre"],
#                 "cant_turistas": random.randint(0, 5000)
#             }
#             for bosque in bosques
#             for fecha in fechas
#         ]

#     def generar_poligonos(self, bosques: Records) -> Records:
#         return [
#             {
#                 "id_poligono": i + 1,
#                 "nombre_bosque": bosque["nombre"]
#             }
#             for i, bosque in enumerate(bosques)
#         ]

#     def generar_coordenadas(self, poligonos: Records, n_coord=5) -> Records:
#         coordenadas = []
#         for poligono in poligonos:
#             for i in range(n_coord):
#                 coordenadas.append({
#                     "latitud": round(random.uniform(-90, 90), 6),
#                     "longitud": round(random.uniform(-180, 180), 6),
#                     "id_poligono": poligono["id_poligono"],
#                     "n_coordenadas": i
#                 })
#         return coordenadas

#     def generar_incendios_forestales(self, bosques: Records, n=5) -> Records:
#         incendios = []
#         for _ in range(n):
#             bosque = random.choice(bosques)
#             start = self.fake.date_time_between(start_date="-1y", end_date="now")
#             end = start + datetime.timedelta(hours=random.randint(1, 72))
#             incendios.append({
#                 "ts_inicio": start,
#                 "ts_fin": end,
#                 "nombre_bosque": bosque["nombre"],
#                 "estacion": random.choice(["verano", "otoño", "invierno", "primavera"]),
#                 "hect_quemadas": round(random.uniform(0.5, 1000), 2),
#                 "latitud_inicio": round(random.uniform(-90, 90), 6),
#                 "longitud_inicio": round(random.uniform(-180, 180), 6)
#             })
#         return incendios

#     def generar_indices_gli(self, bosques: Records, fechas: list[datetime.date]) -> Records:
#         return [
#             {
#                 "fecha": fecha,
#                 "nombre_bosque": bosque["nombre"],
#                 "valor_gli": round(random.uniform(-1, 1), 3),
#                 "valor_rojo": round(random.uniform(0, 1), 3),
#                 "valor_azul": round(random.uniform(0, 1), 3),
#                 "valor_verde": round(random.uniform(0, 1), 3),
#             }
#             for bosque in bosques
#             for fecha in fechas
#         ]

#     def generar_indices_savi(self, bosques: Records, fechas: list[datetime.date]) -> Records:
#         return [
#             {
#                 "fecha": fecha,
#                 "nombre_bosque": bosque["nombre"],
#                 "valor_savi": round(random.uniform(0, 1), 3)
#             }
#             for bosque in bosques
#             for fecha in fechas
#         ]

#     def generar_partidos(self, n=5) -> Records:
#         return [
#             {
#                 "nombre": self.fake.unique.city(),
#                 "densidad_poblacional": round(random.uniform(10, 1000), 2),
#                 "superficie_total": round(random.uniform(100, 10000), 2)
#             } for _ in range(n)
#         ]

#     def generar_bosques_en_partidos(self, bosques: Records, partidos: Records) -> Records:
#         return [
#             {
#                 "nombre_bosque": bosque["nombre"],
#                 "nombre_partido": random.choice(partidos)["nombre"]
#             }
#             for bosque in bosques
#         ]


#     def generar_comportamientos_incendios(self, incendios: Records, informes: Records) -> Records:
#         comportamientos = []
#         for incendio in incendios:
#             for _ in range(2):
#                 dia = incendio["ts_inicio"].date()
#                 hora = self.fake.time()
#                 informe = random.choice(informes)
#                 comportamientos.append({
#                     "nombre_bosque": incendio["nombre_bosque"],
#                     "inicio_incendio": incendio["ts_inicio"],
#                     "dia": dia,
#                     "hora": hora,
#                     "longitud_llamas": round(random.uniform(1, 10), 2),
#                     "altura_llamas": round(random.uniform(1, 5), 2),
#                     "humedad_comb_FFMC": round(random.uniform(0, 100), 2),
#                     "humedad_comb_DMC": round(random.uniform(0, 100), 2),
#                     "humedad_comb_DC": round(random.uniform(0, 100), 2),
#                     "timestamp_informeMeteorologico": informe["timestamp"],
#                     "nombre_estacionMetereologica": informe["nombre_estacionMetereologica"]
#                 })
#         return comportamientos

#     def generar_bomberos(self, partidos: Records) -> Records:
#         return [
#             {
#                 "nro_brigada": i+1,
#                 "nombre_partido": partido["nombre"],
#                 "tipo": random.choice(["oficial", "voluntario"]),
#                 "cantidad_bomberos": random.randint(5, 100)
#             }
#             for i, partido in enumerate(partidos)
#         ]

#     def generar_bomberos_en_incendios(self, brigadas: Records, incendios: Records) -> Records:
#         return [
#             {
#                 "nro_brigada": brigada["nro_brigada"],
#                 "nombre_bosque": incendio["nombre_bosque"],
#                 "inicio_incendio": incendio["ts_inicio"]
#             }
#             for brigada in brigadas
#             for incendio in random.sample(incendios, k=min(2, len(incendios)))
#         ]

#     def generar_recursos(self) -> Records:
#         tipos = ["agua", "helicóptero", "pala", "manguera", "brigadista"]
#         return [
#             {
#                 "nombre": t.capitalize(),
#                 "tipo": "material" if t != "brigadista" else "humano",
#                 "descripcion": f"Recurso tipo {t}"
#             }
#             for t in tipos
#         ]

#     def generar_recursos_utilizados(self, recursos: Records, incendios: Records) -> Records:
#         return [
#             {
#                 "nombre_recurso": recurso["nombre"],
#                 "nombre_bosque": incendio["nombre_bosque"],
#                 "inicio_incendio": incendio["ts_inicio"],
#                 "cantidad": random.randint(1, 10)
#             }
#             for recurso in recursos
#             for incendio in random.sample(incendios, k=min(2, len(incendios)))
#         ]

#     def generar_tacticas(self) -> Records:
#         nombres = ["Ataque directo", "Ataque indirecto", "Monitoreo", "Enfriamiento"]
#         return [
#             {
#                 "nombre": n,
#                 "descripcion": f"Descripción de {n}"
#             } for n in nombres
#         ]

#     def generar_tacticas_utilizadas(self, tacticas: Records, incendios: Records) -> Records:
#         return [
#             {
#                 "nombre_tactica": tactica["nombre"],
#                 "nombre_bosque": incendio["nombre_bosque"],
#                 "inicio_incendio": incendio["ts_inicio"]
#             }
#             for tactica in tacticas
#             for incendio in random.sample(incendios, k=min(2, len(incendios)))
#         ]

#     def generar_causas(self) -> Records:
#         nombres = ["Rayo", "Quema intencional", "Accidente", "Fogata"]
#         return [
#             {
#                 "nombre": n,
#                 "tipo": "natural" if n == "Rayo" else "artificial",
#                 "descripcion": f"Causa del incendio: {n}"
#             } for n in nombres
#         ]

#     def generar_causas_incendios(self, causas: Records, incendios: Records) -> Records:
#         return [
#             {
#                 "nombre_causa": random.choice(causas)["nombre"],
#                 "nombre_bosque": incendio["nombre_bosque"],
#                 "inicio_incendio": incendio["ts_inicio"]
#             }
#             for incendio in incendios
#         ]