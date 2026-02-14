End-to-End Spotify Azure Lakehouse Data Engineering Project
📌 Project Overview

This project demonstrates a complete end-to-end Azure Lakehouse Data Engineering solution built using Azure-native services and Databricks. It covers data ingestion, transformation, dimensional modeling, streaming, and analytics-ready data delivery using modern data engineering best practices.
The solution follows the Medallion Architecture (Bronze, Silver, Gold) and implements incremental processing, Slowly Changing Dimensions (SCD), and scalable Spark transformations.

🛠️ Tech Stack

Azure Data Factory (ADF) – Orchestration & ingestion

Azure SQL Database – Source system

Azure Data Lake Storage Gen2 (ADLS Gen2) – Data storage

Azure Databricks – Data processing

Unity Catalog – Data governance

Delta Lake / Delta Live Tables – Data reliability & pipeline management

Spark Streaming (Auto Loader) – Incremental & streaming ingestion

PySpark – Data transformations

GitHub – Version control


🏗️ Architecture Overview:
1️⃣ Data Ingestion Layer (Bronze)

Parameterized and incremental ADF pipelines

Data ingestion from Azure SQL DB and external sources

Backfilling capability for historical loads

Logic Apps integration for workflow automation

Raw data stored in ADLS Gen2 (Bronze layer)

2️⃣ Data Transformation Layer (Silver)

Spark Streaming using Databricks Auto Loader

PySpark-based cleansing and transformations

Metadata-driven pipelines

SCD Type 1 & Type 2 implementation

Delta tables managed with Unity Catalog

3️⃣ Data Serving Layer (Gold)

Star Schema dimensional modeling

Fact and Dimension tables

Business-ready curated datasets

Optimized for analytics and reporting


🔄 Pipeline Flow:
Azure SQL DB → ADF (Incremental Load) → ADLS Gen2 (Bronze) →
Databricks (Transformations) → Silver Delta Tables →
Gold Layer (Star Schema) → Analytics & Reporting.

This project showcases practical, real-world Data Engineering skills using Azure and Databricks. It demonstrates the ability to design, build, and manage a production-style Lakehouse architecture capable of handling scalable and analytics-ready data workloads.
