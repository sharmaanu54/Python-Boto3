# Task - Client need a script to pull the instance names, instance ids and their
#launch time so that they confirm/ identify the unwanted servers


import boto3

client = boto3.client('ec2')

List_Ec2 = client.describe_instances()

for i in List_Ec2['Reservations']:
    for j in i['Instances']:
        for k in j['Tags']:
            print("Server Name :", k['Value'])
            print("Instance ID : ", j['InstanceId'])
            print("Launch Time : ", j['LaunchTime'])
            #print(k['Value'], j['InstanceId'], j['LaunchTime'])
            #print(f"Instance 1 - {k['Value']}, Instance ID - {j['InstanceId']}, and its Launch Time - {j['LaunchTime']}")
      

# KT - Reservation is the dictionary got in print(List_Ec2) and Instance ids, 
# Value(Server Name) belongs to Tags and Tags belong to Instances

