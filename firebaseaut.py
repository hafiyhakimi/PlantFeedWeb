import pyrebase
from getpass import getpass

firebaseConfig={

    "apiKey": "AIzaSyDHx0RR2nsDiJECbaP4DpLpejjqutLPN34",
    "authDomain": "i-grow-kmma.firebaseapp.com",
    "projectId": "i-grow-kmma",
    "databaseURL": "xxxxxx",
    "storageBucket": "i-grow-kmma.appspot.com",
    "messagingSenderId": "426593032564",
    "appId": "1:426593032564:web:37f2948f17ae0cde6fb421",
    "measurementId": "G-Z1JJD88MCZ"
}

firebase = pyrebase.initialize_app(firebaseConfig)

auth = firebase.auth()

email = input("Please enter your email address: \n ")
password = getpass("Please enter your password: \n ")

#user = auth.create_user_with_email_and_password(email, password)
login = auth.sign_in_with_email_and_password(email,password)
print("Success...")
