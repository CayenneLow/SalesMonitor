import boto3
import config

accessKeyId= config.accessKeyId
secretAccessKey = config.secretAccessKey

sns = boto3.client(
            'sns', 
            region_name = "ap-southeast-2", 
            aws_access_key_id = accessKeyId, 
            aws_secret_access_key = secretAccessKey
        )

# Publish a simple message to the specified SNS topic
def sendEmail(name, price, link):
    response = sns.publish(
        TopicArn='arn:aws:sns:ap-southeast-2:520715813539:Sales-Monitor',    
        Message="{} is now {} at: {}".format(name, price, link),    
    )

    # Print out the response
    print(response)
