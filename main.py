import nextcord
import json
import random
from nextcord.ext import commands
from selfFunction import log_new_member_info, get_random_image_url, log_server_info, create_server_info_log, create_member_info_log, log_ServersMember_info, add_command, help, einladungslink_sätze

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
    create_server_info_log(Bot)
    log_ServersMember_info(Bot)
    await Bot.change_presence(status=nextcord.Status.online, activity=nextcord.Game("help"))
    print(f'Logged in as {Bot.user.name} ({Bot.user.id})')
    await Bot.sync_all_application_commands()
    # Fügen Sie hier Informationen über die Befehle zum help-Dictionary hinzu

@Bot.event
async def on_guild_ready(guild):
    create_member_info_log(guild)
    
@Bot.event
async def on_guild_join(server):
    log_server_info(Bot, server)
    
@Bot.event
async def on_member_join(member):
    log_new_member_info(member, Bot)

@Bot.slash_command(
    name="einladungslink",
    description="Bekomme den Einladungslink, um den Bot in andere Server einzuladen."
)
async def get_invite_link(ctx):
    add_command("einladungslink","Bekomm ein einladungslink um Remus in andere Server hinzuzufügen")
    await ctx.send(random.choice(einladungslink_sätze) + BOTURL)

@Bot.slash_command(
    name="user",
    description="Zeigt Informationen über dich oder einen anderen Benutzer."
)
async def Profile(ctx, user: nextcord.Member = None):
    add_command("user","Zeig informationen über dich oder einen anderer Benutzer an")
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
    add_command("server", "Zeig informationen über den aktuellen Server an.")

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
    add_command("clear", "Lösche bestimmte Anzahl von Nachrichten im den aktuellen Textkanal")

    if 1 <= anzahl <= 100:
        await ctx.channel.purge(limit=anzahl + 1)
        await ctx.send(f"Habe die letzten {anzahl} Nachrichten gelöscht!")

@Bot.slash_command(
    name="help",
    description="Zeige alle Befehle von Remus an"
)
async def help(ctx):
    add_command("help", "Zeige alle Befehle von Remus an")
    
    # Erstelle ein Embed für die Befehlsliste
    embed = nextcord.Embed(
        title="Befehlsliste",
        description="Hier sind alle verfügbaren Befehle und ihre Beschreibungen:",
        color= nextcord.Colour(random.randint(0, 0xFFFFFF))  # Ändere die Farbe nach Bedarf
    )

    # Durchlaufe das help-Dictionary und füge Befehle und Beschreibungen zum Embed hinzu
    for command, description in help.items():
        embed.add_field(name=command, value=description, inline=False)

    embed.set_thumbnail(url=get_random_image_url(UNSPLASHAPI))
    # Sende das Embed in den Discord-Chat
    await ctx.send(embed=embed)
    
Bot.run(TOKEN)
