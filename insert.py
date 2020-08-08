import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="towr678",
    db="pokemon",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)


def insert(new_pokemon):
    if new_pokemon.get('id') and new_pokemon.get('name') and new_pokemon.get('type') and new_pokemon.get(
            'height') and new_pokemon.get('weight'):
        with connection.cursor() as cursor:
            query = f"""INSERT into pokemon (id, name, type, height, weight) 
                    VALUES({new_pokemon['id']}, '{new_pokemon['name']}', '{new_pokemon['type']}', {new_pokemon['height']}, {new_pokemon['weight']})""".format()
            cursor.execute(query)
            connection.commit()
        return {"Created": new_pokemon}
    else:
        return {"Error": "data keys are wrong"}
