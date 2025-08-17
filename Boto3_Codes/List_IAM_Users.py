import boto3

client = boto3.client('iam')

List_IAM_Users = client.list_users()
for i in List_IAM_Users['Users']:
    #print list of all IAM users along with their Creation Date
    #print(f"IAM User - {i['UserName']}  Created On - {i['CreateDate']}")
    
    #list all IAm users
    print(i)
    
    # KT -when we print(List_IAM_Users), the output This returns a dictionary that looks something 
    # like this
    
    # {
    # 'Users': [
        # {
            # 'Path': '/',
            # 'UserName': 'admin-user',
            # 'UserId': 'AIDXXXXXXXXXXXXXXXX',
           #  'Arn': 'arn:aws:iam::123456789012:user/admin-user',
     #       }
    # ]
    # Now we can loop through the 'Users' list inside the response dictionary to 
    # print specific field say UserName , CreateDate
    
    
   
    