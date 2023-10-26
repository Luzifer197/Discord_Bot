import nextcord
import json
import random
from nextcord.ext import commands
from selfFunction import get_random_image_url

with open("./config.json", "r") as config_file: #change path do ./dao/config.json
    config_data = json.load(config_file)

TOKEN = config_data["Discord"]["Token"]
BOTURL = config_data["Discord"]["BotURL"]
UNSPLASHAPI = config_data["unsplash"]

intents = nextcord.Intents.all()
intents.message_content = True
intents.members = True

Bot = commands.Bot(command_prefix='!', intents=intents)
Bot.remove_command("help")

@Bot.event
async def on_ready():
    await Bot.change_presence(status=nextcord.Status.online, activity=nextcord.Game("help"))
    print(f'Logged in as {Bot.user.name} ({Bot.user.id})')
    await Bot.sync_all_application_commands()

@Bot.event
async def on_disconnect():
    await Bot.change_presence(status=nextcord.Status.offline, activity=nextcord.Game(""))

@Bot.slash_command(
    name="einladungslink",
    description="Bekomme den Einladungslink, um den Bot in andere Server einzuladen."
)
async def get_invite_link(ctx):
    await ctx.send('Hier bekommst du meinen Einladungslink: ' + BOTURL)

@Bot.slash_command(
    name="user",
    description="Zeigt Informationen über dich oder einen anderen Benutzer."
)
async def Profile(ctx, user: nextcord.Member = None):
    if user is None:
        user = ctx.user

    inline = True
    embed = nextcord.Embed(
        title=f"{user.name}#{user.discriminator}",
        color=nextcord.Colour(random.randint(0, 0xFFFFFF))
    )

    userData = {
        "Erwähnung": user.mention,
        "Benutzername": user.name,
        "Diskriminator": user.discriminator,
        "Spitzname": user.nick,
        "Erstellt am": user.created_at.strftime("%Y-%m-%d %H:%M:%S"),
        "Beigetreten am": user.joined_at.strftime("%Y-%m-%d %H:%M:%S"),
        "Server": user.guild.name,
        "Server-ID": user.guild.id,
        "Höchste Rolle": user.top_role.name
    }

    for fieldName, fieldValue in userData.items():
        embed.add_field(
            name=f"{fieldName}:",
            value=fieldValue,
            inline=inline
        )

    embed.set_footer(text=f"ID: {user.id}")
    embed.set_thumbnail(url=user.display_avatar.url)

    await ctx.send(embed=embed)


@Bot.slash_command(
    name="server",
    description="Zeigt Informationen über den aktuellen Server."
)
async def server_info(ctx):
    server = ctx.guild

    inline = True
    color = nextcord.Colour(random.randint(0, 0xFFFFFF))  #Create random Colors
    embed = nextcord.Embed(
        title=f"Server-Info - {server.name}",
        color=color
    )

    server_data = {
        "Servername": server.name,
        "Mitgliederanzahl": server.member_count,
        "Server-Besitzer": server.owner.mention,
        "Server-Region": str(server.region),
        "Server-ID": server.id,
    }

    for fieldName, fieldValue in server_data.items():
        embed.add_field(
            name=f"{fieldName}:",
            value=fieldValue,
            inline=inline
        )

    embed.set_footer(text=f"Server-ID: {server.id}")
    embed.set_thumbnail(url=get_random_image_url(UNSPLASHAPI))

    await ctx.send(embed=embed)

@Bot.slash_command(
    name="clear",
    description="Löscht eine bestimmte Anzahl von Nachrichten im Textkanal.",
)
async def clear_messages(ctx, anzahl: int):
    if 1 <= anzahl <= 100:
        await ctx.channel.purge(limit=anzahl + 1)
        await ctx.send(f"Habe die letzten {anzahl} Nachrichten gelöscht!")


Bot.run(TOKEN)
