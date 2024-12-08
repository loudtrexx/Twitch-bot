import os
from twitchio.ext import commands

# set up the bot
bot = commands.Bot(
    token=os.environ['OAUTH_TOKEN'],
    client_id=os.environ['CLIENT_ID'],
    nick=os.environ['BOT_NICK'],
    prefix=os.environ['BOT_PREFIX'],
    initial_channels=[os.environ['CHANNEL']]
)

@bot.command(name='test', aliases=['t'])
async def test_command(ctx):
    await ctx.send(f'Hello {ctx.author.name}')
    
@bot.command(name='woah', aliases=['wow'])
async def test_command2(ctx):
    await ctx.send(f'Oh my')

@bot.command(name='introduce', aliases=['int'])
async def int_command(ctx):
    await ctx.send(f'Hello! I am a bot created by @loudtrex to show how skillfull he can be! If you see this massage you are amazing!')
    
@bot.command(name='counter', aliases=['count'])
async def test_command(ctx, user_name: str = None):
    if user_name:
        await ctx.send(f"Hello, {user_name}!")
    else:
        await ctx.send("Hello, chat!")

@bot.event
async def Ready_comm():
    print("Okay ready!")
    
if __name__ == "__main__":
    bot.run()