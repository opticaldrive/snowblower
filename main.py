import os
import json
import asyncio
import websockets

from dotenv import load_dotenv

load_dotenv()
SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
SLACK_USER_TOKEN = os.getenv("SLACK_USER_TOKEN")
SLACK_USER_COOKIE = os.getenv("SLACK_USER_COOKIE")

print(SLACK_BOT_TOKEN, SLACK_USER_COOKIE, SLACK_USER_TOKEN)


WS_URL = ()

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:147.0) Gecko/20100101 Firefox/147.0",
    "Origin": "https://app.slack.com",
    "Cookie": f"d={SLACK_USER_COOKIE}",
}


async def enable_ear():
    async with websockets.connect(WS_URL, additional_headers=HEADERS) as ws:
        hello = await ws.recv()
        print(f"Connected: {json.loads(hello).get('type')}", flush=True)
        async for message in ws:
            data = json.loads(message)
            print(data)


if __name__ == "__main__":
    asyncio.run(enable_ear())
