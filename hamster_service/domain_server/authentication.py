from hamster_service.domain_server.config import firebase
from hamster_service.domain_server.utils import Validator

Auth = firebase.auth()

def SignUp(email,password):
    if not Validator.isValidEmail(email):
        return "Not a valid email."

    if not Validator.isValidPassword(password):
        return ["Not a valid password",
        "It should contain (A-Z,a-z,0-9,@-#) char and size 8 char."]

    try:
        user = Auth.create_user_with_email_and_password(email,password)
        return user
    except:
        return "EMAIL EXISTS"
    