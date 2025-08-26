import requests

def get_steam_id(vanity_url, API_KEY, steam_url='http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/'):
    params = {'key': API_KEY, 'vanityurl': vanity_url}
    response = requests.get(steam_url, params=params)
    return response.json()['response']['steamid']


def get_games_stats(steam_id, API_KEY, steam_url = 'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/'):
    params = {'key': API_KEY, 'steamid': steam_id, 'format': 'json'}
    response = requests.get(steam_url, params=params)
    return response.json()['response']['games']

def get_game_data(game_id, steam_url='https://store.steampowered.com/api/appdetails'):
    
    relevant_app_details = {}

    params = {'appids': game_id}
    response = requests.get(steam_url, params=params)
    data = response.json()
    
    if data[str(game_id)]['success']:

        try:
            relevant_app_details = {
                "name": data[str(game_id)]['data']['name'],
                "genres": data[str(game_id)]['data']['genres'],
                #"ratings": data[str(game_id)]['data']['ratings'],
                "categories": data[str(game_id)]['data']['categories'],
                "required_age": data[str(game_id)]['data']['required_age']
            }
        except KeyError as e:
            print(f"El juego {game_id} no tiene la clave: {e}")
            relevant_app_details = {
                "name": data[str(game_id)]['data']['name'],
                "genres": None,
                "categories": data[str(game_id)]['data'].get('categories', None),
                #"ratings": data[str(game_id)]['data'].get('ratings', None),
                "required_age": data[str(game_id)]['data'].get('required_age', None)
            }

    return relevant_app_details

def is_porn(game_data):
    if int(game_data.get('required_age', 0)) >= 18:
        return True
