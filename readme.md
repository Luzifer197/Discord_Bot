# Discord-Bot

## Installing Requirements
To run this project, you need to install the required libraries. Use the following command:

```bash
pip install -r requirements.txt
```

## API-Key
before you can proceesd with project, you will need API Keys for the folowing services:

### Discord:
- `Token`: add you Discord-Bot token here
- `Clientsecret`: add your Discord client secret here
- `ClientID`: Add your Discord client ID here
- `BotURL`: Add your bot invite URL here

### ChatGPT:
-`ChatGPT`: Add your ChatGPT API key here

### Unsplash:
-`unsplash`: Add your unsplash api key here


### Modifying `main.py`
In the main.py file, you should make a change in line 7. Change the path to the config.json file from:
```python
with open("./config.json", "r") as config_file:
```
to:
```python
with open("./dao/config.json", "r") as config_file:
```

Make sure that the config.json file is located in the ./dao/ directory.

After following these steps, you should be able to run the project successfully. Good luck!