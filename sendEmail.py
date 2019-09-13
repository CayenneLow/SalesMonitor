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
def sendEmail(price, link):
    response = sns.publish(
        TopicArn='arn:aws:sns:ap-southeast-2:828914858024:SalesMonitor',    
        Message="Get dem headphones for {} at {} boi".format(price, link),    
    )

    # Print out the response
    print(response)
