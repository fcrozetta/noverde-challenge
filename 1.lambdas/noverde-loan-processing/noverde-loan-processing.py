import json
import boto3
from policies.policyExecution import PolicyExecution

def lambda_handler(event, context):
    '''
    Handles the incomming event from API gateway
    '''

    # Get the service resource
    sqs = boto3.resource('sqs')

    # Get the queue
    queue = sqs.get_queue_by_name(QueueName='noverde-loan')

    # Process messages
    for message in queue.receive_messages(MaxNumberOfMessages=1):
        print('ID: {0}'.format(message.body))
        id = str(message.body)
        customer = getCustomer(id)

        # policy processing
        process(customer)

        #update DB
        updateCustomer(id,customer)
        
        # Let the queue know that the message is processed
        message.delete()

    return


def getCustomer(id):
    # Get the service resource.
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('loanRequests')
    data = table.get_item(
        Key={
            'id': str(id),
        }
    )

    return data['Item']

# This function should execute every available policy
def  process(customer):
    result = PolicyExecution().executePolicies(customer)
    print(result)
    pass
def updateCustomer(id,newData):
    pass

if __name__ == "__main__":
    print(lambda_handler({}, {}))
