import json

content = json.loads(open('app/client_secret.json',
                            'r').read())['web']
CLIENT_ID = content['client_id']
APP_NAME = 'Catalop Web Application'
GOOGLE_AUTH = 'app/client_secret.json'
ERROR_401 = 'Unable to process information as requested'
APP_SECRET_KEY=content['client_secret']
FACEBOOK_KEY = ''
SQLALCHEMY_DATABASE_URI = 'postgresql://catalog:passDB@localhost/CatalogDb'
#SERVER_NAME='http://ec2-52-36-126-192.us-west-2.compute.amazonaws.com/'
#SERVER_NAME='_'
