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