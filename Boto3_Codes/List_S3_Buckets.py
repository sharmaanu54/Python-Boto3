import boto3

client = boto3.client('s3')

#since we already gave aws_secret_key and aws_access_key in aws configure in 
# command prompt so we havent used them in line 3 else we need to use line 7
#client = boto3.client('s3', aws_access_key_id='Enter your aws_access_key', aws_secret_access_key='Enter your aws_secret_access_key')

List_S3_Buckets = client.list_buckets()
for i in List_S3_Buckets['Buckets']:
    #print list of all S3 buckets along with their Creation Date
    print(f"S3 Bucket - {i['Name']}  Created On - {i['CreationDate']}")

    # list all S3 buckets
    # print(i)