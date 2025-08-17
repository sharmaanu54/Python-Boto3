import boto3

client = boto3.client('s3', aws_access_key_id='AKIA6H5STAZTWECODTXK', aws_secret_access_key='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')

List_S3_Buckets = client.list_buckets()
for i in List_S3_Buckets['Buckets']:
    #print list of all S3 buckets along with their Creation Date
    print(f"S3 Bucket - {i['Name']}  Created On - {i['CreationDate']}")

    # list all S3 buckets
    # print(i)