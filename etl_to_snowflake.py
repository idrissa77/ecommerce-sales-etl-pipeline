# DAG to orchestrate Amazon ETL -> Snowflake
# File ~/airflow/dags/etl_to_snowflake.py 
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.snowflake.operators.snowflake import SnowflakeOperator
from datetime import datetime
import subprocess
import warnings
from sqlalchemy.exc import SAWarning

warnings.filterwarnings("ignore", category=SAWarning, message=".*flatten.*")


# Paths to your scripts
EXTRACT_SCRIPT = "/home/idrissa/airflow/scripts/extract.py"
TRANSFORM_SCRIPT = "/home/idrissa/airflow/scripts/transform.py"

# Python functions for Airflow
def run_extract():
    subprocess.run(["python3", EXTRACT_SCRIPT], check=True)

def run_transform():
    subprocess.run(["python3", TRANSFORM_SCRIPT], check=True)

# DAG definition
with DAG(
    dag_id="etl_amazon_snowflake",
    start_date=datetime(2025, 10, 23),
    schedule_interval="0 3 * * 1",  # run every Monday at 3 AM
) as dag:

    extract_task = PythonOperator(
        task_id="extract_data",
        python_callable=run_extract
    )

    transform_task = PythonOperator(
        task_id="transform_data",
        python_callable=run_transform
    )

    # Example task to load data into Snowflake
    load_task = SnowflakeOperator(
        task_id="load_to_snowflake",
        snowflake_conn_id="snowflake_conn",
        sql="""
        USE DATABASE AMAZON;
        USE SCHEMA PUBLIC;
        PUT file:///mnt/c/Users/idris/OneDrive/Desktop/Amazon_sales_data/amazon_clean.csv @%PRODUCTS;
        COPY INTO PRODUCTS
        FILE_FORMAT = (TYPE = 'CSV' FIELD_OPTIONALLY_ENCLOSED_BY='"' SKIP_HEADER=1);
        """,
    )

    # Set task execution order
    extract_task >> transform_task >> load_task