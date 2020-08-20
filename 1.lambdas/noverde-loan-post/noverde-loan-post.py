import json
import boto3
import uuid


def lambda_handler(event, context):
    '''
    Handles the incomming event from API gateway
    '''
    # TODO : Create User based on parameters from body
    # return {
    #     "body": event['body']
    # }
    customer = json.loads(event['body'])
    

    id = addCustomer(customer)

    
    # # Adds a message on SQS to be consumed later by processing funtion
    sqs = boto3.resource('sqs')
    queue = sqs.get_queue_by_name(QueueName='noverde-loan')

  
    queue.send_message(MessageBody=id)
    return {
        'statusCode': 200,
        'body': json.dumps({"id":id})
    }


def addCustomer(customer):
    if customer is None:
        return {
            'statusCode': 400
        }
    # Get the service resource.
    dynamodb = boto3.resource('dynamodb')

    id = str(uuid.uuid1())

    #Create the DynamoDB table. (lazy-loading)
    table = dynamodb.Table('loanRequests')
    table.put_item(Item={
        "id": str(id),
        "name": customer['name'],
        "cpf": customer['cpf'],
        "birthdate": customer['birthdate'],
        "amount": customer['amount'],
        "terms": customer['terms'],
        "income": customer['income'],
        "status":'processing'
    })

    return id