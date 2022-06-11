from pyrogram import Client

from .config import Config


class UtubeBot(Client):
    def __init__(self):
        super().__init__(
            name=Config.NAME,
            bot_token=Config.BOT_TOKEN,
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            plugins=dict(root="bot.plugins"),
            workers=16,
        )
        self.DOWNLOAD_WORKERS = 16
        self.counter = 0
        self.download_controller = {}
