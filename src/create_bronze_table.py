# Databricks notebook source
my_catalog = dbutils.widgets.get('catalog_name')
target = dbutils.widgets.get('display_target')
raw_data_path = dbutils.widgets.get('raw_data_path')

spark.sql(f'USE CATALOG {my_catalog}')

print(f'Using the {my_catalog} catalog.')
print(f'Deploying as the {target} pipeline.')
print(f'Reading raw data from: {raw_data_path}')

# COMMAND ----------

spark.sql(f'''
CREATE OR REPLACE TABLE {my_catalog}.default.health_bronze_demo_08 AS
SELECT
  *,
  _metadata.file_name as file_name,
  _metadata.file_modification_time as file_modification_time,
  current_timestamp() as load_date
FROM read_files(
  '{raw_data_path}/',
  format => 'csv',
  header => true
)
''')
