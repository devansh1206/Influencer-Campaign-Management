class Config():
    DEBUG = True
    SQL_ALCHEMY_TRACK_MODIFICATION = False

class LocalDevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.sqlite3"
    DEBUG= True
    SECURITY_PASSWORD_HASH = "bcrypt"
    SECURITY_PASSWORD_SALT = "thisisasecretsalt"
    SECRET_KEY = "secretkeyhere"
    SECURITY_TOKEN_AUTHENTICATION_HEADER = "Authentication-Token"
    
    WTF_CSRF_ENABLED = False
     

     