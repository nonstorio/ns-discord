import dotenv
import grpc
import logging
from bot.Bot import Bot
from os import getenv

dotenv.load_dotenv(dotenv_path = '../.env')
logging.basicConfig(level = logging.DEBUG)

token = getenv('BOT_TOKEN')
grpc_channel = grpc.insecure_channel(getenv('GRPC_TARGET_URL'))

Bot(token, grpc_channel)
