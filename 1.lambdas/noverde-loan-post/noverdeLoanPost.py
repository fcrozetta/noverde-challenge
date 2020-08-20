import json
from loanRequestsDb import LoanRequestsDb
from http_util.httpResponse import Response
def lambda_handler(event, context):
    '''
    Handles the incomming event from API gateway
    '''

    http = Response()
    
    # Sanity check (The body validation happens at AWS API Gateway, with schemas)
    try:
        customer = json.loads(event['body'])
    except KeyError:
        return http.Response(400)
        
    db = LoanRequestsDb()
    id = db.addCustomer(customer)

    return http.Response(200,{'id' : id})