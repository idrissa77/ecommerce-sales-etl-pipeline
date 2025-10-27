# ETL Pipeline — Amazon Sales (Airflow + Snowflake)

# Business Context
A retail e-commerce company wants to analyze its sales data to identify top-selling products, peak demand periods, and emerging trends. Centralizing all data from website, physical stores, and social media into a single warehouse enables better decision-making.

# Technical Context
This project builds an ETL pipeline that extracts raw sales data from multiple sources, transforms it (cleaning, enrichment, aggregation), and loads it into a Snowflake warehouse for analysis. The workflow is automated and orchestrated with Apache Airflow.

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

