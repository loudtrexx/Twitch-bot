import os
from twitchio.ext import commands
from ollama import chat


# set up the bot by inserting the variables to the .env
bot = commands.Bot(
    token=os.environ['OAUTH_TOKEN'],
    client_id=os.environ['CLIENT_ID'],
    nick=os.environ['BOT_NICK'],
    prefix=os.environ['BOT_PREFIX'],
    initial_channels=[os.environ['CHANNEL']]
)
# Command to use with prefix of your choice such as ! (!test)
@bot.command(name='test', aliases=['t'])
async def test_command(ctx):
    await ctx.send(f'Hello {ctx.author.name}')
    
@bot.command(name='woah', aliases=['wow'])
async def test_command2(ctx):
    await ctx.send(f'Oh my')

@bot.command(name="ask")
async def chat_command(ctx: commands.Context, *, phrase: str) -> None:
    Answer = chat(model="llama3.2", messages=[
        {"role": "user", "content": phrase}
    ])
    await ctx.send(Answer["message"]["content"])
    print(Answer["message"]["content"])
    await ctx.send("Did you find me helpful?")

@bot.command(name="simple")
async def echo(ctx: commands.Context, *, phrase: str) -> None:
    response = f"Echo {phrase}"
    await ctx.send(response)

#@bot.command(name='introduce', aliases=['int'])
#async def int_command(ctx):
 #   await ctx.send(f'Hello! I am a bot created by @loudtrex to show how skillfull he can be! If you see this massage you are amazing!')
    
@bot.command(name='counter', aliases=['count'])
async def test_command(ctx, user_name: str = None):
    if user_name:
        await ctx.send(f"Hello, {user_name}!")
    else:
        await ctx.send("Hello, chat!")

@bot.event
async def Ready_comm(self):
    print("Okay ready!")
    
if __name__ == "__main__":
    bot.run()
