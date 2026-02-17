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


async def enable_ear():
    async with websockets.connect(WS_URL, additional_headers=HEADERS) as ws:
        hello = await ws.recv()
        print(f"Connected: {json.loads(hello).get('type')}", flush=True)
        async for message in ws:
            data = json.loads(message)
            # print(data)
            print(data["type"])  # , data["subtype"])
            if data["type"] == "user_typing":
                # print(data)
                print(data["channel"], data["user"], data.get("thread_ts", ""))


if __name__ == "__main__":
    asyncio.run(enable_ear())
