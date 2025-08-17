# Task - Create VPC, Public + Private Subnet, IGW, Route Table
# User input for CIDRs, AZ etc.

import boto3

# User input
vpc_cidr = input("Enter VPC CIDR Block (e.g. 10.0.0.0/16) : ")
public_subnet_cidr = input("Enter Public Subnet CIDR Block (e.g. 10.0.1.0/24) : ")
private_subnet_cidr = input("Enter Private Subnet CIDR Block (e.g. 10.0.2.0/24) : ")
subnet_az = input("Enter Availability Zone (e.g. us-east-1a) : ")
route_entry_cidr = input("Enter Destination CIDR Block (e.g. 0.0.0.0/0) : ")

client = boto3.client('ec2')

# Step 1: Create VPC
myvpc = client.create_vpc(
    CidrBlock=vpc_cidr,
    TagSpecifications=[
        {
            'ResourceType': 'vpc',
            'Tags': [{'Key': 'Name', 'Value': 'VPC-1'}]
        },
    ]
)
print("VPC ID :", myvpc['Vpc']['VpcId'])

# Step 2: Create Public Subnet
public_subnet = client.create_subnet(
    VpcId=myvpc['Vpc']['VpcId'],
    AvailabilityZone=subnet_az,
    CidrBlock=public_subnet_cidr,
    TagSpecifications=[
        {
            'ResourceType': 'subnet',
            'Tags': [{'Key': 'Name', 'Value': 'Public-Subnet'}]
        },
    ]
)
print("Public Subnet ID :", public_subnet['Subnet']['SubnetId'])

# Step 3: Create Private Subnet
private_subnet = client.create_subnet(
    VpcId=myvpc['Vpc']['VpcId'],
    AvailabilityZone=subnet_az,
    CidrBlock=private_subnet_cidr,
    TagSpecifications=[
        {
            'ResourceType': 'subnet',
            'Tags': [{'Key': 'Name', 'Value': 'Private-Subnet'}]
        },
    ]
)
print("Private Subnet ID :", private_subnet['Subnet']['SubnetId'])

# Step 4: Create Internet Gateway
igw = client.create_internet_gateway(
    TagSpecifications=[
        {
            'ResourceType': 'internet-gateway',
            'Tags': [{'Key': 'Name', 'Value': 'IGW-1'}]
        },
    ]
)
print("Internet Gateway ID :", igw['InternetGateway']['InternetGatewayId'])

# Step 5: Attach Internet Gateway
client.attach_internet_gateway(
    InternetGatewayId=igw['InternetGateway']['InternetGatewayId'],
    VpcId=myvpc['Vpc']['VpcId']
)

# Step 6: Create Route Table (for Public Subnet)
public_rt = client.create_route_table(
    VpcId=myvpc['Vpc']['VpcId'],
    TagSpecifications=[
        {
            'ResourceType': 'route_table',
            'Tags': [{'Key': 'Name', 'Value': 'Public-RT'}]
        },
    ]
)
print("Public Route Table ID :", public_rt['RouteTable']['RouteTableId'])

# Step 7: Create Route for Internet Access (only for Public subnet)
client.create_route(
    RouteTableId=public_rt['RouteTable']['RouteTableId'],
    DestinationCidrBlock=route_entry_cidr,
    GatewayId=igw['InternetGateway']['InternetGatewayId']
)

# Step 8: Associate Route Table with Public Subnet
client.associate_route_table(
    SubnetId=public_subnet['Subnet']['SubnetId'],
    RouteTableId=public_rt['RouteTable']['RouteTableId']
)

print("Setup Completed: VPC + Public + Private Subnet Created")
