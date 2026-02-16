import os
import websockets

from dotenv import load_dotenv

load_dotenv()
SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
SLACK_USER_TOKEN = os.getenv("SLACK_USER_TOKEN")
SLACK_USER_COOKIE = os.getenv("SLACK_USER_COOKIE")
print(SLACK_BOT_TOKEN, SLACK_USER_COOKIE, SLACK_USER_TOKEN)
