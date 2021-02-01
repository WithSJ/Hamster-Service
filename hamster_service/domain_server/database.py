from hamster_service.domain_server.config import firebase

database = firebase.database()

def CreateNewUser(localId,fullname="",username=""):
    database.child("Users").child(localId).set(
        {   "fullname":fullname,
            "username": username
        })

