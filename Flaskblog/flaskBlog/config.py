import os

'''
here are all configurations defined for the database, the de mailserver.

make sure that the current global variables are in your system:
 -  SECRET_KEY: this is used for resetting the password
 -  SQLALCHEMY_DATABASE_URI: the location of the database file.
 -  EMAIL_USER: the username for the email-server
 -  EMAIL_PASS: the password for the mail-server
'''


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
