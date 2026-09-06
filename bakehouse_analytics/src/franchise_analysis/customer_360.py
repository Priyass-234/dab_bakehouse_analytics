# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "5"
# ///
# MAGIC %md
# MAGIC # Default notebook
# MAGIC
# MAGIC This default notebook is executed using a Lakeflow job as defined in resources/sample_job.job.yml.

# COMMAND ----------

dbutils.widgets.text("catalog", "bakehouse_analytics_dev")
dbutils.widgets.text("schema", "test")

# COMMAND ----------

# Set default catalog and schema
catalog = dbutils.widgets.get("catalog")
schema = dbutils.widgets.get("schema")
spark.sql(f"USE CATALOG `{catalog}`")
spark.sql(f"CREATE SCHEMA IF NOT EXISTS `{schema}`")
spark.sql(f"USE SCHEMA `{schema}`")

# COMMAND ----------

spark.sql(f"""CREATE OR REPLACE TABLE {catalog}.{schema}.franchise_analytics AS
SELECT country, size, COUNT(*) AS number_of_franchise
FROM samples.bakehouse.sales_franchises
GROUP BY country, size""")