import boto3

class LoanRequestsDb(object):
    def __init__(self):
        self.queueName = 'noverde-loan'
    
    def getQueueMessages(self):
        # Get the service resource
        sqs = boto3.resource('sqs')

        # Get the queue
        queue = sqs.get_queue_by_name(QueueName='noverde-loan')
        
        id = None
        for message in queue.receive_messages(MaxNumberOfMessages = 1):
            id = str(message.body)
        return id

    def getCustomer(self, id: str):
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
    
    def updateTerms(self,id: str, terms):
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
