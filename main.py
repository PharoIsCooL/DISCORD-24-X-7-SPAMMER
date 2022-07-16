from webserver import keep_alive
import requests

channelID = https://discord.com/channels/997945274183995413/997945274741829724
headers = {
    "authorization":
    "OTkwNDA1MzM1NDcyNzk5Nzc1.GDA6TC.hU7lJ798oAN0at6Ew7bKhGg2JeofqyqQQsAiRc"
}
keep_alive()
file = open("text.txt", "r")
lines = file.readlines()

while True:
    for line in lines:
        requests.post(
            f"https://discord.com/api/v9/channels/{channelID}/messages",
            headers=headers,
            json={"content": line})
