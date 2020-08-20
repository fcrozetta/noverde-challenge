import json
from loanRequestsDb import LoanRequestsDb
from policies.policyExecution import PolicyExecution

def lambda_handler(event, context):
    '''
    Handles the incomming event from API gateway
    '''
    
    loanDb = LoanRequestsDb()
    id = None
    try:
        
        sqsMessage = event['Records'][0]
        print('id via sqs')
        id = sqsMessage['body']
    except KeyError:
        print('id via loanRequest call')
        id = loanDb.getQueueMessages()
        
    print(f'ID : {str(id)}')
    
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