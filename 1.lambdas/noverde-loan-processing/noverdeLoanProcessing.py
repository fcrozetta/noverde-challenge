import json
from db_util.loanRequestsDb import LoanRequestsDb
from policies.policyExecution import PolicyExecution

def lambda_handler(event, context):
    '''
    Handles the incomming event from API gateway
    '''
    
    loanDb = LoanRequestsDb()
    id = None

    # Gets the ID from SQS trigger, or calling from local machine
    try:
        sqsMessage = event['Records'][0]
        id = sqsMessage['body']
        print('id via sqs')
    except KeyError:
        id = loanDb.getIdFromSqs()
        print('id via loanRequest call')
        
    print(f'ID : {str(id)}')

    # Sanity check. Only proceeds if there is an ID
    if id == None:
        return

    customer = loanDb.getCustomer(id)

    # policy processing
    isApproved,refused_policy = PolicyExecution().executePolicies(customer)

    # Updates Data on DynamoDB
    if isApproved:
        loanDb.updateCustomer(id,{
            'status': 'approved',
        })
    else:
        loanDb.updateCustomer(id,{
            'status': 'refused',
            'refused_policy': refused_policy
        })

if __name__ == "__main__":
    lambda_handler({},{})