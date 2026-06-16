# run this script with
# python code/demos/ai-02-dotenv.py
from dotenv import load_dotenv
from chatlas import ChatGithub

 # this is the path to the .env file relative to working directory
load_dotenv('.env')

chat = ChatGithub(model="gpt-5")
print(chat.list_models())

chat.chat("Where is SciPy 2026 being held?")

chat.chat("Where is SciPy 2027 being held?")