import pytest
from noverdeLoanIdGet import *
from http_util.httpResponse import Response

res = Response()

def test_empty_get():
    '''
    Test with empty event and context
    '''
    assert lambda_handler({},{}) == res.Response(400)

def test_invalid_key():
    '''
    testing correct event, but with invalid ID
    '''
    with pytest.raises(KeyError):
        assert lambda_handler({'pathParameters': {'id':'invalid-id'}},{}) == res.Response(400)

def test_valid_key():
    '''
    THIS WILL ALWAYS RETURN TRUE
    Necessary mock data to use, instead of real DB
    '''
    # TODO: Implement Test correctly
    assert True