from email.message import EmailMessage
import interactions
import json
from getemails import getemails

f = open('discord_token.json')

data = json.load(f)
token = data['token']

bot = interactions.Client(token=token)

emails = getemails()

@bot.command(
    name="verify",
    description="Verify that you are registered to ClockHacks!",
    scope='1007454289028972584',
    options = [
        interactions.Option(
            name="email",
            description="The email that you registered with",
            type=interactions.OptionType.STRING,
            required=True,
        ),
    ],
)
async def my_first_command(message: interactions.CommandContext, email: str):
    if email in emails:
        await message.send('Yes, your email has been registered!')
    else:
        await message.send('no')

bot.start()