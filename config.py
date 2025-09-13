import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev_secret_change_me")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///portal.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ORGANIZATION_NAME = os.getenv("ORG_NAME", "Ваша Компания")

