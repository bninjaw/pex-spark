# Databricks notebook source
dbutils.notebook.run("dbfs:/FileStore/bw_sandbox/pants", 60)

# COMMAND ----------

# MAGIC %run ./pants

# COMMAND ----------

# MAGIC %sh
# MAGIC pip install pyarrow pandas pex
# MAGIC pex pyspark pyarrow pandas -o pyspark_pex_env.pex

# COMMAND ----------

 ./pyspark_pex_env.pex -c "import pandas; print(pandas.__version__)"
1.1.5

# COMMAND ----------

# MAGIC %sh
# MAGIC ./pants package spark_example/src/python/example

# COMMAND ----------

export PYSPARK_DRIVER_PYTHON=python
export PYSPARK_PYTHON=./pyspark_pex_env.pex
pyspark --files pyspark_pex_env.pex

# COMMAND ----------


