from typing import Tuple
from datetime import datetime, date
class AgePolicy(object):
    
    @staticmethod
    def validate(customer) -> Tuple[bool,str]:
        '''
        Customer age has to be 18+
        '''
        try:
            age = calculate_age(customer['birthdate'])
        except ValueError:
            return(False,'Birthdate is invalid')
        
        if age < 18:
            return (False,"Customer cannot be underage")
        else:
            return (True,"Approved")

def calculate_age(birthdate: str) -> int:
    '''
    Return the age, based on birthdate.
    This function considers the timezone at server location (UTC 00:00 usually)
    '''
    born = datetime.strptime(birthdate,'%Y-%m-%d')
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))