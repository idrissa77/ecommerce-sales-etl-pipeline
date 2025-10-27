# 🧩 ETL Pipeline for E-commerce Sales Analysis

## 📊 Business Context
A retail e-commerce company wants to analyze its sales data to identify:
- Best-selling products  
- High-demand periods  
- Emerging trends  

The goal is to centralize all sales data from multiple platforms into a cloud data warehouse for unified analysis and better decision-making.

---

## ⚙️ Technical Overview
This project builds a **complete ETL pipeline** that extracts raw sales data from Kaggle, cleans and transforms it, and loads it into **Snowflake** for analytics.  
The entire workflow is automated and orchestrated with **Apache Airflow**.

### 🪶 Stack
| Layer | Technology | Purpose |
|:------|:------------|:--------|
| Extraction | Python (`requests`, `pandas`) | Fetch data from Kaggle dataset |
| Transformation | Pandas | Cleaning, formatting, deduplication |
| Load | Snowflake | Centralized analytics warehouse |
| Orchestration | Apache Airflow | DAG automation & scheduling |
| Monitoring (in progress) | StatsD → Prometheus → Grafana | Track DAG execution & task duration |

---

## 🚀 Pipeline Steps
1. **Extract**: Read sales dataset from Kaggle  
   Dataset used → [Amazon Sales Dataset](https://www.kaggle.com/datasets/karkavelrajaj/amazon-sales-dataset)  
   (`extract.py`)
2. **Transform**: Clean data (remove nulls, fix formats, deduplicate)  
   (`transform.py`)
3. **Load**: Push transformed data into **Snowflake** for analysis  
   (connection managed via Airflow connection or Snowflake hook)
4. **Orchestrate**: Schedule and monitor ETL workflow using Airflow DAG  
   (`~/airflow/dags/etl_to_snowflake.py`)
5. **Monitor** (in progress): Setup StatsD + Prometheus + Grafana for observability

---

## 🧱 Airflow DAG Structure
