import boto3
import uuid

class LoanRequestsDb(object):
    '''
    This class manages the data interaction with DynamoDb
    '''
    def __init__(self):
        self.queueName = 'noverde-loan'
        self.sqs = boto3.resource('sqs')
        self.queue = self.sqs.get_queue_by_name(QueueName='noverde-loan')
    
    def sendSQSMessage(self, body: str) -> None:
        '''
        send the SQS message

        No return
        '''
        self.queue.send_message(MessageBody=body)

    def addCustomer(self, customer) -> None:
        '''
        Creates a new Item on DynamoDb
        '''

        # Get the service resource.
        dynamodb = boto3.resource('dynamodb')

        id = str(uuid.uuid1())

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