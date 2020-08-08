from flask import Flask, Response, request
import pymysql
import json

from Bootcamp.python.pokemon_project.add_pokemon_to_owner import insert_pokemon_to_owner
from Bootcamp.python.pokemon_project.pokemon.delete import delete_pokemon, get_owner_id_by_name
from Bootcamp.python.pokemon_project.pokemon.get_by_trainer import get_by_owner
from Bootcamp.python.pokemon_project.pokemon.insert import insert
from Bootcamp.python.pokemon_project.pokemon.get_by_type import get_by_type
from Bootcamp.python.pokemon_project.pokemon.evolve import evolve

app = Flask(__name__)

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="towr678",
    db="pokemon",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)


@app.route('/add', methods=["POST"])
def add():
    new_pokemon = request.get_json()
    response = insert(new_pokemon)

    if response.get("Error"):
        return json.dumps(response), 402
    return json.dumps(response), 201


@app.route('/pokemons_by_trainer/<trainer_name>')
def get_pokemons_by_trainer(trainer_name):
    response = get_by_owner(trainer_name)

    if response.get("Error"):
        return json.dumps(response), 402
    return json.dumps(response), 201


@app.route('/pokemons_by_type/<type_name>')
def get_pokemons_by_type(type_name):
    response = get_by_type(type_name)

    if response.get("Error"):
        return json.dumps(response), 402
    return json.dumps(response), 201


@app.route('/delete/<pokemon_name>/<trainer_name>', methods=["DELETE"])
def delete(pokemon_name, trainer_name):
    response = delete_pokemon(pokemon_name, trainer_name)

    if response.get("Error"):
        return json.dumps(response), 402
    return json.dumps(response), 201


@app.route('/evolve/<pokemon_name>', methods=["PUT"])
def evolve_pokemon(pokemon_name):
    response = evolve(pokemon_name)

    if response.get("Error"):
        return json.dumps(response), 402
    return json.dumps(response), 201


@app.route('/add_pokemon_to_owner/<owner_name>/<pokemon_id>', methods=["POST"])
def add_pokemon_to_owner(owner_name, pokemon_id):
    owner_id = get_owner_id_by_name(owner_name)['id']
    response = insert_pokemon_to_owner(owner_id, pokemon_id)
    if response.get("Error"):
        return json.dumps(response), 402
    return json.dumps(response), 201


if __name__ == '__main__':
    app.run(port=1337)
