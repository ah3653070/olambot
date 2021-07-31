from os import name
from pyrogram import Client
from sample_cofig import (
    API_ID,
    API_HASH,
    BOT_TOKEN
)


class OlamBot(Client):
    def __init__(self):
        super().__init__(
            "olambot",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN
        )

    async def start(self):
        await super().start()
        print(f"BOT IS ONLINE !")

    async def stop(self, *arg):
        await super().stop()
