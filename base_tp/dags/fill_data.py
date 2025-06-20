from airflow import DAG
from airflow.operators.python import PythonOperator
import pendulum
import datetime
from td7.data_generator import DataGenerator
from td7.schema import Schema

EVENTS_PER_DAY = 10_000


def generate_data(base_time: str, n: int):
    """Generates synth data and saves to DB.

    Parameters
    ----------
    base_time: strpoetry export --without-hashes --format=requirements.txt > requirements.txt

        Base datetime to start events from.
    n : int
        Number of events to generate.
    """
    





with DAG(
    "fill_data",
    start_date=pendulum.datetime(2024, 6, 1, tz="UTC"),
    schedule_interval="@hourly",
    catchup=True,
) as dag:
    op = PythonOperator(
        task_id="task",
        python_callable=generate_data,
        op_kwargs=dict(n=EVENTS_PER_DAY, base_time="{{ ds }}"),
    )
    
    generator = DataGenerator()
    schema = Schema()
    
    def crear_estaciones():
        estaciones = generator.generate_estaciones(5)
        schema.insert(estaciones, "estacion_meteorologica")

    def generar_informes(base_time: str):
        estaciones = schema.get_estaciones()  # trae IDs de estaciones existentes
        informes = generator.generate_informes_meteorologicos(
            estaciones,
            datetime.fromisoformat(base_time)
        )
        schema.insert(informes, "informe_meteorologico")

    def generar_incendios(base_time: str):
        bosques = schema.get_bosques()
        incendios = generator.generate_incendios_forestales(
            bosques,
            datetime.fromisoformat(base_time)
        )
        schema.insert(incendios, "incendio_forestal")

    def generar_recursos():
        incendios = schema.get_incendios_activos()
        recursos = generator.generate_recursos(incendios)
        schema.insert(recursos, "recurso")

    def generar_brigadas():
        incendios = schema.get_incendios_activos()
        brigadas = generator.generate_brigadas(incendios)
        schema.insert(brigadas, "brigada_bomberos")


    t1 = PythonOperator(
        task_id="crear_estaciones",
        python_callable=crear_estaciones
    )

    t2 = PythonOperator(
        task_id="generar_informes_meteorologicos",
        python_callable=generar_informes,
        op_kwargs={"base_time": "{{ ds }}"}
    )

    t3 = PythonOperator(
        task_id="generar_incendios",
        python_callable=generar_incendios,
        op_kwargs={"base_time": "{{ ds }}"}
    )

    t4a = PythonOperator(
        task_id="generar_recursos",
        python_callable=generar_recursos
    )

    t4b = PythonOperator(
        task_id="generar_brigadas",
        python_callable=generar_brigadas
    )

    # Definición del flujo
    t1 >> t2 >> t3 >> [t4a, t4b]