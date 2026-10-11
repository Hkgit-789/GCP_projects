from google.cloud import bigquery

client = bigquery.Client()

table = client.get_table(
    "hari-b45.pcm_usecase.pcm_silver_table"
)

print(table.table_id)
print(table.num_rows)
print(table.num_bytes)
print(table.created)
print(table.modified)

for field in table.schema:
    print(field.name, field.field_type, field.mode)

actual_schema = {
    field.name: [field.field_type,field.mode]
    for field in table.schema
}

print('==============================================================')
print(type(actual_schema))
print('==============================================================')
for columnname,columtype in actual_schema.items():
    print(f'{columnname} type of is {columtype[0]} and mode is {columtype[1]}')
