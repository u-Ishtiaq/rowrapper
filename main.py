import requests
from roblox import Client
from fastapi import FastAPI


app = FastAPI()

#generates client object called client
client = Client()





#gets accessories worn by a player (includes 3d jackets)
@app.get("/player-accessories")
async def get_player_accessories(playerId):

  
  URL = requests.get("https://avatar.roblox.com/v1/users/" + str(playerId) + "/currently-wearing")
  user_data = URL.json()
#asset ids in json form

  return user_data
