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
        isApproved,refused_policy = process(customer)

        # Updates Data on DynamoDB
        if isApproved:
            updateCustomer(id,{
                'status': 'approved',
            })
        else:
            updateCustomer(id,{
                'status': 'refused',
                'refused_policy': refused_policy
            })
        
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
    return PolicyExecution().executePolicies(customer)

def updateCustomer(id,newData:dict):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('loanRequests')
    updateString = "set process_status = :s, process_result = :r "
    ExpressionAttributeValues = {
        ':s': 'completed',
        ':r': newData['status']
    }

    if newData['status'] == "refused":
        updateString += ", refused_policy = :rp"
        ExpressionAttributeValues[':rp'] = newData['refused_policy']
    # exit()
    table.update_item(
        Key={
            'id': id,
    },
    UpdateExpression=updateString,
    ExpressionAttributeValues = ExpressionAttributeValues
)

if __name__ == "__main__":
    lambda_handler({}, {})
