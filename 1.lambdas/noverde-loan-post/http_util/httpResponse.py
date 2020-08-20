class Response(object):
    '''
    Creates a simple response object to handle responses
    '''
    # Headers included to avoid CORS problems
    self.headers = {
        'Access-Control-Allow-Headers': '*',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': '*'
    }
    self.statusCode: int
    self.body: str

    @staticmethod
    def Response(statusCode = 200, body = {}):
        return {
            'statusCode': statusCode,
            'body': json.dumps(body),
            'headers': self.headers,
        }