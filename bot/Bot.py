import grpc
import logging
from datetime import datetime
from bot.const import MISC
from discord.ext import commands

def get_prefix(client, message):
    prefixes = [MISC.LONG_PREFIX, MISC.SHORT_PREFIX]
    if not message.guild:
        prefixes.extend([''])
    return commands.when_mentioned_or(*prefixes)(client, message)

class Bot(commands.Bot):
    extensions = [
        'bot.cogs.Mgmt'
    ]

    def __init__(self, token, grpc_channel: grpc.Channel):
        super().__init__(
            command_prefix = get_prefix,
            case_insensitive = True,
            description = MISC.DESCRIPTION,
        )

        self.grpc_channel = grpc_channel

        for ext in self.extensions:
            self.load_extension(ext)

        self.run(token, bot = True, reconnect = True)

    async def on_ready(self):
        print(f'Logged in as {self.user.name}#{self.user.discriminator}')

        logging.debug(f'Logged in at `{datetime.now()}`')
