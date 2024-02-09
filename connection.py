import requests

url = 'https://rickandmortyapi.com/api/'
point = 'character'

req = requests.get(url + point)

data = req.json()

def get_img(index):
    return data['results'][index]['image']


def get_name(index):
    return data['results'][index]['name']

def get_status(index):
    return data['results'][index]['status']

def get_species(index):
    return data['results'][index]['species']

def get_last_location(index):
    return data['results'][index]['location']['name']

def get_first_location(index):
    return data['results'][index]['location']['name']
