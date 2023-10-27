import os
import requests

def get_random_image_url(api_unsplash):
    # Setzen Sie Ihren Unsplash API-Schlüssel hier ein
    unsplash_api_key = api_unsplash
    # Rufen Sie ein zufälliges Bild von Unsplash ab
    response = requests.get("https://api.unsplash.com/photos/random", headers={"Authorization": f"Client-ID {unsplash_api_key}"})
    if response.status_code == 200:
        data = response.json()
        return data["urls"]["regular"]
    else:
        return None

einladungslink_sätze = [
    "Lade mich in deinen Server ein: ",
    "Ich freue mich auf deinen Server! Hier ist der Einladungslink: ",
    "Möchtest du mich in deinem Server haben? Hier ist der Link: ",
    "Komm und hol mich in deinen Server: ",
    "Einladungslink für meinen Bot in deinen Server: ",
    "Du kannst mich zu deinem Server einladen: ",
    "Lass mich in deinem Server arbeiten! Hier ist der Einladungslink: ",
    "Hier ist der Link, um mich in deinen Server zu bringen: ",
    "Möchtest du, dass ich in deinem Server bin? Benutze diesen Link: ",
    "Füge mich zu deinem Server hinzu: ",
    "Du kannst mich in deinen Server einladen: ",
    "Hier ist der Einladungslink, um mich in deinen Server zu bringen: ",
    "Lade mich in deinen Server ein, indem du diesem Link folgst: ",
    "Ich bin bereit, deinen Server zu unterstützen. Hier ist der Link: ",
    "Füge mich zu deinem Server hinzu, indem du auf diesen Link klickst: ",
    "Möchtest du, dass ich in deinem Server arbeite? Hier ist der Einladungslink: ",
    "Hier ist der Link, um mich in deinen Server zu holen: ",
    "Du kannst mich in deinen Server einladen, indem du diesem Link folgst: ",
    "Füge mich zu deinem Server hinzu, damit ich dir helfen kann: ",
    "Ich freue mich darauf, in deinem Server zu sein. Hier ist der Einladungslink: "
]


def create_server_info_log(client):
    log_directory = "./log/"
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    log_file_path = log_directory + "bot_server_info.log"
    with open(log_file_path, "w") as log_file:
        log_file.write("Bot ist in den folgenden Servern angemeldet:\n")
        for guild in client.guilds:
            log_text = f"- Servername: {guild.name}, Server-ID: {guild.id}\n"
            log_file.write(log_text)
            print(log_text)

def log_server_info(client, guild):
    log_text = f"Bot ist dem Server beigetreten - Servername: {guild.name}, Server-ID: {guild.id}\n"

    # Ausgabe in der Befehlszeile und in die Log-Datei
    print(log_text)
    log_directory = "./log/"
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)
    log_file_path = log_directory + "bot_server_info.log"
    with open(log_file_path, "a") as log_file:
        log_file.write(log_text)

def log_new_member_info(member):
    log_text = f"Neues Mitglied beigetreten - Benutzername: {member.name}, Benutzer-ID: {member.id}, joined at: {member.joined_at.strftime('%Y-%m-%d %H:%M:%S')}\n"

    # Ausgabe in der Befehlszeile und in die Log-Datei
    print(log_text)
    log_directory = "./log/"
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)
    log_file_path = log_directory + "newMitgliederInfo.log"
    with open(log_file_path, "a") as log_file:
        log_file.write(log_text)

def create_member_info_log(guild):
    log_directory = "./log/"
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    log_file_path = log_directory + "server_member_info.log"
    with open(log_file_path, "w") as log_file:
        log_file.write(f"Mitglieder von {guild.name}")
        for member in guild.members:
            log_text = f"        - Benutzername: {member.name}, Benutzer-ID: {member.id}, joined at: {member.joined_at.strftime('%Y-%m-%d %H:%M:%S')}\n"
            log_file.write(log_text)
            print(log_text)
            
            
def log_ServersMember_info(bot):
    log_directory = "./log/"
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)
    log_file_path = log_directory + "newMitgliederInfo.log"

    with open(log_file_path, "a") as log_file:
        for guild in bot.guilds:
            server_name = guild.name
            for member in guild.members:
                username = member.name
                user_id = member.id
                join_date = member.joined_at.strftime('%Y-%m-%d %H:%M:%S')
                log_text = f"Mitglied in {server_name}({guild.id}):\n  Benutzername: {username}\n  Benutzer-ID: {user_id}\n  joined at: {join_date}\n"
                log_file.write(log_text + "\n")
                print(log_text)
            

help: dict = {}

def add_command(command_name: str, command_description: str):
    newHelp = {}
    
    for [key, description] in help:
        newHelp.update({key : description})
    
    newHelp.update({command_name : command_description})