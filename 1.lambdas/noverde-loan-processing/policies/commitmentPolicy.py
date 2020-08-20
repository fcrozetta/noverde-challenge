import json
import urllib3
import math
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

        income = float(customer['income'])
        availableIncome = income - (income * commitment)

        return CommitmentPolicy.PMT(float(customer['amount']),int(customer['terms']),availableIncome,float(score))
    
    @staticmethod
    def PMT(pv,n,availableIncome,score):
        '''
        Calculate the possible PMT for the paramters
        pv: requested value,
        n: terms,
        availableIncome: Income available after commitment percentage
        score: Serasa customer's score
        '''
        if n == 12:
            return (false,'Commintment lower than the minimum necessary')
        i = CommitmentPolicy.getInterestRate(score,n)
        result = pv * (pow((1+i),n) * i) / (pow((1+i),n) -1 )
        if result < availableIncome:
                return (true,n)
        else:
                return CommitmentPolicy.PMT(pv, n+3,availableIncome,score)

    @staticmethod
    def getInterestRate(score,terms):
        '''
        get the interest rate based on score levels and terms
        '''
        # TODO: Find an elegant way to present this table. maybe in a database?
        if score >= 900:
            if terms == 6:
                return 0.039
            if terms == 9:
                return 0.042
            if terms == 12:
                return 0.045
        if score >= 800 and score <= 899:
            if terms == 6:
                return 0.047
            if terms == 9:
                return 0.050
            if terms == 12:
                return 0.053
        if score >= 700 and score <= 799:
            if terms == 6:
                return 0.055
            if terms == 9:
                return 0.058
            if terms == 12:
                return 0.061
        if score >= 600 and score <= 699:
            if terms == 6:
                return 0.064
            if terms == 9:
                return 0.066
            if terms == 12:
                return 0.069
    