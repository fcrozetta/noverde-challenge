import json
import urllib3
from typing import Tuple

class CommitmentPolicy(object):
    @staticmethod
    def validate(customer,score) -> Tuple[bool,str]:
        commitment = None

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
            'https://challenge.noverde.name/commitment',
            body=encoded_body,
            headers=headers
        )
        if response.status != 200:
            return (False,"Score not available")
        else:
            response_body = json.loads(response.data)
            commitment = response_body['commitment']


        return (False,"Commintment lower than the minimum necessary")