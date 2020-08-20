from typing import Tuple
import urllib3
import json

class ScorePolicy(object):
    @staticmethod
    def validate(customer) -> Tuple[bool,str]:
        '''
        Validates the customer Score.
        Returns a tuple with status(bool) and a message(score or refuse message)
        '''
        http = urllib3.PoolManager()

        #! API KEY IS VISIBLE ON CODE JUST FOR THE CHALLENGE
        #! in prod, the key should beon aws secrets, or similar
        headers = {
            'x-api-key':'z2qcDsl6BK8FEPynp2ND17WvcJKMQTpjT5lcyQ0d',
            'Content-Type':'application/json'
        }
        apiBody = {'cpf': customer['cpf']}
        encoded_body = json.dumps(apiBody).encode('utf-8')

        response = http.request('POST',
            'https://challenge.noverde.name/score',
            body=encoded_body,
            headers=headers
        )
        if response.status != 200:
            return (False,"Score not available")
        else:
            response_body = json.loads(response.data)
            score = response_body['score']
            if score >= 600:
                return (True,f"{score}")
            else:
                return (False,"Score lower than the minimum necessary")

