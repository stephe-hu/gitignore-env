import os
from dotenv import load_dotenv

load_dotenv()

print(os.getenv('myusername'))
print(os.getenv('mypassword'))
