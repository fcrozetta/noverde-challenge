import boto3

class LoanRequestsDb(object):
    '''
    This class manages the data interaction with DynamoDb
    '''
    def __init__(self):
        self.queueName = 'noverde-loan'
    
    def checkRequest(self,id: str) -> dict:
        # Get the service resource.
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('loanRequests')
        data = table.get_item(
            Key={
                'id': id,
            }
        )
        return data
