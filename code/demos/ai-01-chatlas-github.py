# run this script with
# export GITHUB_TOKEN=your_personal_access_token
# python code/demos/ai-01-chatlas-github.py

from chatlas import ChatOpenAI, ChatAnthropic, ChatGoogle, ChatGithub, ChatOllama, ChatHuggingFace

chat = ChatGithub()
print(chat)
chat.chat("What is the capital of France?")
