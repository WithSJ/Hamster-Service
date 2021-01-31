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
        return {"message":"Account created. Check your email for verification."}
    except:
        return {"message":"EMAIL EXISTS"}
    
def Login(email,password):
    if not Validator.isValidEmail(email):
        return {"message":"Not a valid email."}

    if not Validator.isValidPassword(password):
        return {"message":"Not a valid password."}

    try:
        user = Auth.sign_in_with_email_and_password(email,password)
        userInfo = Auth.get_account_info(user["idToken"])

        if userInfo["users"][0]["emailVerified"] != True:
            Auth.send_email_verification(user["idToken"])
            return {"message":"Email not verified. Check your email."}

        return {
            "message":"Login Successfull",
            "user":user,
            "userInfo": userInfo
        }
    except:
        return {"message":"INVALID EMAIL or PASSWORD "}
    
def PasswordReset(email):
    if not Validator.isValidEmail(email):
        return {"message":"Not a valid email."}

    try:
        Auth.send_password_reset_email(email)
        return {"message":"Check email for reset password."}
    except:
        return {"message":"EMAIL NOT FOUND"}