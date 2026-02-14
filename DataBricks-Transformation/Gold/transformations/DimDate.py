import dlt

@dlt.table
def FactStream_Stg():
    df = spark.readStream.table("db2099.silver.factstreams")
    return df

dlt.create_streaming_table("factstreams")

from pyspark import pipelines as dp

dp.create_auto_cdc_flow(
  target = "factstreams",
  source = "FactStream_Stg",
  keys = ["stream_id"],
  sequence_by = "stream_timestamp",
  stored_as_scd_type = 1,
  track_history_except_column_list = None,
  name = None,
  once = False
)