import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

# Host
host = os.environ.get('SUPRO_API_HOST')

# TestRail Data
testrail_data = {
    'user': os.environ.get('TESTRAIL_USER'),
    'password': os.environ.get('TESTRAIL_PASSWORD'),
    'email': os.environ.get('TESTRAIL_EMAIL'),
    'url': os.environ.get('TESTRAIL_HOST')
}

run_id = -1