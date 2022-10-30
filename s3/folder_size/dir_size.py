import boto3
from boto3 import client

conn = client('s3')
bucket_name = "tmpkishorereddy"
top_level_folders = dict()

for key in conn.list_objects(Bucket='tmpkishorereddy')['Contents']:

    folder = key['Key'].split('/')[0]
    print("Key %s in folder %s. %d bytes" % (key['Key'], folder, key['Size']))

    if folder in top_level_folders:
        top_level_folders[folder] += key['Size']
    else:
        top_level_folders[folder] = key['Size']

for folder, size in top_level_folders.items():
    print("Folder: %s, size: %d" % (folder, size))

# Get size by folder level
s3 = boto3.resource('s3')
resp = s3.Bucket(bucket_name).objects.filter(Prefix="poc/rundate/").all()
for obj in resp:
    print(obj.size)
    print(dir(obj))
    print(obj.owner)
    print(obj.bucket_name)