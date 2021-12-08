# Databricks notebook source
dbutils.notebook.run("dbfs:/FileStore/bw_sandbox/pants", 60)

# COMMAND ----------

# MAGIC %run ./pants

# COMMAND ----------

# MAGIC %sh
# MAGIC 
# MAGIC ./pants package spark_example/src/python/example

# COMMAND ----------

# MAGIC %sh ls

# COMMAND ----------


