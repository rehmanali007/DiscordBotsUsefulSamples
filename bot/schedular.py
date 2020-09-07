from discord.ext.commands import Bot as BaseBot
from discord import Embed
from datetime import datetime
from apscheduler.triggers.cron import CronTrigger
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from configparser import ConfigParser

PREFIX = '!'


class Bot(BaseBot):
    def __init__(self):
        self.prefix = PREFIX
        self.ready = False
        self.guild = None
        self.scheduler = AsyncIOScheduler()
        super().__init__(command_prefix=PREFIX)

    def run(self, token):
        super().run(token)

    async def on_connect(self):
        print('Bot is connected!')

    async def on_disconnect(self):
        print('Bot disconnected!')

    @staticmethod
    def timed(msg, channel):
        async def inner_timed():
            await channel.send(msg)
        return inner_timed

    async def on_ready(self):
        print('Bot is ready')
        self.guild = self.get_guild(716501980603744267)
        self.channel = self.get_channel(745323070280958056)
        self.scheduler.add_job(self.timed('Hello', self.channel), CronTrigger(
            second="0,10,20,30,40,50"))
        self.scheduler.start()
        await self.channel.send('Now Online.')

    async def on_message(self, message):
        pass


bot = Bot()
