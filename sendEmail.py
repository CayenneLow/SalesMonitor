import boto3

sns = boto3.client('sns')

# Publish a simple message to the specified SNS topic
def sendEmail(price, link):
    response = sns.publish(
        TopicArn='arn:aws:sns:ap-southeast-2:828914858024:SalesMonitor',    
        Message="Get dem headphones for {} at {} boi".format(price, link),    
    )

    # Print out the response
    print(response)