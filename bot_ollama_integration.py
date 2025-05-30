import os
from twitchio.ext import commands
from ollama import chat
from dotenv import load_dotenv

load_dotenv()


# set up the bot by inserting the variables to the .env
bot = commands.Bot(
    token=os.environ['OAUTH_TOKEN'],
    client_id=os.environ['CLIENT_ID'],
    nick=os.environ['BOT_NICK'],
    prefix=os.environ['BOT_PREFIX'],
    initial_channels=os.getenv('CHANNEL').split(",")
)
# Command to use with prefix of your choice such as ! (!test) 
@bot.command(name='test', aliases=['t'])
async def test_command(ctx):
    await ctx.send(f'Hello {ctx.author.name}')
    
@bot.command(name='woah', aliases=['wow'])
async def test_command2(ctx):
    await ctx.send(f'Oh my')

@bot.command(name="ask", aliases=["chat"])
async def chat_command(ctx: commands.Context, *, phrase: str) -> None:
    Answer = chat(model="gemma3", messages=[
        {"role": "user", "content": phrase}
    ])
    await ctx.send(Answer["message"]["content"][:500])
    print(Answer["message"]["content"])
    # await ctx.send("Did you find me helpful?") #Debug message, Commented in general use

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

@bot.command(name="check", aliases=["chk", "ck"])
async def my_command(ctx: commands.Context):
    channel_name = ctx.channel.name
    await ctx.send(f"This command was sent in {channel_name}")

@bot.command(name="checkrole", aliases=["rc", "roles"])
async def check_role(ctx: commands.Context):
    user = ctx.author
    if user.is_mod:
        await ctx.send("Rooted!")
    else:
        await ctx.send("NA")

@bot.command(name="dasknfjwknfewkjnf", aliases=["dbg"])
async def debugroles(ctx: commands.Context, status: bool = None):
    user = ctx.author
    if user.name == "loudtrex":
        await ctx.send("I recognize you!")
    else:
        await ctx.send("No, I don't recognize you!")


@bot.event
async def Ready_comm(self):
    print("Okay ready!")
    
if __name__ == "__main__":
    bot.run()
