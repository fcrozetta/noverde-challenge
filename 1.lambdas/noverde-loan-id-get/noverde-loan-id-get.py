import json
from loanRequestsDb import LoanRquestsDb
from http_util.httpResponse import Response
def lambda_handler(event, context):
    '''
    Handles the incomming event from API gateway
    '''

    try:
        id = event['pathParameters']['id']
    except KeyError:
        #! Not being called via API gateway
        return Response.Response(400)

    customer = getLoanResponse(id)
    return Response.Response(200,getLoanResponse(id))


def getLoanResponse(id: str) -> dict:
    '''
    Return the altered response from DB
    '''

    db = LoanRquestsDb()
    customer = db.checkRequest(id)

    # ? There should be a mapper to use dynamoDB json objects directly
    # ? For now, doing it manually is acceptable
    response = {
        "id":customer['id'],
        "status":customer['status'],
        "amount":float(customer['amount']),
        "terms": int(customer['terms']),
    }
    if response['status'] == 'completed':
        response["result"] = customer['result']
        if response['result'] == 'refused':
            response['refused_policy'] = customer['refused_policy']
    return response
