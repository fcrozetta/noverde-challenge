import json
from loanRequestsDb import LoanRquestsDb

def lambda_handler(event, context):
    '''
    Handles the incomming event from API gateway
    '''

    try:
        id = event['pathParameters']['id']
    except KeyError:
        #! Not being called via API gateway
        return {
            'statusCode': 400
        }

    return {
        "statusCode":200,
        'body': json.dumps(getLoanResponse(id)),
        'headers': {
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': '*'
        },
        
    }


def getLoanResponse(id: str) -> dict:
    '''
    Return the response from the DB
    '''
    # Sanity check
    if id is None:
        return {}

    db = LoanRquestsDb()
    db.checkRequest(id)

    print(item)
    response = {
        "id":item['id'],
        "status":item['status'],
        "amount":float(item['amount']),
        "terms": int(item['terms']),
    }
    if response['status'] == 'completed':
        response["result"] = item['result']
        
        
        if response['result'] == 'refused':
            response['refused_policy'] = item['refused_policy']
    return response
