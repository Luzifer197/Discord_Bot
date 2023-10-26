import requests

def get_random_image_url():
    # Setzen Sie Ihren Unsplash API-Schlüssel hier ein
    unsplash_api_key = "6-ElB1ia3oWxolxyx5JGSxnJPVJv_zLVaz0moIOuWRs"
    # Rufen Sie ein zufälliges Bild von Unsplash ab
    response = requests.get("https://api.unsplash.com/photos/random", headers={"Authorization": f"Client-ID {unsplash_api_key}"})
    if response.status_code == 200:
        data = response.json()
        return data["urls"]["regular"]
    else:
        return None
