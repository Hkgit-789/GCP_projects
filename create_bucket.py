from google.cloud import storage

client=storage.Client()

buckets=client.list_buckets()
existing_bucks=[]
for bucket in buckets:
    if bucket.name not in existing_bucks:
        existing_bucks.append(bucket.name)
try:
    newbuckname=input("enter your bucknam you want to create=")

    if newbuckname not in existing_bucks:
        client.create_bucket(newbuckname)
        print("\nnew bcuket created")
        buckets=client.list_buckets()
        for buck in buckets:
            print(buck.name)

    else:
        print("your buckname already exist create a new buck")

except Exception as e:
    print(e)

finally:
    print("=============bye bye==========")





