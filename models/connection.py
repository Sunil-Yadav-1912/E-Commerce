import firebase_admin
from firebase_admin import credentials,firestore,db

class Connection(object):

    connection = None

    @classmethod
    def get_connection(cls):
        if cls.connection is None:
            try:
                cred = credentials.Certificate("key.json")
                firebase_admin.initialize_app(cred, {
                    'databaseURL': 'https://digital-deals-1912-default-rtdb.asia-southeast1.firebasedatabase.app/'
                })
                # firebase_admin.initialize_app(cred)  
                # cls.connection = firestore.client()
                cls.connection = db.reference()
                print("Connection established")
            except Exception as error:
                print("Error: Connection not established {}".format(error))
        return cls.connection


