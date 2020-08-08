import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="towr678",
    db="pokemon",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)


def owner_name_by_id(owner_id):
    with connection.cursor() as cursor:
        owner_id_query = f"""select name from owners 
                            where id = {owner_id}"""
        cursor.execute(owner_id_query)
        return cursor.fetchone()['name']


def pokemon_name_by_id(pokemon_id):
    with connection.cursor() as cursor:
        pokemon_id_query = f"""select name from pokemon 
                                where id = {pokemon_id}"""
        cursor.execute(pokemon_id_query)
        return cursor.fetchone()['name']


def insert_pokemon_to_owner(owner_id, pokemon_id):
    with connection.cursor() as cursor:
        if_exists_query = f"""select * from pokemon_owners
                            where owner_id = {owner_id} and pokemon_id = {pokemon_id}"""
        print(if_exists_query)
        cursor.execute(if_exists_query)
        if cursor.fetchone():
            response = {"Error": "this pokemon already belongs to that owner"}
        else:
            insert_query = f"""insert into pokemon_owners
                           values({owner_id}, {pokemon_id})"""
            cursor.execute(insert_query)
            connection.commit()
            response = {"Inserted": f"pokemon {pokemon_name_by_id(pokemon_id)} added to {owner_name_by_id(owner_id)}"}

    return response
