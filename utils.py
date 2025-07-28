import requests

def get_steam_id(vanity_url, API_KEY, steam_url='http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/'):
    params = {'key': API_KEY, 'vanityurl': vanity_url}
    response = requests.get(steam_url, params=params)
    return response.json()['response']['steamid']


def get_games_stats(steam_id, API_KEY, steam_url = 'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/'):
    params = {'key': API_KEY, 'steamid': steam_id, 'format': 'json'}
    response = requests.get(steam_url, params=params)
    return response.json()['response']['games']

