import os


class Config:
    # SECRET_KEY = os.environ.get('SECRET_KEY')
    SECRET_KEY = '5dff52b8ac26ff40b60afb0fb07e4e22'

    # SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_DATABASE_URI= 'sqlite:///site.db'

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
