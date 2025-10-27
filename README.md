# ETL Pipeline — Amazon Sales (Airflow + Snowflake)

End-to-end ETL from Kaggle to Snowflake. Orchestrated with Airflow.

## Repo structure

## 📂 Repo Structure

```text
📂 airflow/
├── dags/
│ └── etl_to_snowflake.py
└── scripts/
├── extract.py
└── transform.py
```

## Quick facts
- Source data: Kaggle — Amazon Sales Dataset.  
- Local flow: run `extract.py` and `transform.py` on Windows to produce `amazon_clean.csv`.  
- Load: Airflow (WSL2) runs `etl_to_snowflake` DAG which uploads `amazon_clean.csv` into Snowflake table `PRODUCTS`.  
- Schedule: weekly, Monday 03:00 (CRON `0 3 * * 1`).  
- Monitoring: Prometheus config at `~/airflow/prometheus.yml` (statsd exporter + Grafana planned). Mapping stage pending.

## How to run 
1. On Windows: run  
   ```bash
   python extract.py
   python transform.py
=> produces amazon_clean.csv.
2. On WSL2 (Airflow): place DAG at ~/airflow/dags/etl_to_snowflake.py, ensure Airflow connection snowflake_conn is set, then start scheduler and webserver. DAG will run and load into Snowflake.

Expected result
PRODUCTS table populated in Snowflake with cleaned sales data ready for BI.

Next steps 
Finalize StatsD → Prometheus mapping.

Build Grafana dashboards for DAG health, task duration, failures.

