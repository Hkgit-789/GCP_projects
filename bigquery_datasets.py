from google.cloud import bigquery

client=bigquery.Client()

'''datasets=client.list_datasets()

for dataset in datasets:
    print(dataset.dataset_id)'''

'''dstnm=f'{client.project}.hari9854dataset'
client.delete_dataset(dstnm)'''

'''print("\ncreating new data set")
print("=========*******************========")
print("newdatasets are")
datasetnm=f'{client.project}.hari9854dataset'
client.create_dataset(datasetnm)'''

datasets=client.list_datasets()

for dataset in datasets:
    ds=client.get_dataset(dataset.dataset_id)
    print("=============--------==============----------")
    print(ds.dataset_id)
    print(ds.location)
    print(ds.created)
    print("===============---------================")