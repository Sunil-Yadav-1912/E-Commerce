from dotenv import dotenv_values
# from pathlib import Path
# from dotenv import load_dotenv

env = dotenv_values(".env")

TYPE = env['TYPE']
PROJECT_ID = env['PROJECT_ID']
PRIVATE_KEY_ID = env['PRIVATE_KEY_ID']
PRIVATE_KEY = env['PRIVATE_KEY']
CLIENT_EMAIL = env['CLIENT_EMAIL']
CLIENT_ID = env['CLIENT_ID']
auth_uri = env['auth_uri']
TOKEN_URI = env['TOKEN_URI']
AUTH_PROVIDER_X509_CERT_URL = env['AUTH_PROVIDER_X509_CERT_URL']
CLIENT_X509_CERT_URL = env['CLIENT_X509_CERT_URL']
UNIVERSE_DOMAIN = env['UNIVERSE_DOMAIN']
DATABASE_URL = env['DATABASE_URL']


