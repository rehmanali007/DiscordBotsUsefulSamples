from bot import bot
from configparser import ConfigParser


config = ConfigParser()
config.read('conf.ini')
bot_token = config['CONF']['bot_token']


bot.run(bot_token)
