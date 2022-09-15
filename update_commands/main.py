import requests

GUILD_ID = "REPLACE_ME"
APP_ID = "REPLACE_ME"
BOT_TOKEN = "REPLACE_ME"

# Create or update commmands.
# global commands are cached and only update every hour
url = f"https://discord.com/api/v8/applications/{APP_ID}/commands"

# while guild commands update instantly
# they're much better for testing
# url = f'https://discord.com/api/v8/applications/{APP_ID}/guilds/{GUILD_ID}/commands'

json = {
    "name": "askmike",
    "type": 1,
    "description": "Ask Mike a question",
    "options": [
        {
            "name": "question",
            "description": "Whaddya got for me?",
            "type": 3,
            "required": True,
        }
    ],
}
headers = {"Authorization": f"Bot {BOT_TOKEN}"}
response = requests.post(url, headers=headers, json=json)

print(response.text)


# Get current commands.
# get_app_commands = f'https://discord.com/api/v10/applications/{APP_ID}/commands'
# get_guilds_commands = f'https://discord.com/api/v10/applications/{APP_ID}/guilds/{GUILD_ID}/commands'
# r = requests.get(get_guilds_commands, headers=headers)
# print(r)
# print(r.text)


# Delete current commands.
# /bleb 1019844354006843443
# bleb_id = '1019844354006843443'
# delete_url = f'https://discord.com/api/v10/applications/{APP_ID}/guilds/{GUILD_ID}/commands/{bleb_id}'
# r = requests.delete(delete_url, headers=headers)
# print(r)
# print(r.text)
