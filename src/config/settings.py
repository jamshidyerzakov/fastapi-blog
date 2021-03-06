import os
from .local_config import *

PROJECT_NAME = "BLOG"
SERVER_HOST = 'http://127.0.0.1:8000'

# Secret key
SECRET_KEY = b"awubsyb872378t^*TG8y**ASD&*8y8yg9POB)*896ft7CR^56dfYUv"

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

API_V1_STR = "/api/v1"

# Token 60 minutes * 24 hours * 8 days = 8 days
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7

# CORS
BACKEND_CORS_ORIGINS = [
    "http://localhost",
    "http://localhost:4200",
    "http://localhost:3000",
    "http://localhost:8080",
]

# Data Base
SQLALCHEMY_DATABASE_URI = (
    f'postgresql://{os.environ.get("POSTGRES_USER")}:'
    f'{os.environ.get("POSTGRES_PASSWORD")}@'
    f'{os.environ.get("POSTGRES_HOST")}/'
    f'{os.environ.get("POSTGRES_DB")}'
)

USERS_OPEN_REGISTRATION = True

EMAILS_FROM_NAME = PROJECT_NAME
EMAIL_RESET_TOKEN_EXPIRE_HOURS = 48
EMAIL_TEMPLATES_DIR = "src/email-templates/build"
EMAILS_ENABLED = SMTP_HOST and SMTP_PORT
EMAIL_TEST_USER = "jamshidyerzakov@gmail.com"