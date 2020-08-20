import pytest
from noverdeLoanPost import *
from http_util.httpResponse import Response

http = Response()

validUser = {
	"name": "a",
	"cpf": "12345678901",
    "birthdate": "1992-12-22",
    "amount": 1000,
    "terms": 6,
    "income": 1000
}

def test_empty_post():
    '''
    Test an empty post. 
    This will not occur during production,since validation occurs
    in AWS API Gateway
    '''
    assert lambda_handler({},{}) == http.Response(400)

def test_valid_post():
    '''
    Test a valid input.
    This method requires a mock service to work propeprly.
    For now, it raises an error
    ''' 
    #TODO Implement Mock data to test those functions
    # assert lambda_handler({'body':validUser},{}) == http.Response(200,{'id':'Some ID'})
    raise NotImplementedError

# ! This test is not necessary here, since AWS validates the body at the gateway
# def test_invalid_post():
#     pass