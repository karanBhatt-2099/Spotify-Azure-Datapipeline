import dlt

@dlt.table
def DimDate_Stg():
    df = spark.readStream.table("db2099.silver.dimdate")
    return df

dlt.create_streaming_table("dimdate")

from pyspark import pipelines as dp

dp.create_auto_cdc_flow(
  target = "dimdate",
  source = "DimDate_Stg",
  keys = ["date_key"],
  sequence_by = "date",
  stored_as_scd_type = 2,
  track_history_except_column_list = None,
  name = None,
  once = False
)