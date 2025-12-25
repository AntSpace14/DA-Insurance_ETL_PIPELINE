# 🚀 Insurance ETL Data Pipeline – Serverless, Automated, Production-Ready

A fully-automated, end-to-end **serverless ETL pipeline** that extracts insurance data from an HTTP source, transforms it into structured analytical tables, and loads it into a centralized AWS Data Lake with Glue + Athena integration.

This project demonstrates **modern data engineering techniques** using **pure Python**, **AWS Lambda**, **S3**, **EventBridge**, **Glue Crawlers**, and **Athena**—without any external packages, without layers, and with guaranteed zero deployment errors.

---

## 🏗️ Architecture Overview

EventBridge (Daily Schedule)
│
▼
Lambda → Extract Data → S3 (raw_data/to_processed/)
│
S3 Event Trigger (ObjectCreated)
▼
Lambda → Transform Data → S3 (transformed_data)
▼
AWS Glue Data Catalog
▼
Amazon Athena (SQL Analytics)



---

## 🎯 Project Goals

- Extract publicly available insurance dataset via HTTP  
- Load raw data into Amazon S3 with controlled folder hierarchy  
- Transform into **Policy**, **Claims**, and **Customer** analytical tables  
- Automatically trigger downstream transformations  
- Catalog datasets using AWS Glue Crawlers  
- Run SQL analytics on Athena  
- Zero dependencies, zero layers, no external services  

---

## 📁 Data Lake Structure (S3)

insurance-etl-datalake-<your-name>/
│
├── raw_data/
│ ├── to_processed/
│ └── processed/
│
└── transformed_data/
├── policy_data/
├── claims_data/
└── customer_data/

yaml
Copy code

---

# ⚙️ 1. Data Extraction – Lambda Function

**Purpose:**  
Fetches the dataset from an HTTP source, converts it to JSON, and stores it inside:

raw_data/to_processed/

markdown
Copy code

**Trigger:**  
Daily schedule using **EventBridge**.

### Features
- Pure Python (no pandas)
- Uses built-in `urllib.request`
- Generates timestamped JSON files

---

# 🧪 2. Data Transformation – Lambda Function

**Purpose:**  
Transforms raw JSON into structured datasets:

- `policy_data`
- `claims_data`
- `customer_data`

**Trigger:**  
S3 → `ObjectCreated` event on:

raw_data/to_processed/

yaml
Copy code

### Features

- Pure Python transformations  
- Generates cleaned CSV files  
- Moves processed raw files → `processed/`  
- Stores transformed outputs in `transformed_data/` folders  

---

# 🕒 3. Orchestration – EventBridge

A scheduled EventBridge rule:

rate(1 day)

yaml
Copy code

Triggers the **data extraction Lambda** automatically.

---

# 🧭 4. Schema Management – AWS Glue Crawlers

Three crawlers were configured:

| Crawler Name            | S3 Path                                      |
|-------------------------|-----------------------------------------------|
| policy-data-crawler     | transformed_data/policy_data/                 |
| claims-data-crawler     | transformed_data/claims_data/                 |
| customer-data-crawler   | transformed_data/customer_data/               |

All crawlers write to the **Glue Data Catalog** under:

insurance_analytics_db

yaml
Copy code

---

# 📊 5. SQL Analytics – Amazon Athena

Example queries:

```sql
SELECT * FROM policy_data LIMIT 10;

SELECT smoker, COUNT(*) AS total_claims
FROM claims_data
GROUP BY smoker
ORDER BY total_claims DESC;
sql
Copy code
SELECT gender, region, AVG(CAST(age AS INT)) AS avg_age
FROM customer_data
GROUP BY gender, region;
📌 Technologies Used
Category	Tools
Compute	AWS Lambda (Python 3.10)
Storage	Amazon S3 (Data Lake)
Orchestration	Amazon EventBridge
Cataloging	AWS Glue + Crawlers
Query Engine	Amazon Athena
Language	Python (Standard Library Only)

🏆 Key Achievements
Designed a fully serverless ETL pipeline on AWS

Automated ingestion & transformation of 1,300+ insurance records

Built a scalable S3 Data Lake with raw, processed, and curated layers

Produced structured analytical tables (Policy, Claims, Customer)

Implemented event-driven orchestration using Lambda + S3 triggers

Enabled BI-ready querying using Athena SQL on S3

Zero Lambda layers, zero external dependencies, 100% AWS-native

📈 End-to-End Output
After executing the pipeline, the system produces:

✔️ Structured datasets
policy_transformed_*.csv

claims_transformed_*.csv

customer_transformed_*.csv

✔️ Glue Catalog tables
policy_data

claims_data

customer_data

✔️ Athena SQL workspace
Query-ready dataset for analytics and BI workloads.
