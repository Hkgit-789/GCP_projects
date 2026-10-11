from google.cloud import bigquery

client=bigquery.Client()

tables=client.list_tables("pcm_usecase")

for table in tables:
    print(table.table_id)