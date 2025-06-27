from airflow import DAG
from airflow.operators.python import PythonOperator
import pendulum
import datetime
import random

from td7.data_generator import DataGenerator
from td7.schema import Schema

generator = DataGenerator()
schema = Schema()

with DAG(
    dag_id="dag_carga_datos",
    start_date=pendulum.datetime(2025, 6, 1, tz="UTC"),
    schedule_interval="@hourly",
    catchup=True,
) as dag:

    def generar_partidos():
        partidos = generator.generar_partidos(5)
        schema.insert(partidos, "partidos")

    def generar_bosques():
        bosques = generator.generar_bosques(5)
        schema.insert(bosques, "bosques")

    def generar_bosquesenpartido():
        partidos = schema.get_partidos()
        bosques = schema.get_bosques()

        ubicacionbosques = []
        for bosque in bosques:
            partido = random.choice(partidos)
            ubicacionbosques.append({
                "nombre_bosque": bosque["nombre"],
                "nombre_partido": partido["nombre"]
        })
        schema.insert(ubicacionbosques, "bosquesenpartidos")

    def generar_estaciones():
        partidos = schema.get_partidos()
        estaciones = generator.generar_estaciones_meteorologicas(partidos)
        schema.insert(estaciones, "estacionesmetereologicas")

    def generar_informes():
        estaciones = schema.get_estaciones()
        informes = generator.generar_informes_meteorologicos(estaciones, 10)
        schema.insert(informes, "informesmetereologicos")

    def generar_incendios():
        bosques = schema.get_bosques()
        incendios = generator.generar_incendios_forestales(bosques, 5)
        schema.insert(incendios, "incendiosforestales")
    

    t1 = PythonOperator(task_id="partidos", python_callable=generar_partidos)
    t2 = PythonOperator(task_id="bosques", python_callable=generar_bosques)
    t3 = PythonOperator(task_id="ubicacionbosques", python_callable=generar_bosquesenpartido)
    t4 = PythonOperator(task_id="estaciones", python_callable=generar_estaciones)
    t5 = PythonOperator(task_id="informes", python_callable=generar_informes, op_kwargs={"base_time": "{{ ds }}"})
    t6 = PythonOperator(task_id="incendios", python_callable=generar_incendios, op_kwargs={"base_time": "{{ ds }}"})

    t1 >> [t3, t4]
    t2 >> [t3, t6]
    t4 >> t5




# from airflow import DAG
# from airflow.operators.python import PythonOperator
# import pendulum
# import datetime

# from td7.data_generator import DataGenerator
# from td7.schema import Schema

# generator = DataGenerator()
# schema = Schema()

# with DAG(
#     dag_id="cargar_datos_incendios",
#     start_date=pendulum.datetime(2024, 6, 1, tz="UTC"),
#     schedule_interval="@hourly",
#     catchup=True,
# ) as dag:

#     def generar_partidos():
#         partidos = generator.generar_partidos(5)
#         schema.insert(partidos, "Partidos")

#     def generar_bosques():
#         bosques = generator.generar_bosques(5)
#         schema.insert(bosques, "Bosques")

#     def crear_estaciones():
#         partidos = schema.get_partidos()
#         estaciones = generator.generar_estaciones_metereologicas(partidos)
#         schema.insert(estaciones, "EstacionesMetereologicas")

#     def generar_recursos():
#         recursos = generator.generar_recursos()
#         schema.insert(recursos, "Recursos")

#     def generar_tacticas():
#         tacticas = generator.generar_tacticas()
#         schema.insert(tacticas, "Tacticas")

#     def generar_causas():
#         causas = generator.generar_causas()
#         schema.insert(causas, "Causas")

#     def generar_bomberos():
#         partidos = schema.get_partidos()
#         brigadas = generator.generar_bomberos(partidos)
#         schema.insert(brigadas, "Bomberos")

#     def generar_informes(base_time: str):
#         estaciones = schema.get_estaciones()
#         informes = generator.generar_informes_metereologicos(
#             estaciones,
#             datetime.datetime.fromisoformat(base_time)
#         )
#         schema.insert(informes, "InformesMetereologicos")

#     def generar_incendios(base_time: str):
#         bosques = schema.get_bosques()
#         incendios = generator.generar_incendios_forestales(
#             bosques,
#             datetime.datetime.fromisoformat(base_time)
#         )
#         schema.insert(incendios, "IncendiosForestales")

#     # Tareas base
#     t0a = PythonOperator(task_id="partidos", python_callable=generar_partidos)
#     t0b = PythonOperator(task_id="bosques", python_callable=generar_bosques)

#     # Catálogos y dependencias básicas
#     t1 = PythonOperator(task_id="estaciones", python_callable=crear_estaciones)
#     t2 = PythonOperator(task_id="recursos", python_callable=generar_recursos)
#     t3 = PythonOperator(task_id="tacticas", python_callable=generar_tacticas)
#     t4 = PythonOperator(task_id="causas", python_callable=generar_causas)
#     t5 = PythonOperator(task_id="bomberos", python_callable=generar_bomberos)

#     # Datos con fecha dinámica
#     t6 = PythonOperator(
#         task_id="informes",
#         python_callable=generar_informes,
#         op_kwargs={"base_time": "{{ ds }}"}
#     )
#     t7 = PythonOperator(
#         task_id="incendios",
#         python_callable=generar_incendios,
#         op_kwargs={"base_time": "{{ ds }}"}
#     )

#     # Dependencias
#     t0a >> [t1, t5]
#     t0b >> t7
#     [t1] >> t6
