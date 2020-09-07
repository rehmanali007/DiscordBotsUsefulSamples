
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

    async def on_ready(self):
        print('Bot is ready')
        self.guild = self.get_guild(716501980603744267)
        self.channel = self.get_channel(745323070280958056)
        embed = Embed()
        embed.title = 'We are helpers!'
        embed.description = 'We are your great companion.'
        embed.timestamp = datetime.utcnow()
        embed.color = 0xFFFF00
        footer_image = 'https://image-cdn.hypb.st/https%3A%2F%2Fhypebeast.com%2Fimage%2F2020%2F02%2Fkaws-share-companion-vinyl-figures-release-info-1.jpg?q=75&w=800&cbr=1&fit=max'
        embed.set_footer(text='End of message!', icon_url=footer_image)
        image_url = 'https://www.merck-animal-health.com/wp-content/uploads/2019/09/species-companion.jpg?w=767'
        embed.set_image(url=image_url)
        thumbnail = 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSQThku5H1JVJN2jLjxc86VzXBwDeiD2afy3A&usqp=CAU'
        embed.set_thumbnail(url=thumbnail)
        author_icon = 'https://cdn.gamer-network.net/2015/usgamer/Fallout-4-Nick-Valentine-Heading.jpg/EG11/thumbnail/1920x1080/format/jpg/quality/65/26-09-2017-fallout-4-companion-guide-dogmeat-strong-cait.jpg'
        embed.set_author(name='Big Bot', icon_url=author_icon)
        embed.add_field(name='Name', value='Rehman Ali', inline=False)
        embed.add_field(
            name='Address', value='P/o Mohla Kalan, Teh and dist. Gujrat.', inline=False)
        await self.channel.send(embed=embed)

    async def on_message(self, message):
        pass


bot = Bot()
