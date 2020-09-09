import api.grpc.mgmt_pb2 as mgmt_pb2
import api.grpc.mgmt_pb2_grpc as mgmt_pb2_grpc
from discord.ext.commands import (
    Cog,
    group,
    guild_only
)

class Mgmt(Cog, name = 'NS Management'):
    @group(invoke_without_command = True, aliases = ['server'])
    @guild_only()
    async def guild(self, ctx):
        """
        Data about the guild related to NS
        """
        await ctx.send(f'Guild\'s name: {ctx.guild.name}')

    @guild.command()
    async def prefix(self, ctx, prefix: str):
        """
        Use custom prefix for bot commands in guild instead of default one.
        """
        mgmt = mgmt_pb2_grpc.MgmtStub(ctx.bot.grpc_channel)
        mgmt.SetPrefix(mgmt_pb2.SetPrefixRequest(prefix = prefix))
        await ctx.send(f'This is the prefix you sent: `{prefix}`')

def setup(bot):
    bot.add_cog(Mgmt())
