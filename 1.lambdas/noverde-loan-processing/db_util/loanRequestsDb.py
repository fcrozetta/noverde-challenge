import boto3

class LoanRequestsDb(object):
    '''
    This class manages the data interaction with DynamoDb
    '''
    def __init__(self):
        self.queueName = 'noverde-loan'
    
    def getIdFromSqs(self) -> str:
        '''
        Gets the Id for the first message in the list
        '''
        # Get the service resource
        sqs = boto3.resource('sqs')

        # Get the queue
        queue = sqs.get_queue_by_name(QueueName='noverde-loan')
        

        id = None
        for message in queue.receive_messages(MaxNumberOfMessages = 1):
            id = str(message.body)
            message.delete()
        return id

    def getCustomer(self, id: str) -> dict:
        '''
        Gets the customer from the database
        Return a dict with the data
        '''
        # Get the service resource.
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('loanRequests')
        data = table.get_item(
            Key={
                'id': str(id),
            }
        )

        return data['Item']

    def updateCustomer(self, id: str, newData:dict):
        '''
        Updates the user on dynamoDb

        No return
        '''
        # TODO: Refactor this to update any field
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
        table.update_item(
            Key={
                'id': id,
            },
            UpdateExpression=updateString,
            ExpressionAttributeValues = ExpressionAttributeValues
        )
    
    def updateTerms(self,id: str, terms):
        '''
        Updates the number of terms on the database.

        No return
        '''
        # TODO: Integrate this on updateCustomer method
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('loanRequests')

        if terms != None:
            table.update_item(
                Key={
                    'id': id,
                },
                UpdateExpression='set terms = :t',
                ExpressionAttributeValues = {':t': terms}
            )
        else:
            table.update_item(
                Key={
                    'id': id,
                },
                UpdateExpression='remove #p',
                ExpressionAttributeValues = {'#p': 'terms'}
            )
