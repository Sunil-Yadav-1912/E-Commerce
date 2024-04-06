import firebase_admin
from firebase_admin import credentials,firestore,db
import config
class Connection(object):

    connection = None

    @classmethod
    def get_connection(cls):
        if cls.connection is None:
            try:
                cred = credentials.Certificate({
                    "type":config.TYPE,
                    "project_id":config.PROJECT_ID,
                    "private_key_id":config.PRIVATE_KEY_ID,
                    "private_key":config.PRIVATE_KEY,
                    "client_email":config.CLIENT_EMAIL,
                    "client_id":config.CLIENT_ID,
                    "auth_uri":config.auth_uri,
                    "token_uri":config.TOKEN_URI,
                    "auth_provider_x509_cert_url":config.AUTH_PROVIDER_X509_CERT_URL,
                    "client_x509_cert_url":config.CLIENT_X509_CERT_URL
                })                
                firebase_admin.initialize_app(cred, {
                    'databaseURL':config.DATABASE_URL,
                })
                # firebase_admin.initialize_app(cred)  
                # cls.connection = firestore.client()
                cls.connection = db.reference()
                print("Connection established")
            except Exception as error:
                print("Error: Connection not established {}".format(error))
        return cls.connection


