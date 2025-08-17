import boto3

client = boto3.client('ec2')

List_VPC = client.describe_vpcs()
for i in List_VPC['Vpcs']:
    print(f"VPC ID - {i['VpcId']} and CIDR Block - {i['CidrBlock']}")
    
    # KT - In Line 3 we used ec2 not vpc because when we use boto3.client('xyz'), the
    # 'xyz' must be an actual AWS service name like ec, lambda,iam, s3. But vpc
    # itself is not an aws service name, vpc is part of ec2 so when need to list
    # vpc we need to call it via ec2 client only
    
    # we have not passed the aws_access_key and aws_secret_key in code because 
    # we passed these in command prompt via aws configure.