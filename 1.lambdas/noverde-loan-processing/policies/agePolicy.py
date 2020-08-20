from typing import Tuple
from datetime import datetime, date
class AgePolicy(object):
    
    @staticmethod
    def validate(customer) -> Tuple[bool,str]:
        '''
        Customer age has to be 18+
        '''
        age = calculate_age(customer['birthdate'])
        if age < 18:
            return (False,"Customer cannot be underage")
        else:
            return (True,"Approved")

def calculate_age(birthdate):
    born = datetime.strptime(birthdate,'%Y-%m-%d')
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))