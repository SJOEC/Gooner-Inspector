import utils
import json
from utils import *

with open('DEV_INFO.json', 'r') as f:
    data = json.load(f)

API_KEY = data['API_KEY']

print(API_KEY)

if __name__ == '__main__':
    user_games_data = []
    porn = []

    steam_url = 'https://api.steampowered.com/ISteamUser/ResolveVanityURL/v1/'
    vanity_url = 'Bl4ky113'

    user_steam_id = utils.get_steam_id(vanity_url, API_KEY)
    user_games = utils.get_games_stats(user_steam_id, API_KEY)

    print(user_steam_id)
    
    for game in user_games:
        user_games_data.append(utils.get_game_data(game['appid']))

    for game in user_games_data:
        if utils.is_porn(game):
            porn.append(game['name'])

    print(porn)

    print(user_games)









