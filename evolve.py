import pymysql
import requests

from Bootcamp.python.pokemon_project.pokemon.insert import insert

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="towr678",
    db="pokemon",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)


def evolve(pokemon_name):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'
    data = requests.get(url).json()
    species_url = data['species']['url']
    info = requests.get(species_url).json()
    evolution_url = info['evolution_chain']['url']
    chain = requests.get(evolution_url).json()['chain']
    while chain['species']['name'] != pokemon_name:
        if chain['evolves_to']:
            chain = chain['evolves_to'][0]
        else:
            response = {"Error": f'pokemon {pokemon_name} can not evolve'}

        new_name = chain['evolves_to'][0]['species']['name']
        pok = requests.get(url=f"https://pokeapi.co/api/v2/pokemon/{new_name}", verify=False).json()
        insert(pok)

        with connection.cursor() as cursor:
            pokemon_query = f"""UPDATE trainer_pokemon 
                            SET id = {pok['id']} WHERE  name = '{pokemon_name}'"""
            cursor.execute(pokemon_query)
            connection.commit()

        response = {"Updated": f'pokemon {pokemon_name} to {pok["name"]}'}

    return response