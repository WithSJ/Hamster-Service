import pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyCN9_90a-l7ABnmrDpOpupXifiykhzXhSo",
    "authDomain": "hamster-49dc2.firebaseapp.com",
    "projectId": "hamster-49dc2",
    "storageBucket": "hamster-49dc2.appspot.com",
    "messagingSenderId": "718345613012",
    "appId": "1:718345613012:web:1c1895ebca8ed6d6b89541",
    "measurementId": "G-WN8LEW44L4",
    "databaseURL": "https://hamster-49dc2-default-rtdb.firebaseio.com/"
}

firebase = pyrebase.initialize_app(firebaseConfig)