from policies.agePolicy import AgePolicy
from policies.scorePolicy import ScorePolicy
from policies.commitmentPolicy import CommitmentPolicy
from loanRequestsDb import LoanRequestsDb
class PolicyExecution(object):

    @staticmethod
    def executePolicies(customer):
        isCustomerApproved=True
        returnMessage = ""

        # ! Age policy
        isApproved,message = AgePolicy.validate(customer)
        if not isApproved:
            isCustomerApproved = False
            returnMessage += f'{message};'

        # ! Score policy
        isApproved,message = ScorePolicy.validate(customer)
        if isApproved:
            commitment = float(message)
        else:
            isCustomerApproved = False
            returnMessage += f'{message};'
            


        # ! Commitment policy
        # * validates only if everything is ok so far
        if isCustomerApproved:
            isApproved,commitmentReturn = CommitmentPolicy.validate(customer,commitment)
            if isApproved:
                db = LoanRequestsDb()
                db.updateTerms(customer['id'],commitmentReturn)
            else:
                isCustomerApproved = False
                returnMessage += commitmentReturn


        # Return the flag after the policies and messages, if any
        return (isCustomerApproved,returnMessage)

        