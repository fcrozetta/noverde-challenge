import json
from loanRequestsDb import LoanRequestsDb
def lambda_handler(event, context):
    '''
    Handles the incomming event from API gateway
    '''
    # TODO : Create User based on parameters from body

    customer = json.loads(event['body'])
    db = LoanRequestsDb()

    # Sanity check (But the validation happens at AWS API Gateway)
    if customer is None:
        return {
            'statusCode': 400
        }

    id = db.addCustomer(customer)

    # Return includes headers to avoid problems with CORS
    return {
        'statusCode': 200,
        'body': json.dumps({"id":id}),
        'headers': {
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': '*'
        },
    }


