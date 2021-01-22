class Signup():
    def __init__(self,username,email,password,fullname):
        self.username = username
        self.email = email
        self.password = password
        self.fullname = fullname


class Login():
    def __init__(self,username="",email="",password=""):
        self.username = username
        self.email =  email 
        self.password = password

class Forget_Password():
    def __init__(self,email):
        self.email= email


    
