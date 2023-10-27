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
    # Überprüfe, ob das "log" Verzeichnis existiert, andernfalls erstelle es
    import os
    log_directory = "./log/"
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    # Öffne die Log-Datei im Schreibmodus und füge die Server-Informationen hinzu
    with open(log_directory + "bot_server_info.log", "w") as log_file:
        log_file.write("Bot ist in den folgenden Servern angemeldet:\n")
        for guild in client.guilds:
            log_text = f"- Servername: {guild.name}, Server-ID: {guild.id}\n"
            log_file.write(log_text)
            print(log_text)

def log_server_info(client, guild):
    log_text = f"Bot ist dem Server beigetreten - Servername: {guild.name}, Server-ID: {guild.id}\n"
    
    # Ausgabe in der Befehlszeile
    print(log_text)
    
    # Überprüfe, ob das "log" Verzeichnis existiert, andernfalls erstelle es
    import os
    log_directory = "./log/"
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    # Öffne die Log-Datei im Schreibmodus und füge die Server-Informationen hinzu
    with open(log_directory + "bot_server_info.log", "a") as log_file:
        log_file.write(log_text)