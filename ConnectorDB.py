import mysql.connector as connector

config = {
    'user': 'root',
    'password': '',
    'host': '127.0.0.1',
    'database': 'bank_db',
    'raise_on_warnings': True
}

connection_to_mysql = connector.connect(**config)
cursor = connection_to_mysql.cursor()


def read_script(script):
    try:
        cursor.execute(script)
        print('Script executado com sucesso')
        return cursor
    except connector.errors:
        connection_to_mysql.rollback()


def execute_script(script):
    try:
        cursor.execute(script)
        connection_to_mysql.commit()
        print('Script executado com sucesso')
        return cursor
    except connector.errors:
        connection_to_mysql.rollback()


def close_connection():
    if connection_to_mysql.is_connected():
        cursor.close()
        connection_to_mysql.close()
