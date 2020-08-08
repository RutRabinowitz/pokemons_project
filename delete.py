import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="towr678",
    db="pokemon",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)


def is_valid_keys(dict_, *args):
    for arg in args:
        if not dict_.get(arg):
            return False
    return True


def get_owner_id_by_name(owner_name):
    with connection.cursor() as cursor:
        owner_id_query = f"""select id from owners 
                            where name = '{owner_name}'"""
        cursor.execute(owner_id_query)
        return cursor.fetchone()


def get_id_by_name(pokemon_name):
    with connection.cursor() as cursor:
        pokemon_id_query = f"""select id from pokemon 
                                where name = '{pokemon_name}'"""
        cursor.execute(pokemon_id_query)
        return cursor.fetchone()


def delete(pokemon_to_delete):
    with connection.cursor() as cursor:
        query = f"""delete from pokemon_owners 
                    where pokemon_id = {pokemon_to_delete['pokemon_id']}"""
        cursor.execute(query)
        connection.commit()


def pokemon_to_owner(owner_id, pokemon_id):
    with connection.cursor() as cursor:
        query = f"""select * from pokemon_owners 
                where owner_id = {owner_id['id']} and  pokemon_id = {pokemon_id['id']}"""
        cursor.execute(query)

        return cursor.fetchone()


def delete_pokemon(pokemon_name, trainer_name):
    owner_id = get_owner_id_by_name(trainer_name)
    pokemon_id = get_id_by_name(pokemon_name)
    if not owner_id or not pokemon_id:
        response = {"Error": "this pokemon or trainer does not exist"}
    else:
        pokemon_to_delete = pokemon_to_owner(owner_id, pokemon_id)

        if pokemon_to_delete:
            delete(pokemon_to_delete)
            response = {"Deleted": {'trainer name': trainer_name, 'pokemon name': pokemon_name}}
        else:
            response = {"Error": "this pokemon does not belong to that trainer"}
    return response


