import datetime
import random
from faker import Faker
from faker.providers import address, date_time, internet, passport, phone_number
import uuid

from custom_types import Records

PHONE_PROBABILITY = 0.7


class DataGenerator:
    def __init__(self):
        """Instantiates faker instance"""
        self.fake = Faker()
        self.fake.add_provider(address)
        self.fake.add_provider(date_time)
        self.fake.add_provider(internet)
        self.fake.add_provider(passport)
        self.fake.add_provider(phone_number)

    # --- 1. Datos Meteorológicos ---
    def generar_datos_meteorologicos(self):
        return {
            "estacion": self.fake.city(),
            "timestamp": self.fake.date_time_this_year(),
            "temperatura": round(random.uniform(10, 45), 1),  # °C
            "humedad": random.randint(20, 90),  # %
            "direccion_viento": self.fake.random_element(["N", "NE", "E", "SE", "S", "SO", "O", "NO"]),
            "velocidad_viento_kmh": round(random.uniform(5, 60), 1),
            "precipitacion_6h_mm": round(random.uniform(0, 30), 1),
            "precipitacion_12h_mm": round(random.uniform(0, 60), 1)
        }
    
    # --- 2. Reporte de Incendios ---
    def generar_reporte_incendio(self):
        superficie = round(random.uniform(0.1, 500), 2)
        return {
            "id_incendio": str(uuid.uuid4()),
            "fecha": self.fake.date_between(start_date='-1y', end_date='today'),
            "hora": self.fake.time(),
            "localidad": self.fake.city(),
            "estacion_del_anio": self.fake.random_element(["Verano", "Otoño", "Invierno", "Primavera"]),
            "franja_horaria": self.fake.random_element(["Madrugada", "Mañana", "Tarde", "Noche"]),
            "hectareas_quemadas": superficie,
            "tactica_usada": self.fake.random_element(["Ataque directo", "Ataque indirecto", "Uso de agua", "Uso de tierra"]),
            "dotacion": self.fake.random_element(["Bomberos oficiales", "Voluntarios"]),
            "recursos": {
                "personas": random.randint(5, 40),
                "camiones": random.randint(1, 5),
                "helicopteros": random.randint(0, 2)
            }
        }
    
    # --- 3. Índices de vegetación ---
    def generar_indices_vegetacion(self):
        return {
            "bosque_id": str(uuid.uuid4()),
            "indice_SAVI": round(random.uniform(0.0, 1.0), 3),
            "indice_GLI": {
                "R": random.randint(0, 255),
                "G": random.randint(0, 255),
                "B": random.randint(0, 255)
            }
        }
    
    # --- 4. Datos sociales (turismo y densidad) ---
    def generar_datos_sociales(self):
        return {
            "zona": self.fake.city(),
            "afluencia_turistica_mensual": random.randint(500, 20000),
            "densidad_poblacional_hab_km2": round(random.uniform(10, 500), 1)
        }   
            
    def generate_people(self, n: int) -> Records:
        """Generates n people.

        Parameters
        ----------
        n : int
            Number of people to generate.

        Returns
        -------
        List[Dict[str, Any]]
            List of dicts that include first_name, last_name, phone_number,
            address, country, date_of_birth, passport_number and email.

        Notes
        -----
        People are guaranteed to be unique only within a function call.
        """
        people = []
        for _ in range(n):
            people.append(
                {
                    "first_name": self.fake.unique.first_name(),
                    "last_name": self.fake.unique.last_name(),
                    "phone_number": self.fake.unique.phone_number(),
                    "address": self.fake.unique.address(),
                    "country": self.fake.unique.country(),
                    "date_of_birth": self.fake.unique.date_of_birth(),
                    "passport_number": self.fake.unique.passport_number(),
                    "email": self.fake.unique.ascii_email(),
                }
            )
        return people

    def generate_sessions(
        self,
        people: list,
        base_time: datetime.datetime,
        window: datetime.timedelta,
        n: int,
    ) -> Records:
        """Generates sessions for people.

        Parameters
        ----------
        people : list
            People to generate events for.
        base_time : datetime.datetime
            Base time for sessions.
        window : datetime.timedelta
            Time window for sessions. Events will fill
            the whole window equidistantly.
        n : int
            Number of events to generate.

        Returns
        -------
        List[Dict[str, Any]]
            List of dicts for events including properties such as
            person_passport_number, event_time, user_agent, session_id.

        Notes
        -----
        Events can be considered to be unique across function calls
        since a surrogate key is generated using UUID4.
        """
        sessions = []
        frequency = window / n
        for i in range(n):
            person = people[random.randint(0, len(people)-1)]
            if random.random() < PHONE_PROBABILITY:
                useragent = self.fake.android_platform_token()
            else:
                useragent = self.fake.chrome()

            sessions.append(
                {
                    "person_passport_number": person["passport_number"],
                    "event_time": base_time + i * frequency,
                    "user_agent": useragent,
                    "session_id": str(uuid.uuid4()),
                }
            )
        return sessions
    
        # --- Ejemplo de generación múltiple ---
    def generar_datos(self,n=5):
        for i in range(n):
            print("=== Meteorología ===")
            print(self.generar_datos_meteorologicos())
            print("=== Incendio ===")
            print(self.generar_reporte_incendio())
            print("=== Vegetación ===")
            print(self.generar_indices_vegetacion())
            print("=== Sociales ===")
            print(self.generar_datos_sociales())
            print("\n------------------\n")
            print("=== Personas ===")
            personas = self.generate_people(5)
            for persona in personas:
                print(persona)
            print("=== Sesiones ===")
            base_time = datetime.datetime.now()
            window = datetime.timedelta(days=1)
            sesiones = self.generate_sessions(personas, base_time, window, 10)
            for sesion in sesiones:
                print(sesion)
    
    





# Ejecutar ejemplo
if __name__ == "__main__":
    
    data_generator = DataGenerator()
    # Generar 3 conjuntos de datos
    data_generator.generar_datos(3)

