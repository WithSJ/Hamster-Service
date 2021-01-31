import re

class Validator:
    @classmethod
    def isValidEmail(cls,email):

        if len(email) > 7:
        
            if re.match(
                "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,5}$",
                email) != None:
                return True
        
        return False