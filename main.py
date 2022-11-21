from email.message import EmailMessage
from http import client
from attr import fields
import interactions
import json
from getemails import getemails, getdiscords
from sendemail import sendemail

f = open('discord_token.json')

data = json.load(f)
token = data['token']

client = interactions.Client(token=token)

scope = '1007454289028972584'
organizer = 1007454489596412084

@client.event 
async def on_ready():
    print(f'\n\033[92mBot is ready!\033[0m\n')

@client.command(
    name="verify",
    description='Verify your registration to ClockHacks, and get assigned the hacker role and channel',
    scope=scope,
    options = [
        interactions.Option(
            name="email",
            description="The email that you registered with",
            type=interactions.OptionType.STRING,
            required=True,
        ),
    ]
)
async def verify(message: interactions.CommandContext, email: str):
    things = getemails()
    emails = things[0]
    names = things[1]
    discords = getdiscords()
    if email not in emails:
        await message.send('Oh no! We couldn\'t find you on the list of registered users. Here\'s what could have happened:\n\n1. You haven\'t registered yet. Do so here: clockhacks.ca\n\n2. You registered, but you didn\'t put the email that you registered with. Please check that you have the right email and try again.\n\n3. You registered, but the API wasn\'t able to find you on the list of users. Here\'s what you should do: Try again in 10-15 minutes.\n\n4. You put in the correct email, but you have changed your Discord name since your registration.\n\nIf the problem persists, contact one of our organizers in the Discord server.', ephemeral=True)
        print(f'{message.author.username} not found')
        return
    

    discord = discords[emails.index(email)]
    if email in emails and f"{message.user.username}#{message.user.discriminator}" == discord:
        if 1030284402841894943 in message.author.roles:
            await message.send('Success! You\'ve already verified, and have full access to the server.', ephemeral=True)
            print('already verified')
        else:
            try:
                name = names[emails.index(email)]
                await message.author.modify(int(scope), nick=name)
            except:
                await message.send('Either something went wrong, or you\'re too cool for me to do that', ephemeral=True)
                print(f'{message.author.username} nick error')
                return
            await message.author.add_role(1030284402841894943)
            await message.send('Success! You now have the Hacker role, and full access to the server.', ephemeral=True)
            print(name, 'verified')

    else:
        await message.send('That email is registered, but it\'s either not your email or doesn\'t have your email in the registration. Please check to make sure you have the right email. If the problem persists, contact an organizer in the Discord.', ephemeral=True)
        print('this happened')

@client.command(
    name='guilds',
    description='Show all guilds that the bot is in',
    scope=scope
)
async def guilds(message: interactions.CommandContext):
    if organizer not in message.author.roles:
        return
    await message.send(str(client.guilds), ephemeral=True)

@client.command(
    name='ping',
    description='Shows command latency',
    scope=scope
)
async def guilds(message: interactions.CommandContext):
    if organizer not in message.author.roles:
        return
    await message.send(f'I take about {str("{:10.2f}".format(client.latency)).strip()} milliseconds to respond.', ephemeral=True)

@client.command(
    name='links',
    description = 'Important links for ClockHacks',
    scope=scope,
    options = [
        interactions.Option(
            name="ephemeral",
            description="Replies publicly or ephemerally",
            type=interactions.OptionType.BOOLEAN,
            required=False,
        ),
    ]
)
async def links(message: interactions.CommandContext, ephemeral:bool=True):
    embed = interactions.Embed(
        title="Important Links",
        color=interactions.Color.green(),
        description="""https://linktr.ee/clockhacks

[Website](https://clockhacks.ca/)
[Registration](https://docs.google.com/forms/d/e/1FAIpQLSdUDbXhQ3MCTsl_e0mp4dS-uRLHbbAZH5LePfpVzFSEvUrZog/viewform)
[LinkedIn](https://www.linkedin.com/company/clockhacks/?viewAsMember=true)
[Discord](https://discord.com/invite/UKjQBdy26S)
[Instagram](https://www.instagram.com/clockhacks/)
[Devpost](https://clockhacks.devpost.com/)
[MLH](https://mlh.io/seasons/2023/events)
"""
    )
    await message.send(embeds=embed, ephemeral=ephemeral)

client.start()