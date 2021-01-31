from hamster_service.domain_server.config import firebase
from hamster_service.domain_server.utils import Validator

Auth = firebase.auth()

def SignUp(email,password):
    if not Validator.isValidEmail(email):
        return {"message":"Not a valid email."}

    if not Validator.isValidPassword(password):
        return {"message":"Not a valid password."}

    try:
        user=Auth.create_user_with_email_and_password(email,password)
        Auth.send_email_verification(user["idToken"])
        return {"message":"Check your email for verification."}
    except:
        return {"message":"EMAIL EXISTS"}
    