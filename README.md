# Insurance Claims Data Pipeline - End-to-End AWS ETL Project

[![AWS](https://img.shields.io/badge/AWS-Cloud-orange)](https://aws.amazon.com/)
[![Python](https://img.shields.io/badge/Python-3.10-blue)](https://python.org)
[![Lambda](https://img.shields.io/badge/AWS-Lambda-yellow)](https://aws.amazon.com/lambda/)
[![S3](https://img.shields.io/badge/AWS-S3-green)](https://aws.amazon.com/s3/)
[![Glue](https://img.shields.io/badge/AWS-Glue-purple)](https://aws.amazon.com/glue/)
[![Athena](https://img.shields.io/badge/AWS-Athena-red)](https://aws.amazon.com/athena/)

## 🎯 Project Overview

A **production-ready, serverless ETL pipeline** that processes insurance claims data and transforms it into analytics-ready tables for business intelligence. This project demonstrates enterprise-level data engineering skills using AWS cloud services.

### 🚀 **Live Demo & Results**
- **Data Processed**: 1.3K+ insurance records
- **Processing Time**: <30 seconds end-to-end
- **Tables Generated**: 3 structured analytics tables
- **Monthly Cost**: <$3 (AWS free tier friendly)

---

## 🏗️ **Solution Architecture**
![Insurance ETL Pipeline Architecture](Project_Architecture.jpg)
---

## 🎯 **Business Objectives**

### **Primary Goals:**
- **Claims Analysis**: Identify patterns in claim frequency and amounts
- **Risk Assessment**: Analyze claim trends by demographics and policy types
- **Fraud Detection**: Detect anomalies in claim patterns
- **Customer Segmentation**: Group customers by claim behavior
- **Operational Efficiency**: Track processing times and bottlenecks

### **Technical Objectives:**
- Build **scalable, serverless** ETL pipeline
- Implement **event-driven architecture**
- Create **analytics-ready data warehouse**
- Demonstrate **AWS cloud expertise**

---

## 🛠️ **Technology Stack**

### **AWS Services:**
| Service | Purpose | Why Chosen |
|---------|---------|------------|
| **AWS Lambda** | Serverless compute for ETL | Cost-effective, auto-scaling |
| **Amazon S3** | Data lake storage | Unlimited storage, high durability |
| **AWS Glue** | Data cataloging & schema | Managed metadata store |
| **Amazon Athena** | SQL analytics | Serverless querying |
| **EventBridge** | Scheduling & orchestration | Event-driven automation |

### **Programming & Tools:**
- **Python 3.10** - Core programming language
- **boto3** - AWS SDK for Python
- **Built-in libraries** - No external dependencies
- **HTTP/REST** - Data source integration

---

## 📊 **Data Pipeline Flow**

### **Stage 1: Data Extraction**
```python
# Lambda 1: HTTP Data Extraction
HTTP Source → CSV Download → JSON Conversion → S3 Raw Storage
```
- **Source**: Public insurance dataset (1.3K+ records)
- **Format**: CSV → JSON transformation
- **Storage**: S3 data lake (raw_data/to_processed/)
- **Trigger**: EventBridge daily schedule

### **Stage 2: Data Transformation**
```python
# Lambda 2: Event-Driven Transformation
S3 Event → JSON Processing → 3 Table Creation → CSV Output
```
- **Input**: Raw JSON insurance data
- **Processing**: Split into Policy, Claims, Customer entities
- **Output**: 3 structured CSV files
- **Storage**: S3 data lake (transformed_data/)

### **Stage 3: Data Cataloging**
```sql
-- Glue Crawlers: Schema Discovery
Raw Data → Schema Inference → Glue Catalog → Athena Tables
```
- **Crawlers**: 3 automated schema discoverers
- **Catalog**: AWS Glue Data Catalog
- **Tables**: policy_data, claims_data, customer_data

---

## 📈 **Data Model**

### **Policy Table**
| Column | Type | Description |
|--------|------|-------------|
| policy_id | STRING | Unique policy identifier |
| customer_age | INT | Customer age |
| gender | STRING | Customer gender |
| region | STRING | Geographic region |
| premium_amount | DECIMAL | Annual premium |

### **Claims Table**
| Column | Type | Description |
|--------|------|-------------|
| claim_id | STRING | Unique claim identifier |
| policy_id | STRING | Related policy |
| claim_amount | DECIMAL | Claim value |
| bmi | DECIMAL | Customer BMI |
| smoker | STRING | Smoking status |

### **Customer Table**
| Column | Type | Description |
|--------|------|-------------|
| customer_id | STRING | Unique customer identifier |
| policy_id | STRING | Related policy |
| age | INT | Customer age |
| gender | STRING | Customer gender |
| children | INT | Number of dependents |
| smoker | STRING | Smoking status |
| region | STRING | Geographic region |

---

## 📊 **Sample Analytics Queries**

### **Claims Analysis by Smoking Status**
```sql
SELECT 
    smoker,
    COUNT(*) as total_claims,
    AVG(CAST(claim_amount AS DOUBLE)) as avg_claim_amount,
    MAX(CAST(claim_amount AS DOUBLE)) as max_claim_amount
FROM claims_data 
GROUP BY smoker
ORDER BY avg_claim_amount DESC;
```

## 🔧 **Troubleshooting Guide**

### **Common Issues & Solutions**

#### **Lambda Function Errors**
| Error | Cause | Solution |
|-------|-------|----------|
| `Timeout` | Function exceeds time limit | Increase timeout to 5-10 minutes |
| `Memory exceeded` | Insufficient memory allocation | Increase memory to 512MB+ |
| `Import error` | Missing dependencies | Use built-in Python libraries only |

#### **S3 Issues**
| Error | Cause | Solution |
|-------|-------|----------|
| `Access Denied` | Insufficient IAM permissions | Add S3FullAccess to Lambda role |
| `Bucket not found` | Incorrect bucket name | Verify bucket name in code |
| `Trigger not working` | S3 event configuration | Check prefix/suffix settings |

#### **Glue Crawler Issues**
| Error | Cause | Solution |
|-------|-------|----------|
| `No tables created` | No data in S3 path | Run Lambda functions first |
| `Schema errors` | Malformed CSV data | Check CSV format and headers |
| `Permission denied` | IAM role missing | Add S3 read permissions to Glue role |

## 📈 **Performance Metrics**

### **Pipeline Performance**
- **Data Volume**: 1,338 records processed
- **Processing Time**: 15-30 seconds end-to-end
- **Throughput**: ~45 records/second
- **Availability**: 99.9% (AWS Lambda SLA)

### **Cost Analysis**
| Service | Monthly Cost | Usage |
|---------|-------------|-------|
| Lambda | $0.00 | <1M requests (free tier) |
| S3 | $0.50 | ~100MB storage |
| Glue | $1.00 | 3 crawler runs/month |
| Athena | $0.50 | ~10GB queried |
| **Total** | **~$2.00** | Light usage |

---

## 🔮 **Future Improvements**

### **Phase 2 Enhancements**
- [ ] **Real-time Processing**: Implement Kinesis for streaming data
- [ ] **Data Quality**: Add Great Expectations for data validation
- [ ] **Monitoring**: CloudWatch dashboards and alerts
- [ ] **CI/CD**: GitHub Actions for automated deployment
- [ ] **Security**: Implement data encryption and VPC endpoints

---

## 📚 **Learning Resources**

### **AWS Documentation**
- [AWS Lambda Developer Guide](https://docs.aws.amazon.com/lambda/)
- [Amazon S3 User Guide](https://docs.aws.amazon.com/s3/)
- [AWS Glue Developer Guide](https://docs.aws.amazon.com/glue/)
- [Amazon Athena User Guide](https://docs.aws.amazon.com/athena/)
