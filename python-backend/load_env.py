import os
from dotenv import load_dotenv, find_dotenv

# pip install python-dotenv
# load_dotenv()
# load_dotenv('../') # 指定目录

load_dotenv(find_dotenv(), override=True)

api_key = os.getenv("API_KEY", '-')
base_url = os.getenv("BASE_URL", '-')
model_name = os.getenv("MODEL_NAME", '-')
print(f'{api_key=}\n{base_url=}\n{model_name=}')

