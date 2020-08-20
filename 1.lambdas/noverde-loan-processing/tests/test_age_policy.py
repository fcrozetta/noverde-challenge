import pytest
from policies.agePolicy import AgePolicy
import datetime
validAge = { 'birthdate': '1900-01-01'}
underAge = {'birthdate': datetime.date.today().strftime('%Y-%m-%d')}
invalidAge = {'birthdate': 'wrong date'}

def test_validAge():
    '''
    test age policy against someone born in 1900
    '''
    result,message = AgePolicy.validate(validAge)
    assert result == True

def test_underAge():
    '''
    Test Age policy against someone who was born at the local currrent date
    '''
    result,message = AgePolicy.validate(underAge)
    assert result == False
    assert len(message) > 0

def test_invalidAge():
    '''
    The birthdate should be validated before this point.
    This is just a sanity check
    '''
    result,message = AgePolicy.validate(invalidAge)
    assert result == False
    assert len(message) > 0