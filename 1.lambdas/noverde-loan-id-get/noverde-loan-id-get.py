import json
import boto3


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
        'body': json.dumps(getLoanResponse(id))
        
    }


def getLoanResponse(id):
    # Sanity check
    if id is None:
        return {}

    # Get the service resource.
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('loanRequests')
    data = table.get_item(
        Key={
            'id': id,
        }
    )

    item = data['Item']
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



if __name__ == "__main__":
    json.dumps(lambda_handler({
        "pathParameters": {
            "id": '32fbdd96-df46-11ea-88de-f35f8eff49e0'
        }
    }, {}))