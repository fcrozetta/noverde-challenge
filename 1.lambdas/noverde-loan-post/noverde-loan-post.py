import json
from loanRequestsDb import LoanRequestsDb
from http_util.httpResponse import Response
def lambda_handler(event, context):
    '''
    Handles the incomming event from API gateway
    '''

    customer = json.loads(event['body'])
    db = LoanRequestsDb()

    # Sanity check (The body validation happens at AWS API Gateway)
    if customer is None:
        return Response.Response(400)

    id = db.addCustomer(customer)

    return Response.Response(200,{'id' : id})