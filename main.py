APIKEY = ""
WEBHOOK = ""
PLAYERNAME = input("Player name : ")


import time, requests, random
from datetime import datetime
from discord_webhook import DiscordWebhook, DiscordEmbed

chars = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
rdColor = ""
for i in range(6):
    rdColor = rdColor + random.choice(chars)
    

PLAYER_UUID = requests.get("https://api.mojang.com/users/profiles/minecraft/" + str(PLAYERNAME)).json()


PLAYER_UUID = PLAYER_UUID["id"]

print("BWsniper v1 by LegitPhase ! ' Made in 10 minutes while watching a streamer )")

print(" Player UUID : " + str(PLAYER_UUID))
print(" Starting Discord Webhooks...")
def discord_text(text):
    webhook = DiscordWebhook(url=WEBHOOK, content=str(text))
    response = webhook.execute()
def discord_embed(title,text):
    global rdColor
    webhook = DiscordWebhook(url=WEBHOOK)
    embed = DiscordEmbed(title=str(title), description=str(text), color=rdColor)
    webhook.add_embed(embed)
    response = webhook.execute()
discord_text("Started. for player : " + str(PLAYERNAME))
#print(PLAYER_DATA)
PREV_PLAYER_DATA = ""
while True :
    time.sleep(5)
    PLAYER_DATA = requests.get("https://api.hypixel.net/status?key=" + str(APIKEY) + "&uuid=" + str(PLAYER_UUID)).json()
    if PLAYER_DATA != PREV_PLAYER_DATA :
        is_online = PLAYER_DATA["session"]["online"]
        try :
            game = PLAYER_DATA["session"]["gameType"]
        except :
            game = " Offline"
        try :
            mode = PLAYER_DATA["session"]["mode"]
        except :
            mode = " Offline"
        try :
            map_ = PLAYER_DATA["session"]["map"]
        except :
            map_ = "Lobby !"
        
        if is_online == False :
            discord_embed(PLAYERNAME,"Player is not online on the Hypixel Network")
            print("Player isnt online")
        else :
            now = datetime.now()

            current_time = now.strftime("%H:%M:%S")
            print(PLAYERNAME + " is playing " + str(game) + " " + str(mode) + " on the map " + str(map_))
            discord_embed(PLAYERNAME,"\nPlaying : " + str(game) + "\nGamemode : " + str(mode) + "\nMap : " + str(map_) + "\nTime :" + str(current_time))
    PREV_PLAYER_DATA = PLAYER_DATA
