import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="towr678",
    db="pokemon",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)


def get_by_type(type_name):
    with connection.cursor() as cursor:
        pokemons_name_query = f"""select name from owners 
                               where type = '{type_name}'"""
        cursor.execute(pokemons_name_query)
        pokemons_name = cursor.fetchall()

        if not pokemons_name:
            response = {"Error": "this type does not exist"}

        else:
            response = {'pokemon names:': pokemons_name}
        return response