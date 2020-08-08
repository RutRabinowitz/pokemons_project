import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="towr678",
    db="pokemon",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)


def get_by_owner(trainer_name):
    with connection.cursor() as cursor:
        owner_id_query = f"""select id from owners 
                            where name = '{trainer_name}'"""
        cursor.execute(owner_id_query)
        owner_id = cursor.fetchone()

        if not owner_id:
            response = {"Error": "this trainer does not exist"}

        else:
            pokemon_names = []
            pokemon_id_query = f"""select pokemon_id from pokemon_owners 
                                        where owner_id = {owner_id['id']}"""
            cursor.execute(pokemon_id_query)
            pokemon_ids = cursor.fetchall()

            for pokemon_id in pokemon_ids:
                pokemon_name_query = f"""select name from pokemon
                                        where id = {pokemon_id['pokemon_id']}"""
                cursor.execute(pokemon_name_query)
                pokemon_name = cursor.fetchone()['name']
                pokemon_names.append(pokemon_name)

            response = {'pokemon names': pokemon_names}
        return response


